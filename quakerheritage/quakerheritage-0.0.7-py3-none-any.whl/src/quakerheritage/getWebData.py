# quakerheritage/getWebData.py

"""Main web function that collects url data and extracts text from each pdf examined.

This module allows the user to extract core data from formatted pdfs on the Britain Yearly Meeting website.

This module contains the following functions:

- `getUrls(url)` - Filters the Quaker Heritage Project's website for the url links to pdfs.
- `pdfDataExtract(url)` - Extracts core data text from a single pdf passed in as a url link.
"""

import io
import urllib3
import re

from bs4 import BeautifulSoup, SoupStrainer
import pdfplumber
import requests



def getUrls(url: str) -> list:
    """Short function to isolate links from the chosen web page. As the webpage is pre-selected, they are all known to be pdf files.

    Args:
        url (string): the pre-selected web address.

    Return:
        pdfList(array): a Python list containing all the links extracted from the page. 
    """
    pdfList = []
    response = requests.get(url)
    for link in BeautifulSoup(response.text, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr('href') and link['href'][0] != "#":
            pdfList.append(url + link['href'])
    return pdfList

def pdfDataExtract(url: str) -> dict:
    """Extracts text data from pdfs and passes it into a dictionary

    Args:
        url (string): a single url which must be a pdf file storage location.

    Return:
        itemDict (array): Python dictionary containing keys and values extracted from text.
    """
    itemDict = {}

    http = urllib3.PoolManager()
    temp = io.BytesIO()
    temp.write(http.request("GET", url).data)
    try:    
        pdf = pdfplumber.open(temp)
        all_text = ''
        itemDict["Meeting Name"] = url.split('/')[-1].split('.')[0].replace("%20", " ")
        header_list= pdf.pages[0].extract_text().splitlines()[0:5]
        header_data = [x.strip() for x in header_list if x.strip()]
        itemDict["Meeting Full Name"] = header_data[0]
        itemDict["Meeting House Address"] = header_data[1]
        itemDict[header_data[2].split(': ')[0]] = header_data[2].split(': ')[1]

        for pdf_page in pdf.pages:
            single_page_text = pdf_page.extract_text()
            if single_page_text is not None:
                all_text += '\n' + single_page_text
        startLoc = all_text.find('1.1')
        endLoc = all_text.find('1.19')
        trimText = all_text[startLoc:endLoc]
        splitText = re.split(r"[1]\.[0-9]+", trimText)
        for item in splitText[1:]:
            splitItem = item.strip().split(': ')
            itemDict[splitItem[0]] = splitItem[1].strip()
    except:
        pass
    return itemDict
