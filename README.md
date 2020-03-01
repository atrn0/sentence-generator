# Sentence Generator
入力の文章に基づいて文を生成します。

## Usage
install requirements
```shell script
pip install -r requirements.txt
```

Basic usage
```shell script
$ python generator.py example/akutagawa.txt
# しかし電話はいつになつてゐた。
# お持ちなさいと云ふ事であつた。
# 保吉は思はず煙草から女の顔の赤くなる容子を想像した。
# 俊吉はすべてに無頓着なのか、ぱつたり姿を隠してしまつた。
# が、彼女の声も、彼女自身に照子の事を話し合つた。
```

キャッシュを有効にする
```shell script
$ python generator.py example/akutagawa.txt --cache
# ...
```

生成する文の数を指定
```shell script
$ python generator.py example/akutagawa.txt -c 3
# 彼は叔父おじさんの家へ帰るようになった大学生のことが書いてあるんだよ。
# 二三時間の後、揺り上げた赤子へ目を移した。
# 「読みつづける気にはならないものだった。
```

help
```shell script
$ python generator.py -h
```
