import re
import os
import sys
import requests
import argparse
import recipe_scraper

data_dir = "data"

def download_html(url, dataset):
    response = requests.get(url)  
    path = get_path_and_create_dir(url, dataset)
    with open(path, 'w+', encoding="utf-8") as file:
        for line in response.text:
            file.write(line)
    return path

def get_path_and_create_dir(url, dataset):
    name = re.sub(r'^.*\/([^/]*)-.*', r'\1', url)
    path = data_dir + "/" + dataset + "/" + name + ".txt"
    make_directory(path)
    return path

def make_directory(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
def read_from_stdin(args):
    for url in sys.stdin:
        url = url.strip()
        print(download_html(url, args.dataset))
    
def read_from_args(args):
    if args.recursive:
        read_recursive(args)
        return
    for url in args.url:
        print(download_html(url, args.dataset))

def read_recursive(args):
    index_url = args.url
    dataset = args.dataset
    recipe_urls = get_recipe_urls_from_index(index_url)
    save_urls(recipe_urls, dataset)

def get_recipe_urls_from_index(url):
    response = requests.get(url)
    return recipe_scraper.scrape_index(response.text)

def save_urls(urls, dataset):
    path = data_dir + "/" + dataset + "/" + "recipes.url"
    make_directory(path)
    with open(path, 'w+', encoding="utf-8") as file:
        for line in urls:
            file.write(line + '\n')

def setup_args():
    parser = argparse.ArgumentParser(description="Download recipe HTML from a given url")
    parser.add_argument("url", nargs="*", help="url to download")
    parser.add_argument("--recursive", "-r", action="store_true", help="The given url is interpreted as an index of multiple URL:s to download recursively")
    parser.add_argument("--dataset", "-s", action="store", default="allrecipes")
    parser.add_argument("--datadir", "-d", action="store", default="data")
    return parser.parse_args()

def main():
    args = setup_args()
    global data_dir
    data_dir = args.datadir

    if len(args.url) >= 1:
        read_from_args(args)
    else:
        read_from_stdin(args)

if __name__ == "__main__":
    main()