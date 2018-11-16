# -*- coding: utf-8 -*-

import argparse
import mangaeden.actions as actions


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
    subparsers = parser.add_subparsers(metavar="")

    search = subparsers.add_parser(
        'search',
        help='search mangas'
    )
    search.add_argument(
        'manga',
        type=str,
        action=actions.SearchAction
    )

    download = subparsers.add_parser(
        'download',
        help='download mangas'
    )
    download.add_argument(
        'manga',
        type=str,
        nargs='*'
    )

    remove = subparsers.add_parser(
        'remove',
        help='remove downloaded mangas'
    )
    remove.add_argument(
        'manga',
        type=str,
        nargs='*'
    )

    list = subparsers.add_parser(
        'list',
        help='list downloaded mangas'
    )

    show = subparsers.add_parser(
        'show',
        help='show information about mangas'
    )
    show.add_argument(
        'manga',
        type=str
    )

    # optional arguments
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
