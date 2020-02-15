import requests
from bs4 import BeautifulSoup

BLACKLIST = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
    'button',
    'svg',
    'nav',
    'form',
    'style',
    'figure',
    'div',
]

def download(url):
    html = requests.get(url).content
    return html

def scrape_text(url):
    """Get the page text content from a url
    
    Arguments:
        url {str} -- A link to the page you want to extract text from
    
    Returns:
        text {str[]} -- The text content as a list of strings 
    """
    html = download(url)
    text = get_text(html)
    return text

def get_text(html):
    """Extracts raw text content from HTML
    
    Arguments:
        html {str} -- HTML content scraped from web site

    Returns:
        text [str] -- The text content of the html
    """
    soup = BeautifulSoup(html, "html.parser")
    text = soup.find_all(text=True)
    output = [t for t in text if t.parent.name not in BLACKLIST]
    return " ".join(output)