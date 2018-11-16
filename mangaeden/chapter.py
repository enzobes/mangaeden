# -*- coding: utf-8 -*-

""" Mangaeden Manga Module """


class Chapter(object):
    def __init__(self, data=None):
        self.data = data

    def get_images(self) -> list:
        """Gets chapter images."""
        return self.data['images']

    def get_image_page(self, row_n: int) -> int:
        """Gets image page number."""
        return self.data['images'][row_n][0]

    def get_image_url(self, row_n: int) -> str:
        """Gets image url."""
        return self.data['images'][row_n][1]

    def get_image_resolution(self, row_n: int) -> tuple:
        """Gets image resolution."""
        return tuple([
            self.data['images'][row_n][2],
            self.data['images'][row_n][3]
        ])
