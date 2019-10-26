import re
import os
import sys

def download_html(url, dataset):
    response = requests.get(url)  
    path = get_path_and_create_dir(url, dataset)
    with open(path, 'w+', encoding="utf-8") as file:
        for line in response.text:
            file.write(line)
    return response.text

def get_path_and_create_dir(url, dataset):
    name = re.sub(r'^.*\/([^/]*)-.*', r'\1', url)
    path = data_dir + "/" + dataset + "/" + name + ".txt"
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

def main():
    url = 'https://www.allrecipes.com/recipe/214500/sausage-peppers-onions-and-potato-bake/'
    if len(sys.argv) > 0:
        urls = sys.argv
    
    dataset = "allrecipes"
    text = load_html(url, dataset)
    scrape_html(text)
    print(soup)
    

if __name__ == "__main__":
    main()