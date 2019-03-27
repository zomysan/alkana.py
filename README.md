# alkana.py
A tool to get the katakana reading of an alphabetical string.

# Installing
Python 3 or higher is required.

## From pip
```
python3 -m pip install -U alkana.py
```

## Clone from GitHub
```
$ git clone https://github.com/cod-sushi/alkana.py
$ cd alkana.py
$ python3 -m pip install -U .
```

# Example
## Python import
Quick example:
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

# Copyrights
Alphabetical word - katakana dictionary's data is from `bep-eng.dic`.

[Bilingual Emacspeak Project](http://www.argv.org/bep/)
(c) 1999-2002 Bilingual Emacspeak Project

# Lisence
GPLv2
