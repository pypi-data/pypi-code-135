import requests
from bs4 import BeautifulSoup
import random

def get_wiki_random():
    """
    - Get random article from Wikipedia. 

    Returns:
        title and url
    """
    
    ran = random.randrange(0,100)
    
    if ran == 1:
        title = "Rick Roll"
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    else:

        url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        soup = BeautifulSoup(url.content, "html.parser")
        title = soup.find(class_="firstHeading").text
        url = "https://en.wikipedia.org/wiki/%s" % title
    
    return title,url
    