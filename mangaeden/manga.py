# -*- coding: utf-8 -*-

""" Mangaeden Manga Module """

STATUS = ['', 'Ongoing', 'Completed']


class Manga(object):
    def __init__(self, data=None):
        self.data = data

    def get_alias(self) -> str:
        """Gets the alias."""
        return self.data['alias']

    def get_artist(self) -> str:
        """Gets the artist."""
        return self.data['artist']

    def get_author(self) -> str:
        """Gets the author."""
        return self.data['author']

    def get_categories(self) -> list:
        """Gets categories list."""
        return self.data['categories']

    def get_chapters(self) -> list:
        """Gets chapters list."""
        return self.data['chapters']

    def get_chapter_number(self, row_n: int) -> int:
        """Gets the chapter number at row_n."""
        return self.data['chapters'][row_n][0]

    def get_chapter_date(self, row_n: int) -> float:
        """Gets the chapter unix timestamp code at row_n."""
        return self.data['chapters'][row_n][1]

    def get_chapter_title(self, row_n: int) -> str:
        """Gets the chapter title at row_n."""
        return self.data['chapters'][row_n][2]

    def get_chapter_id(self, row_n: int) -> str:
        """Gets the chapter id at row_n."""
        return self.data['chapters'][row_n][3]

    def get_creation_date(self) -> float:
        """Gets creation unix timestamp code."""
        return self.data['created']

    def get_number_of_chapters(self) -> int:
        """Gets the number of chapters."""
        return self.data['chapters_len']

    def get_description(self) -> str:
        """Gets description."""
        return self.data['description'].strip('\n')

    def get_number_of_views(self) -> int:
        """Gets the number of views."""
        return self.data['hits']
    
    def get_cover(self) -> str:
        """Gets cover image url."""
        return self.data['image']
    
    def get_language(self) -> int:
        """Gets language code."""
        return self.data['language']
    
    def get_last_chapter_date(self) -> float:
        """Gets last chapter unix timestamp code."""
        return self.data['last_chapter_date']
    
    def get_release_year(self) -> int:
        """Gets release year."""
        return self.data['released']
    
    def get_status(self) -> int:
        """Gets status code."""
        return self.data['status']
    
    def get_title(self) -> str:
        """Gets title."""
        return self.data['title']
