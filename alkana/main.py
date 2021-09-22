# coding: utf-8
#
# Licence GPLv2
# (c) 2019 cod
from re import sub

from .data import data


def get_kana(word):
    # type: (str) -> str | None
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


def get_kana_for_sentence(sentence):
    # type: (str) -> str | None
    """
    Returns the reading of `word` as katakana.

    Parameters
    ----------
    sentence : str
        A sentence with mixed letters of the alphabet.
        The case of string is ignored.

    Returns
    ----------
    reading : str
        A sentence in which all alphabetic strings in `sentence` are replaced with its reading.
        `None` if reading is not found.
    """
    try:
        return sub(
            r'[a-z]+',
            lambda s: data[s.group(0)],
            str(sentence).lower())

    except KeyError:
        return None
