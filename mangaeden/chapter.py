# -*- coding: utf-8 -*-

""" Mangaeden Manga Module """

import typing

Chapter = typing.NewType('Chapter', dict)


def get_images(chapter: Chapter) -> list:
    """Gets chapter images."""
    return chapter['images']

def get_image_page(chapter: Chapter, row_n: int) -> int:
    """Gets image page number."""
    return chapter['images'][row_n][0]

def get_image_url(chapter: Chapter, row_n: int) -> str:
    """Gets image url."""
    return chapter['images'][row_n][1]

def get_image_resolution(chapter: Chapter, row_n: int) -> list:
    """Gets image resolution."""
    return list(
        [
            chapter['images'][row_n][2],
            chapter['images'][row_n][3]
        ]
    )
