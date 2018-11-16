# -*- coding: utf-8 -*-

import argparse

__author__ = "Manoah Bernier"
__email__ = "contact@mhbernier.com"
__version__ = "1.0"


def init_parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(
        prog='mangaeden',
        usage="\n\n  %(prog)s <command> [options]",
        description='An API wrapper for https://mangaeden.com'
    )


def set_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        'search',
        type=str,
        help='search for mangas'
    )
    parser.add_argument(
        'download',
        type=str,
        help='download mangas'
    )
    parser.add_argument(
        'remove',
        type=str,
        help='remove downloaded mangas'
    )
    parser.add_argument(
        'list',
        help='list downloaded mangas'
    )
    parser.add_argument(
        'show',
        type=str,
        help='show information about mangas')
    parser.add_argument(
        '-v', '--verbose',
        help='give more detailled output',
        action='store_true'
    )
    parser.add_argument(
        '-V', '--version',
        help='show program version and exit',
        action='version',
        version='%(prog)s {}'.format(__version__)
    )
