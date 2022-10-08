from typing import Any, List, Dict, Union
import requests
from bs4 import BeautifulSoup, ResultSet


class WordInfo:
    def __init__(self) -> None:
        return None

    def get_synonym(self, word: str) -> List[str]:
        """
        Returns a list of synonyms for a given word
        """
        response = requests.get('https://www.thesaurus.com/browse/{}'.format(word))
        soup = BeautifulSoup(response.text, 'html.parser')
        div =  soup.find('div', {'class': 'css-ixatld e15rdun50'})
        if not div:
            return "No Synonym for this word in this API"
        lis = div.find_all('li')
        if not lis:
            return "No Synonym for this word in this API"
        return [li.text.strip() for li in lis]

    def get_antonym(self, word: str) -> List[str]:
        """
        Returns a list of antonyms of a given word
        """
        response = requests.get('https://www.thesaurus.com/browse/{}'.format(word))
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', {'id': 'antonyms'})
        if not div:
            return "No Antonym for this word in this API"
        lis = div.find_all('li')
        if not lis:
            return "No Antonym for this word in this API"
        return [li.text.strip() for li in lis]

    def split_words_and_examples(self, sentencelist: List[str]) -> List[Dict[str, Any]]:
        """
        The defintions and examples are returned together as a string in a list. 
        This function splits those strings into definition as a key - "meaning", and example as the value - "examples", in a dictionary
        Returns a list of dictionaries such as {"meaning": "one defintion of a word", "examples": None}
        """
        result = []
        for word in sentencelist:
            if len(word.split(":")) > 1:
                result.append({"meaning": word.split(":")[0], "examples":word.split(":")[1]})
            else: 
                if "!" in word:
                    pass
                else:
                    result.append({"meaning": word, "examples": None})
        return result
        
    def meanings(self, section: ResultSet) -> List[Dict[str, Any]]:
        """
        Extracts and returns a list of definitions and their meanings as a string, from a given section
        """
        result = section.find('div', {'class': 'css-10n3ydx e1hk9ate0'})
        default_content =  result.find('div', {'class': 'default-content'})
        if not default_content:
            spans = result.find_all('span')
            list_of_definitions_and_examples_span =  [s.text.strip().replace(".", "") for s in spans if 'Slang' not in s.text.strip().replace(".", "")][0:3]
            return self.split_words_and_examples(list_of_definitions_and_examples_span)
        definitions = default_content.find_all('div')
        list_of_definitions_and_examples_default_content =  ["".join([word for word in d.text.strip().split(".") if '(def' not in word and "1)" not in word]) for d in definitions][0:3]
        
        return self.split_words_and_examples(list_of_definitions_and_examples_default_content)

    def get_meaning(self, word: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Returns part_of_speech and meanings for a given word
        """
        response = requests.get("https://www.dictionary.com/browse/{}".format(word))
        soup = BeautifulSoup(response.text, 'html.parser')
        meaning = soup.find('div', {'class': 'default-content'})
        sections = meaning.find_all('section', {"class": "css-109x55k e1hk9ate4"})
        if not sections:
            return {soup.find('span', {'class': 'luna-pos'}).text.strip().upper().replace(",", ""):self.meanings(soup)}
        return {s.find('span', {'class': 'luna-pos'}).text.strip().upper().replace(",", ""):self.meanings(s) for s in sections}
        
        
    def get_part_of_speech(self, word: str) -> Union[List[str],str]:
        """
        Returns the part_of_speech for a given word
        """
        url = "https://www.dictionary.com/browse/{}"
        response = requests.get(url.format(word))
        soup = BeautifulSoup(response.text, 'html.parser')
        meaning = soup.find('div', {'class': 'default-content'})
        sections = meaning.find_all('section', {"class": "css-109x55k e1hk9ate4"})
        if not sections:
            return soup.find('span', {'class': 'luna-pos'}).text.strip().upper().replace(",", "")
        return [s.find('span', {'class': 'luna-pos'}).text.strip().upper().replace(",", "") for s in sections]

