# -*- coding: utf-8 -*-
import os

"""
    Sphinx Meetup Theme
    ~~~~~~~~~~~~~~~~~~~~~
    Sphinx Theme for generic meetup website
    :copyright: -
    :license: MIT, see LICENSE for more details.
"""

__version__ = '0.0.1'
__license__ = 'MIT'


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return [cur_dir]
