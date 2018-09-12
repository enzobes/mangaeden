# -*- coding: utf-8 -*-

""" Mangaeden Manga Module """

import typing

Manga = typing.NewType('Manga', dict)
STATUS = ['', 'Ongoing', 'Completed']


def get_description(manga: Manga) -> str:
    """Get manga description from from manga data"""
    return manga['description'].strip('\n')


def get_author(manga: Manga) -> str:
    """Gets manga author"""
    return manga['author']


def get_artist(manga: Manga) -> str:
    """Gets manga artist"""
    return manga['artist']


def get_number_of_chapters(manga: Manga) -> int:
    """Gets manga number of chapters"""
    return manga['chapters_len']


def get_release_year(manga: Manga) -> int:
    """Gets manga release year."""
    return manga['released']


def get_chapters(manga: Manga) -> dict:
    """Gets manga chapters list"""
    return manga['chapters']
