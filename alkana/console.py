# coding: utf-8
#
# Licence GPLv2
# (c) 2019 cod

import argparse

from .main import get_kana


def parse_args(test=None):
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        prog='alkana',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="A tool to get the katakana reading of an alphabetical string"
    )

    parser.add_argument('word', metavar='word', type=str,
                        help='The alphabetical string you want to get the katakana reading')
    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s {}'.format('0.0.1'))
    if test:
        return parser.parse_args(test)
    else:
        return parser.parse_args()


def console():
    # type: () -> None
    args = parse_args()
    result = get_kana(args.word)
    if result:
        print(result)
