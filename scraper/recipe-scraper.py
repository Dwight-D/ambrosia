import requests
from bs4 import BeautifulSoup

data_dir = "data"




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
    url = 'https://www.allrecipes.com/recipe/214500/sausage-peppers-onions-and-potato-bake/'
    dataset = "allrecipes"
    text = load_html(url, dataset)
    scrape_html(text)
    print(soup)
    

if __name__ == "__main__":
    main()