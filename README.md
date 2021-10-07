# alkana
[![PyPI version](https://badge.fury.io/py/alkana.svg)](https://badge.fury.io/py/alkana)

A tool to get the katakana reading of an alphabetical string.

# Installing
Python 3 or higher is required.

## From pip
```
python3 -m pip install -U alkana
```

## Clone from GitHub
```
$ git clone https://github.com/cod-sushi/alkana.py
$ cd alkana.py
$ python3 -m pip install -U .
```

# Example
## Python import
```python
import alkana

print(alkana.get_kana("Hello"))
print(alkana.get_kana("World"))
print(alkana.get_kana("abcdefg"))
```
Output of above example is:
```
ハロー
ワールド
None
```
If the reading is not exist, Returns `None`.

## Command line
```shell
$ alkana hello
ハロー
$ alkana world
ワールド
$ alkana abcdefg
```
If the reading is not exist, there is no output.

## External file

Alkana can extend the dictionary.

`sample.csv`
```
hogehoge,ホゲホゲ
piyopiyo,ピヨピヨ
...
```

```python
import alkana
alkana.add_external_data('./sample.csv')

print(alkana.get_kana('hogehoge'))  # ホゲホゲ
```

# Copyrights
Alphabetical word - katakana dictionary's data is from `bep-eng.dic`.

[Bilingual Emacspeak Project](http://www.argv.org/bep/)
(c) 1999-2002 Bilingual Emacspeak Project

# Lisence
GPLv2
