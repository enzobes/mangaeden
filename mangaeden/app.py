# -*- coding: utf-8 -*-

""" Mangaeden App Module """


def download_image(img: tuple, name: str, path: str=''):
    f_name = name + "." + img[1].split('/')[1] # name and file type concatenation
    f_path = f_name + path

    with open(f_path, 'wb') as file:
        file.write(img[0]) # writing image data to file
