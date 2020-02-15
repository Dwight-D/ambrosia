from ambrosia import scraper
from ambrosia.nlp import preproc

def handle(url):
    text = scraper.scrape_text(url)
    text = preproc.clean(text)
    with open('experiment.txt', mode='w') as file:
        file.write(text)
    print('lol')

url = 'https://www.allrecipes.com/recipe/223042/chicken-parmesan/?internalSource=streams&referringId=201&referringContentType=Recipe%20Hub&clickId=st_recipes_mades'
handle(url)