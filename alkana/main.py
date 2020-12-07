# coding: utf-8
#
# Licence GPLv2
# (c) 2019 cod
from .data import data


def get_kana(word):
    """
    Returns the reading of `word` as katakana.

    Parameters
    ----------
    word : str
        The alphabetical string you want to get the katakana reading.
        The case of string is ignored.

    Returns
    ----------
    reading : str
        The reading of `word`.
        `None` if reading is not found.
    """
    try:
        return data[word.lower()]
    except KeyError:
        return None
