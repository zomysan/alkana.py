# Licence GPL
#
# (c) 2019 cod
# coding: utf-8


import setuptools
import pathlib


description = 'A tool to get the katakana reading of an alphabetical string.'
readme_file = pathlib.Path(__file__).parent/'README.md'
with readme_file.open(encoding='utf-8') as f:
    readme = f.read()

setuptools.setup(
    name='alkana',
    version='0.0.3',
    url='https://github.com/cod-sushi/alkana.py',
    author='cod',
    author_email='cod.sushi@gmail.com',
    license='GPLv2',
    python_requires='>=3.0, <4.0',
    description=description,
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: Japanese',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',  # noqa
    ],
    entry_points={
        'console_scripts': [
            'alkana = alkana.console:console',
        ],
    },
)
