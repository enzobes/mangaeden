#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import mangaeden

__maintainer__ = "Manoah Bernier"
__maintainer_email__ = "contact@mhbernier.com"

setup(
    name='mangaeden',
    description='An API wrapper for https://mangaeden.com.',
    version=mangaeden.__version__,
    license='GPLv3',
    author='Manoah Bernier',
    author_email='contact@mhbernier.com',
    maintainer=__maintainer__,
    maintainer_email=__maintainer_email__,
    url='https://github.com/mhbernier/mangaeden',
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Database :: Front-Ends',
        'Topic :: Multimedia',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
