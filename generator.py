#!/usr/bin/env python3
import hashlib
import os
import MeCab
import argparse
import markovify


def build_model(src: str, state_size: int = 3, should_export: bool = True,
                export_path: str = 'cache/') -> str:
    with open(src) as f:
        src_text = f.read()
        f.close()
    # TODO: if hash(text) exists

    text = src_text \
        .replace("?", "？") \
        .replace("!", "！") \
        .replace("，", "、") \
        .replace("．", "。") \
        .replace("。", "。\n")

    data = [MeCab.Tagger("-Owakati").parse(s) for s in text.split("\n") if s != ""]
    joined_data = "".join(data)
    model_json = markovify.NewlineText(joined_data, state_size=state_size).to_json()

    if should_export:
        filename = str(hashlib.sha256(src_text.encode()).hexdigest()) + '.json'
        os.makedirs(export_path, exist_ok=True)
        with open(os.path.join(export_path, filename), mode="w") as f:
            f.write(model_json)
            f.close()

    return model_json


def generate_from(model_json: str, count: int = 5) -> list:
    sentences = []
    for i in range(count):
        sentence = None
        while sentence is None:
            sentence = markovify.Text.from_json(model_json).make_sentence(tries=100)
        sentences.append("".join(sentence.split()))
    return sentences


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("src", type=str, help="source file")
    parser.add_argument("--cache", action="store_true", help="cache model")
    parser.add_argument("-c", "--count", type=int, help="number of statements to generate")
    args = parser.parse_args()

    model_json = build_model(args.src, should_export=args.cache)
    if args.count:
        sentences = generate_from(model_json, args.count)
    else:
        sentences = generate_from(model_json)

    for s in sentences:
        print(s)
