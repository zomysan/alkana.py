# coding: utf-8
#
# Licence GPLv2
# (c) 2019 cod
from .data import data


def add_external_data(file_path):
    external_data = {}
    with open(file_path, 'r') as f:
        for x in f:
            x = x.strip().split(',')
            external_data[x[0].lower()] = x[1]
    data.update(external_data)
