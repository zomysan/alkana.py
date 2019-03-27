# coding: utf-8
#
# Licence GPLv2
# (c) 2019 cod


def console():
    import sys
    from .main import get_kana

    if len(sys.argv) != 2:
        print('usage: alkana <word>')
        sys.exit()
    result = get_kana(sys.argv[1])
    if result:
        print(result)
