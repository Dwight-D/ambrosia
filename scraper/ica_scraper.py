import requests
from bs4 import BeautifulSoup

START_TOKEN = "___START___"
PAGE_SIZE = 16
url_template = ("https://www.ica.se/templates/ajaxresponse.aspx?id=12&ajaxFunction=RecipeListMdsa&mdsarowentityid=00c54a06-037f-413c-9b0a-a42700eb59ff&sortbymetadata=Relevance&start="
 + START_TOKEN + "&num= " + str(PAGE_SIZE) +"&filter=M%c3%a5ltid:Middag")

def build_url(index):
    return url_template.replace(START_TOKEN, str(index * PAGE_SIZE))

def main():
    for i in range(100):
        url = build_url(i)
        try:
            html = requests.get(url).text
            soup = BeautifulSoup(html, "html.parser")
            links = soup.find_all("a", { "class": "js-track-listing-recipe" } )
            url_list = list(map(lambda anchor: anchor.get("href"), links))
            urls = set()
            for url in url_list:
                urls.add(url)
            for url in urls:
                print(url)
        except:
            continue

if __name__ == "__main__":
    main()