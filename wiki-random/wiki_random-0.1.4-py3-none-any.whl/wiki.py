import requests
from bs4 import BeautifulSoup

def get_wiki_random():
    """
    - Get random article from Wikipedia. 

    Returns:
        title and url
    """
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text

    url = "https://en.wikipedia.org/wiki/%s" % title

    return title,url
    