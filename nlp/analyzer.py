import spacy
import argparse
import sys
from spacy.lang.en import English
from spacy.matcher import Matcher

def find_ingredients(text):
    nlp = English()
    doc = nlp(text)
    for token in doc:
        if token.like_num:
            i = token.i
            next = doc[i + 1]
            if next.is_alpha:
                print(doc[i:i+5].text.strip())
    print(doc.text)

def read_from_args(args):
    for path in args.paths:
        txt = read_from_file(path)
        find_ingredients(txt)

def read_from_file(path):
    with open(path, mode="r") as file:
        output = ""
        return output.join(file.readlines())

def setup_args():
    parser = argparse.ArgumentParser(description="Analyze recipe text")
    parser.add_argument("paths", nargs="*", help="paths to text files to parse")
    return parser.parse_args()

def main():
    args = setup_args()
    if len(sys.argv) > 1:
        read_from_args(args)
    else:
        read_from_stdin(args)
    exit

if __name__ == "__main__":
    main()