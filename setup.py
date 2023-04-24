# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the GNU General Public License version 3.
import setuptools
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='resp',
    version='0.0.0',
    packages=setuptools.find_packages(
        where=".",
        exclude=("examples"),
    ),
    project_urls={
        "Gitter": "https://github.com/monk1337/resp",
    },

    install_requires=[
    ],
)