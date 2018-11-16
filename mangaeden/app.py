# -*- coding: utf-8 -*-

""" Mangaeden App Module """

import os

import mangaeden.api as api
import mangaeden.utils as utils
import mangaeden.manga as manga


def download_image(img: tuple, name: str, path: str = '') -> None:
    f_name = name + "." + img[1].split('/')[1]  # name and file type concatenation
    f_path = path + f_name

    with open(f_path, 'wb') as file:
        file.write(img[0])  # writing image data to file


def download_chapter(m: manga.Manga, row_n: int, path: str = '') -> None:
    f_path = path + m.get_title()
    if not os.path.exists(f_path):  # creates manga folder if it doesn't exists
        os.makedirs(f_path)

    chapter_number = m.get_chapter_number(row_n)
    chapter_title = m.get_chapter_title(row_n)

    f_name = str(chapter_number) + ". " + chapter_title + "/"
    f_path = f_path + "/" + f_name
    if not os.path.exists(f_path):  # creates chapter folder if it doesn't exists
        os.makedirs(f_path)

    chapter = api.get_chapter(m.get_chapter_id(row_n))
    chapter_images = chapter.get_images()
    for n in range(len(chapter_images)):
        img = api.get_image(chapter.get_image_url(n))
        download_image(img, str(chapter.get_image_page(n)), f_path)


def search(req: str, result_n: int = 10) -> tuple:
    dataset = api.get_dataset(api.LANG['EN'])

    # sort dataset by manga alias
    sorted_dataset = sorted(dataset, key=lambda x: x['a'])

    req_pos = utils.binary_search(sorted_dataset, len(sorted_dataset), req)

    return tuple(sorted_dataset[req_pos:req_pos + result_n])
