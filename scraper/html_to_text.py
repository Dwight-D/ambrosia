from bs4 import BeautifulSoup
import argparse
import sys

def setup_args():
    parser = argparse.ArgumentParser(description="Extract text from HTML")
    parser.add_argument("paths", nargs="*", help="paths to HTML files to parse")
    return parser.parse_args()

def read_from_args(args):
    for path in args.paths:
        txt = read_from_file(path)
        print(html_to_text(txt))

def read_from_file(path):
    with open(path, mode="r") as file:
        output = ""
        return output.join(file.readlines())

def html_to_text(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

def read_from_stdin(args):
    html = "".join(sys.stdin.readlines())
    print(html_to_text(html))

def main():
    args = setup_args()
    if len(sys.argv) > 1:
        read_from_args(args)
    else:
        read_from_stdin(args)

if __name__ == "__main__":
    main()