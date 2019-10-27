import requests
import argparse
import sys
import os
from bs4 import BeautifulSoup

def scrape_index(html):
    soup = BeautifulSoup(html, "html.parser")
    recipes = soup.find_all("div", { "class": "fixed-recipe-card__info"} )
    urls = []
    for recipe in recipes:
        anchor = recipe.find("a", { "class": "fixed-recipe-card__title-link" } )
        urls.append(anchor.get("href"))
    return urls

def scrape_html(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find_all("h1" , {"id": "recipe-main-content"})
    ingredients_html = soup.find_all("span", {"itemprop": "recipeIngredient"})
    ingredients_list = []
    for ingr in ingredients_html:
        str = ingr.string
        ingredients_list.append(str)

    ingredients = map(lambda ingredient: ingredient.string, ingredients_html)

    recipe = { "title": title.string,
                "ingredients": ingredients
    }

def read_html_from_file(path):
    with open(path, mode="r") as file:
        return file.readlines

def read_recursive(paths):
    for path in paths:
        if not os.path.exists(path):
            continue
        for (dirpath, dirnames, filenames) in os.walk(path):
            read_from_paths(filenames)
            read_recursive(dirnames)

def read_from_paths(paths):
    for path in paths:
        html = read_html_from_file(path)
        scrape_html(html)

def read_from_args(args):
    if args.recursive:
        read_recursive(args.paths)
        return
    read_from_paths(args.paths)

def read_from_stdin(args):
    print("Reading from stdin not yet implemented")
        
def setup_args():
    parser = argparse.ArgumentParser(description="Scrape recipe data from HTML strings")
    parser.add_argument("paths", nargs="+", help="paths to HTML files to scrape")
    parser.add_argument("--recursive", "-r", action="store_true", help="Paths are treated as paths to directories containing files to be scraped recursively")
    return parser.parse_args()

def main():
    args = setup_args()
    if len(sys.argv) > 1:
        read_from_args(args)
    else:
        read_from_stdin(args)
    
if __name__ == "__main__":
    main()