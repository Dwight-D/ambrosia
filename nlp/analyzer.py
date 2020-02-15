import spacy
import argparse
import sys
import preproc
from spacy.lang.en import English
from spacy.matcher import Matcher
from spacy.cli.download import download as spacy_download

NLP = None
MODEL = "en_core_web_sm"

def setup_nlp(text):
    text = preproc.clean(text)
    nlp = spacy.load(MODEL)
    return nlp(text)

def find_ingredients(text):
    doc = setup_nlp(text)
    for token in doc:
        if token.pos_ == 'NOUN':
            print(token)
        
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

def read_from_stdin(args):
    print("Reading from stdin not yet implemented")
    exit

def setup_model():
    global NLP
    global MODEL
    try:
        NLP = spacy.load(MODEL)
    except OSError:
        print(f"Spacy models '{MODEL}' not found.  Downloading and installing.")
        spacy_download(MODEL)
        NLP = spacy.load(MODEL)

def main():
    setup_model()
    args = setup_args()
    if len(sys.argv) > 1:
        read_from_args(args)
    else:
        read_from_stdin(args)
    exit

if __name__ == "__main__":
    main()