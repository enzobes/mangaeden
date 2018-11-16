# -*- coding: utf-8 -*-

""" Mangaeden API Module """

import mangaeden.manga as manga
import mangaeden.chapter as chapter
import mangaeden.utils as utils

LANG = {"EN": 0, "IT": 1}
MANGA_LIST = 'https://www.mangaeden.com/api/list/{}/'
MANGA = 'https://www.mangaeden.com/api/manga/{}/'
CHAPTER = 'https://www.mangaeden.com/api/chapter/{}/'
IMAGE = 'https://cdn.mangaeden.com/mangasimg/{}'


def get_dataset(lang: int) -> list:
    params = dict()
    url = MANGA_LIST.format(str(lang))
    return utils.get_json(url, params)['manga']


def get_manga(_id: str) -> manga.Manga:
    """Returns a manga data row."""
    return manga.Manga(utils.get_json(MANGA.format(_id)))


def get_chapter(_id: str) -> chapter.Chapter:
    """Returns a chapter data row."""
    return chapter.Chapter(utils.get_json(CHAPTER.format(_id)))


def get_image(url: str) -> tuple:
    """Returns an image data."""
    req = utils.secure_get(IMAGE.format(url))
    return tuple([req.content, req.headers.get('content-type')])
