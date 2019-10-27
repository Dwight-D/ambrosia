import requests
import argparse
import sys
import os
import json
from bs4 import BeautifulSoup

def parse_index(html):
    """Parse an index page containing multiple links to other recipe pages
    
    Arguments:
        html {string} -- The HTML of the index page to scrape
    
    Returns:
        urls[{string}] -- A list of recipe URLs found on the page
    """
    soup = BeautifulSoup(html, "html.parser")
    recipes = soup.find_all("div", { "class": "fixed-recipe-card__info"} )
    urls = []
    for recipe in recipes:
        anchor = recipe.find("a", { "class": "fixed-recipe-card__title-link" } )
        urls.append(anchor.get("href"))
    return urls

def parse_ingredients(soup):
    ingredients_html = soup.find_all("span", {"itemprop": "recipeIngredient"})
    return list(map(lambda ingredient: ingredient.string, ingredients_html))

def parse_directions(soup):
    directions = soup.find("div", { "class": "directions--section" } )
    time = directions.find_all("li", { "class": "prepTime__item" } )
    time_list = list(filter(lambda item: item, map(lambda item: item.get("aria-label"), time)))

    steps = list(filter(lambda string: string, map(lambda step: step.get_text().strip(), directions.find_all("li", { "class": "step" } ))))
    return time_list, steps

def parse_recipe(recipe):
    title = recipe.find("h1" , {"id": "recipe-main-content"}).string
    ingredients = parse_ingredients(recipe)
    time, directions = parse_directions(recipe)

    recipe = { "title": title,
                "ingredients": ingredients,
                "time": time,
                "directions": directions
    }
    print(json.dumps(recipe))
    
def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    recipe = soup.find("div" , {"class": "recipe-container-outer"})
    if not recipe:
        return
    parse_recipe(soup)

def read_html_from_file(path):
    with open(path, mode="r") as file:
        output = ""
        return output.join(file.readlines())

def read_recursive(paths):
    for path in paths:
        if not os.path.exists(path):
            continue
        for (dirpath, dirnames, filenames) in os.walk(path):
            filenames = map(lambda path: dirpath + "/" + path, filenames)
            dirnames = map(lambda path: dirpath + "/" + path, dirnames)
            read_from_paths(filenames)
            read_recursive(dirnames)

def read_from_paths(paths):
    for path in paths:
        html = read_html_from_file(path)
        parse_html(html)

def read_from_args(args):
    if args.recursive:
        read_recursive(args.paths)
        return
    read_from_paths(args.paths)

def read_from_stdin(args):
    print("Reading from stdin not yet implemented")
        
def setup_args():
    parser = argparse.ArgumentParser(description="parse recipe data from HTML strings")
    parser.add_argument("paths", nargs="+", help="paths to HTML files to parse")
    parser.add_argument("--recursive", "-r", action="store_true", help="Paths are treated as paths to directories containing files to be parsed recursively")
    return parser.parse_args()

def main():
    args = setup_args()
    if len(sys.argv) > 1:
        read_from_args(args)
    else:
        read_from_stdin(args)
    
if __name__ == "__main__":
    main()