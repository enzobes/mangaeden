# -*- coding: utf-8 -*-

""" Mangaeden API Module """

import mangaeden.manga as manga
import mangaeden.chapter as chapter
import mangaeden.utils as utils

MANGA_LIST = 'https://www.mangaeden.com/api/list/{}/'
MANGA = 'https://www.mangaeden.com/api/manga/{}/'
CHAPTER = 'https://www.mangaeden.com/api/chapter/{}/'
IMAGE = 'https://cdn.mangaeden.com/mangasimg/{}'


def get_dataset(lang: int=0, page_n: int=None, n_mangas_per_page: int=None) -> dict:
    """
    Make a call to the API to get all mangas from the database.
    Where lang can be 0 (English) or 1 (Italian)
    """
    params = dict()
    url = MANGA_LIST.format(str(lang), page_n)

    if page_n:
        params['p'] = page_n
    if n_mangas_per_page:
        params['l'] = n_mangas_per_page

    return utils.get_json(url, params)

def get_manga(_id: str) -> manga.Manga:
    """Returns a manga data row."""
    return utils.get_json(MANGA.format(_id))

def get_chapter(_id: str) -> chapter.Chapter:
    """Returns a chapter data row."""
    return utils.get_json(CHAPTER.format(_id))

def get_image(url: str) -> tuple:
    """Returns an image data."""
    req = utils.secure_get(IMAGE.format(url))
    return tuple([req.content, req.headers.get('content-type')])

def download_image(img: tuple, name: str, path: str=''):
    f_name = name + "." + img[1].split('/')[1] # name and file type concatenation
    f_path = f_name + path

    with open(f_path, 'wb') as file:
        file.write(img[0]) # writing image data to file
