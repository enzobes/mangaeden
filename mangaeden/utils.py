# -*- coding: utf-8 -*-

""" Mangaeden Utils Module """

from urllib.error import HTTPError
from requests import get, Timeout


def secure_get(url, params=None):
    """Performs a url content request and check for any errors"""
    try:
        response = get(url, timeout=10, params=params)
    except Timeout:
        # TODO Implement logging
        return None
    except HTTPError as e:
        # TODO Implement logging "ERROR {}: {}\n".format(e.code, e.reason)
        return None

    return response


def get_json(url, params=None):
    """Returns the json data of the requested url"""
    return secure_get(url, params).json()
