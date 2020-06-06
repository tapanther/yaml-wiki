#! /usr/bin/env python3

import argparse
import yaml
import re
import warnings

from operator import attrgetter
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, contextfilter
from shutil import rmtree
from os import symlink
from anytree import Node, RenderTree, Resolver, PreOrderIter, LevelOrderGroupIter
from anytree.resolver import ResolverError, ChildResolverError
from os import PathLike
from typing import Union, Tuple, Optional
from dateutil.parser import parse as dateparse

from pprint import PrettyPrinter

_pp = PrettyPrinter(indent=1).pprint

# Global helper to store parsed command line arguments
_args: argparse.Namespace = argparse.Namespace()

# Global helper to store the Jinja environment
_env: Environment = Environment()

# Global helper to store links
_global_links = list()


# ---------------------
# Parse Arguments
# ---------------------

def parse_arguments():
    """
    Parse command line arguments to a global variable.

    Returns
    -------
    None
        Sets global _args variable to store command line arguments.
    """
    global _args

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-y',
        '--yaml-cfg',
        default='wiki.yml',
        help='Wiki configuration file, in lieu of passed options.'
    )

    parser.add_argument(
        '-o',
        '--output',
        default='./docs',
        help='Output root directory. Defaults to "./docs"'
    )

    parser.add_argument(
        '-t',
        '--templates',
        default='./templates',
        help='Directory path to get custom templates from. Defaults to "./templates"'
    )

    parser.add_argument(
        '-l',
        '--lib',
        default='./lib',
        help='Root library directory. Defaults to "./lib"'
    )

    parser.add_argument(
        '--stylesheets',
        help='Directory relative to --lib to get custom stylesheets. Note: stylesheets must be added to mkdocs.yml.j2'
    )

    parser.add_argument(
        '--js',
        help='Directory relative to --lib to get custom javascript. Note: js must be added to mkdocs.yml.j2'
    )

    parser.add_argument(
        '--img',
        help='Directory relative to --lib to get custom images.'
    )

    parser.add_argument(
        '-v',
        '--verbose',
        default=0,
        action='count',
        help='Print debug information.'
    )

    args = parser.parse_args()

    wiki_cfg = Path(args.yaml_cfg)
    if wiki_cfg.exists():
        with open(wiki_cfg, 'r') as wiki_cfg_file:
            cfg_data = yaml.load(wiki_cfg_file, Loader=yaml.FullLoader)

        for key, value in cfg_data.items():
            cmd_val = getattr(args, key, None)
            if cmd_val is None:
                setattr(args, key, value)
            else:
                msg = f'{key} from WikiCfg overridden by command line: {cmd_val}'
                warnings.warn(msg)

    _args = args


# --------------------------
# Helper Functions
# --------------------------

DateOrNone = Optional[datetime]


def is_date(string: str, fuzzy: bool = False) -> DateOrNone:
    """
    Uses the dateutils parser to check if a string is a standard date format.

    Parameters
    ----------
    string : str
        String to test for date-y-ness
    fuzzy : bool
        Controls if "fuzzy" formats are allowed ("Today is January 1 of 2020")

    Returns
    -------
    DateOrNone
        None if the string is not a date, otherwise datetime.datetime object

    """
    try:
        return dateparse(string, fuzzy=fuzzy)
    except ValueError:
        return False


DateTuple: Tuple = Tuple[int, int, int]
"""Tuple of three integers."""


def age_decode(event: str) -> DateTuple:
    """Decode Tritanian-style date strings to (Y, M, D) integers.

    Tritan Date-Strings have a special pattern {###}Y {##}M [{##}]<Day>
    This function converts them into a tuple of numbers that represent
    year, month, day as sortable numbers.

    Parameters
    ----------
    event : str
        Tritanian Date-String

    Returns
    -------
    DateTuple
        (Year, Month, Day)
    """
    age_str = event['Date']
    date = is_date(age_str)
    if date:
        timetuple = date.timetuple()
        return timetuple[0], timetuple[1], timetuple[2]
    else:
        map_ = {'KAL': 1, 'IDE': 20, 'NON': 28, 'X': 2}
        age_list = age_str.split(' ')
        age_list.extend(['0KAL', '0KAL', '0KAL'])
        age_list[0] = int(re.sub(r'[^- 0-9]', '', age_list[0]))
        age_list[1] = int(re.sub(r'[^ 0-9]', '', age_list[1]))
        try:
            day = int(re.sub(r'([0-9]*).*', r'\1', age_list[2]))
        except ValueError:
            day = 1
        mark = re.sub(r'[0-9]*(KAL|IDE|NON|X)', r'\1', age_list[2])
        age_list[2] = (32 - map_[mark] - (day - 2)) % 31

    return age_list[0], age_list[1], age_list[2]


def resolve_tree_node(tree: Node, path_str: str) -> Node:
    """Given a path string, return the corresponding node from a tree

    Parameters
    ----------
    tree : Node
        anytree Node object
    path_str : str
        String representation of anytree node path

    Returns
    -------
    Node
        Referenced anytree Node object
    """
    resolver = Resolver('name')
    try:
        node = resolver.get(tree, path_str)
    except (ResolverError, ChildResolverError):
        parent = resolve_tree_node(tree, path_str.rsplit('/', 1)[0])
        node = Node(path_str.split('/')[-1], parent=parent)

    return node


# --------------------------
# Custom Jinja Filters
# --------------------------

@contextfilter
def auto_link(ctx, raw_text):
    """Jinja2 Custom Filter to automatically link keywords in text to their pages.

    Parameters
    ----------
    ctx : jinja2.runtime.Context
        Template Context
    raw_text : str
        Template text

    Returns
    -------
    str
        `raw_text` with known keywords linked to their pages
    """
    if 'no_autolink' in ctx.resolve('control'):
        return raw_text
    my_title = ctx.resolve('title')
    for linkTarget in _global_links:
        search_text = linkTarget['text']
        link_text = linkTarget['link']
        if link_text != my_title:
            search_pattern = r'\b' + f"({search_text}('?s?)?)" + r'\b' + r'(?![^[]*])'
            replace_text = r'[\1]' + f'[{link_text}]'
            raw_text = re.sub(search_pattern, replace_text, raw_text, count=1)
    return raw_text


@contextfilter
def relative_link(ctx, raw_text):
    """Inject mermaid-style relative links.

    Mermaid diagrams use relative links to the generated HTML, rather than
    markdown-style links to named references.

    Parameters
    ----------
    ctx : jinja2.runtime.Context
        Template Context
    raw_text : str
        Template text

    Returns
    -------
    str
        `raw_text` with known keywords linked to their generated pages

    """
    my_title = ctx.resolve('title')
    for linkTarget in _global_links:
        search_text = linkTarget['text']
        link_text = linkTarget['file'].split('.', 1)[0]
        if link_text != my_title:
            search_pattern = f'(click .*?) "({search_text}(\'?s?)?)"'
            replace_text = f'\g<1> "../{link_text}/"'
            raw_text = re.sub(search_pattern, replace_text, raw_text)
    unresolved_text = r'click .*? "((?!\.\./).*?)"'
    unresolved_links = re.findall(unresolved_text, raw_text)
    if unresolved_links:
        for u_link_match in unresolved_links:
            msg = f'Unresolved mermaid link in {ctx.resolve("yml_file")} : {u_link_match}'
            warnings.warn(msg, stacklevel=7)
    return raw_text


def sort_multi(list_in, *operators):
    """Jinja2 Custom Filter to sort by multiple attributes

    Parameters
    ----------
    list_in : list
    operators : \*attrs
        `operator.attrgetter` style attributes to retrieve

    Returns
    -------
    list
        Sorted list based on attributes specified
    """
    list_sorted = sorted(list_in, key=attrgetter(*operators))
    return list_sorted


def stringify_keys(dictionary):
    """
    Jinja filter to convert all keys in a dictionary to strings.

    Parameters
    ----------
    dictionary : dict
        dictionary to process

    Returns
    -------
    dict
        original `dictionary` with keys converted to strings

    """
    new_dict = dict((str(k), v) for k, v in dictionary.items())
    return new_dict


def number_format(value):
    """
    Attempt to format a string as a number

    Parameters
    ----------
    value : str
        String which could be a number

    Returns
    -------
    str
        String with comma separators for thousands if number, otherwise
        just the original string.

    """
    try:
        formatted_str = format(int(value), ',d')
    except (TypeError, ValueError):
        formatted_str = value
    return formatted_str


def list_text(text):
    """
    Jinja2 filter to allow text to be properly formatted as a list in markdown

    Parameters
    ----------
    text : str

    Returns
    -------
    str
        `text` with corrected indentation to support markdown lists

    """
    return '\n    '.join(text.split('\n'))


def get_tree_direct_children(tree):
    """
    Get only the direct children of a given anytree Node

    Parameters
    ----------
    tree : Node

    Returns
    -------
    List[Node]
        Child-less nodes first, then sorted by name.

    """
    childless = [[node for node in children] for children in LevelOrderGroupIter(tree,
                                                                                 filter_=lambda n: not n.children)][1]
    childed = [[node for node in children] for children in LevelOrderGroupIter(tree, filter_=lambda n: n.children)][1]
    # Sort the lists
    childless.sort(key=lambda x: x.name)
    childed.sort(key=lambda x: x.name)
    return childless + childed


StringOrInteger = Union[str, int]


def human_sort_int_first(txt):
    """
    Human-sort strings that contain numbers.

    For example, `["10", "5", "51"]` should sort as
    `["5", "10", "51"]`

    Parameters
    ----------
    txt : str

    Returns
    -------
    StringOrInteger, str
        The numerical interpretation of the string (if any) and the original text.
    """
    if isinstance(txt, int):
        number = txt
        txt = str(number)
    else:
        num_match = re.search(r'[0-9]+', txt).group(0)
        number = int(num_match) if num_match is not None else -1
    return number, txt


def roll_sort(dictionary):
    """
    Jinja filter to sort dictionaries using human sort.

    Typically used to sort roll tables `{"roll value" : "result" }`

    Parameters
    ----------
    dictionary : dict

    Returns
    -------
    List[Tuple[str, object]]
        sorted list of (key, value) tuples

    """
    sorted_list = [(key, dictionary[key]) for key in sorted(dictionary, key=human_sort_int_first)]
    return sorted_list


class SafeLoaderIgnoreUnknown(yaml.SafeLoader):
    @staticmethod
    def default_ctor(loader, tag_suffix, node):
        """
        YAML Loader that safely ignores python object tags

        Parameters
        ----------
        loader
        tag_suffix
        node

        Returns
        -------
        str

        """
        return tag_suffix + ' ' + node.value


# --------------------------
# Sequencer
# --------------------------

def setup_jinja():
    """
    Set up Jinja2 Environment for templates.
    """
    global _env

    # Add in the default library
    template_lib = [_args.templates, './yaml-wiki/templates']

    env = Environment(
        loader=FileSystemLoader(template_lib),
        extensions=['jinja2.ext.do'],
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Add Custom Filters
    env.filters['auto_link'] = auto_link
    env.filters['relative_link'] = relative_link
    env.filters['number_format'] = number_format
    env.filters['list_text'] = list_text
    env.filters['sort_multi'] = sort_multi
    env.filters['stringify_keys'] = stringify_keys
    env.filters['get_tree_direct_children'] = get_tree_direct_children
    env.filters['roll_sort'] = roll_sort

    _env = env


def main():
    """
    Main function.

    This function builds the wiki navigation tree, then runs the
    Jinja template engine to write out the markdown pages.
    """
    global _global_links

    parse_arguments()

    setup_jinja()

    outdir = Path(_args.output)
    if outdir.exists():
        rmtree(outdir)

    outdir.mkdir(parents=True, exist_ok=True)

    # ---------------------
    # Prepare the nav
    # ---------------------

    nav_tree = Node('Root')
    date = datetime.today().strftime('%Y-%m-%d')

    timeline_struct = list()

    md_lib = list()

    path: Union[Path, PathLike]
    for path in Path(_args.lib).glob('**/*.yml'):

        if '.#' in str(path):
            continue

        if _args.verbose > 3:
            print(path)

        with open(path) as y_file:
            y_data = yaml.load(y_file, Loader=yaml.FullLoader)

        y_data['yml_file'] = path.name

        outpath = Path(_args.output, path.stem).with_suffix('.md')

        md_lib.append({'path': outpath, 'data': y_data})

        # ---------------------
        # Assemble the nav
        # ---------------------

        r_file = Path(outpath.name)

        node = resolve_tree_node(nav_tree, f"/Root/{y_data['node']}/{y_data['title']}")

        node.title = y_data['title']
        node.file = str(r_file)
        node.noLink = ('control' in y_data and 'no_link' in y_data['control'])
        node.noAutoLink = ('control' in y_data and 'no_autolink' in y_data['control'])
        if 'altLinks' in y_data:
            node.altLinks = y_data['altLinks']

        # Gather timeline information for a common timeline
        if ('History' in y_data) and ('Timeline' in y_data['History']):

            # Custom sort for timeline entries
            y_data['History']['Timeline'] = sorted(
                y_data['History']['Timeline'],
                key=age_decode)

            for event in y_data['History']['Timeline']:
                event.update({'Source': y_data['title']})
                timeline_struct.append(event)

    # -----------------------
    # Generate the Timeline
    # -----------------------

    timeline_template = _env.get_template('Timeline.md')
    timeline = Path('./docs', 'Timeline.md')

    node = resolve_tree_node(nav_tree, f"/Root/General/Timeline")
    node.title = 'Timeline'
    node.file = str(timeline.name)
    node.noLink = False
    node.noAutoLink = False

    timeline_sorted = sorted(timeline_struct, key=age_decode)

    if _args.verbose > 3:
        _pp(timeline_sorted)

    # ---------------------
    # Prepare AutoLinker
    # ---------------------

    linked_list = list()
    file_links = list()
    for node in PreOrderIter(nav_tree):
        if node.is_leaf and not node.noAutoLink:
            file_links.append({'title': node.title,
                               'file': node.file})
            linked_list.append({'text': node.title,
                                'link': node.title,
                                'file': node.file})
            if hasattr(node, 'altLinks'):
                for altLink in node.altLinks:
                    linked_list.append({'text': altLink,
                                        'link': node.title,
                                        'file': node.file})

    _global_links = sorted(linked_list, key=lambda k: len(k['text']), reverse=True)

    # ---------------------
    # Run link templater
    # ---------------------

    links = Path(_args.templates, 'links.md.j2')
    template = _env.get_template('links.j2')

    with open(links, 'w') as linkFile:
        linkFile.write(template.render(fileLinks=file_links))

    # ---------------------
    # Write Timeline
    # ---------------------

    with open(timeline, 'w') as timelineFile:
        timeline_render = timeline_template.render(timeline=timeline_sorted, date=date)
        timelineFile.write(timeline_render)

    # ---------------------
    # Run Templater
    # ---------------------
    for entry in md_lib:
        outpath = entry['path']

        y_data = entry['data']

        template = _env.get_template(y_data['template'])

        with open(outpath, 'w') as outfile:
            outfile.write(template.render(y_data, date=date))

    # ---------------------
    # Write the Cat Pages
    # ---------------------

    template = _env.get_template('Category.md')
    for category in nav_tree.children:
        # Make sure it really is a category
        if category.children:
            page = Path(outdir, category.name).with_suffix('.md')
            category.file = page.name
            with open(page, 'w') as pageFile:
                pageFile.write(template.render(navTree=category,
                                               date=date))

    # ---------------------
    # Write the config
    # ---------------------

    template = _env.get_template('mkdocs.yml.j2')
    config = Path('mkdocs.yml')
    with open(config, 'w') as configFile:
        configFile.write(template.render(navTree=nav_tree))

    # ---------------------
    # Write the Main Page
    # ---------------------

    SafeLoaderIgnoreUnknown.add_multi_constructor('', SafeLoaderIgnoreUnknown.default_ctor)

    with open('mkdocs.yml') as mkdocs_ctrl_file:
        mkdocs_ctrl = yaml.load(mkdocs_ctrl_file, Loader=SafeLoaderIgnoreUnknown)

    template = _env.get_template('index.md')
    index = Path(outdir, 'index.md')

    with open(index, 'w') as indexFile:
        indexFile.write(template.render(navTree=nav_tree,
                                        mkdocs_yaml=mkdocs_ctrl,
                                        date=date))

    libpath = Path('..', _args.lib)

    symlink(Path('../yaml-wiki/lib/stylesheets'), outdir.joinpath('stylesheets_lib'), target_is_directory=True)
    symlink(Path('../yaml-wiki/lib/js'), outdir.joinpath('js_lib'), target_is_directory=True)

    if _args.js:
        symlink(libpath.joinpath(_args.js), outdir.joinpath(_args.js), target_is_directory=True)

    if _args.stylesheets:
        symlink(libpath.joinpath(_args.stylesheets), outdir.joinpath(_args.stylesheets), target_is_directory=True)

    if _args.img:
        symlink(libpath.joinpath(_args.img), outdir.joinpath(_args.img), target_is_directory=True)


if __name__ == "__main__":
    main()
