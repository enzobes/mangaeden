# -*- coding: utf-8 -*-

""" Mangaeden App Module """

import mangaeden.api as api
import mangaeden.utils as utils


def download_image(img: tuple, name: str, path: str='') -> None:
    f_name = name + "." + img[1].split('/')[1] # name and file type concatenation
    f_path = f_name + path

    with open(f_path, 'wb') as file:
        file.write(img[0]) # writing image data to file

def search(req: str, result_n: int = 10) -> tuple:
    dataset = api.get_dataset(api.LANG['EN'])
    
    # sort dataset by manga alias
    sorted_dataset = sorted(dataset, key = lambda x: x['a'])

    req_pos = utils.binary_search(sorted_dataset, len(sorted_dataset), req)

    return tuple(sorted_dataset[req_pos:req_pos+result_n])
