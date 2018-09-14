# -*- coding: utf-8 -*-

""" Mangaeden Manga Module """

import typing

Chapter = typing.NewType('Chapter', dict)


def get_images(chapter: Chapter) -> list:
    """Gets chapter images."""
    return chapter['images']

def get_image_page(images: list, row_n: int) -> int:
    """Gets image page number."""
    return images[row_n][0]

def get_image_url(images: list, row_n: int) -> str:
    """Gets image url."""
    return images[row_n][1]

def get_image_resolution(images: list, row_n: int) -> list:
    """Gets image resolution."""
    return list([images[row_n][2], images[row_n][3]])
