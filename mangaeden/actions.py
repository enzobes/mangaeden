# -*- coding: utf-8 -*-

import argparse
import mangaeden.app as app


class SearchAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None) -> None:
        setattr(namespace, self.dest, values)
        results = app.search(values)
        print(results)
