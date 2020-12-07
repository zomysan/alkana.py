# alkana
[![PyPI version](https://badge.fury.io/py/alkana.py.svg)](https://badge.fury.io/py/alkana)

アルファベット文字列から、読み仮名をカタカナで取得できるツールです。

# インストール
Python3、またはより新しいバージョンが必要です。

## pipでインストール 
```
python3 -m pip install -U alkana
```

## GitHubからclone
```
$ git clone https://github.com/cod-sushi/alkana.py
$ cd alkana.py
$ python3 -m pip install -U .
```

# 例
## Python importで使う
```python
import alkana

print(alkana.get_kana("Hello"))
print(alkana.get_kana("World"))
print(alkana.get_kana("abcdefg"))
```
実行すると、以下のように出力されます。
```
ハロー
ワールド
None
```
指定された単語が辞書に存在しない場合、`None`を返します。

## コマンドラインで使う
```shell
$ alkana hello
ハロー
$ alkana world
ワールド
$ alkana abcdefg
```
指定された単語が辞書に存在しない場合、なにも出力されません。

## External file

辞書は拡張する事ができます。

`sample.csv`を作成します。
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
アルファベット文字列とカタカナを変換する辞書は、Bilingual Emacspeak Projectの`bep-eng.dic`のデータを利用しています。

[Bilingual Emacspeak Project](http://www.argv.org/bep/)
(c) 1999-2002 Bilingual Emacspeak Project

# Lisence
GPLv2
