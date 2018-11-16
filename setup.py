#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import mangaeden

__maintainer__ = "Manoah Bernier"
__maintainer_email__ = "contact@mhbernier.com"


setup(
    name='mangaeden',
    description='An API wrapper for https://mangaeden.com.',
    version='1.0a0',
    license='MIT',
    author='Manoah Bernier',
    author_email='contact@mhbernier.com',
    maintainer = __maintainer__,
    maintainer_email=__maintainer_email__,
    url='https://github.com/mhbernier/mangaeden',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Database :: Front-Ends',
        'Topic :: Multimedia',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)