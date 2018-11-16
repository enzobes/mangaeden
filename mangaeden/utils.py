# -*- coding: utf-8 -*-

""" Mangaeden Utils Module """

import math
from urllib.error import HTTPError
from requests import get, Timeout


def secure_get(url, params=None):
    """Performs a url content request and check for any errors"""
    try:
        response = get(url, timeout=10, params=params)
    except Timeout:
        # TODO Implement logging
        return None
    except HTTPError:
        # TODO Implement logging "ERROR {}: {}\n".format(e.code, e.reason)
        return None

    return response


def get_json(url, params=None):
    """Returns the json data of the requested url"""
    return secure_get(url, params).json()


def binary_search(dataset: list, dataset_len: int, target: str) -> int:
    left = 0
    right = dataset_len - 1

    while left <= right:
        middle = math.floor((left + right) / 2)
        if dataset[middle]['a'] < target:
            left = middle + 1
        elif dataset[middle]['a'] > target:
            right = middle - 1
        else:
            return middle

    return -1
