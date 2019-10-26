import requests
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
    soup = BeautifulSoup(response, "html.parser")
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

def main():
    print("No main method yet")
    
if __name__ == "__main__":
    main()