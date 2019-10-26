import re
import os
import sys
import requests
data_dir = "../data"

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
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path
    
def read_from_stdin(dataset):
    for line in sys.stdin:
        print(line)
    
def read_from_args(dataset):
    for url in sys.argv[1:]:
        print(download_html(url, dataset))

def main():
    dataset = "allrecipes"
    if len(sys.argv) > 1:
        read_from_args(dataset)
    else:
        read_from_stdin(dataset)

if __name__ == "__main__":
    main()