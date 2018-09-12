# -*- coding: utf-8 -*-

""" Mangaeden API Module """

from mangaeden.utils import get_json

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

    return get_json(url, params)
