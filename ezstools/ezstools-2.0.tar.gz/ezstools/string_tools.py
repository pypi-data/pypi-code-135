from typing import List
import re, enchant, json, pathlib

HERE = pathlib.Path(__file__).parent

def most_similar_string(target: str, options: List[str], case_sensitive: bool = True) -> str:
    # Returs most similar item to target from options
    percents = {}

    if not case_sensitive:
        options = [*map(lambda w: w.lower(), options)]
        target = target.lower()

    for word in options:
        similar_count: int = 0

        for word_char, target_char in zip(word, target):

            if word_char == target_char:
                similar_count += 1

        # calculate percent
        percents[word] = (similar_count * 100) / len(word)

    return sorted(percents, key=percents.get)[-1]


def is_word(word: str):
    dicts = [
        enchant.Dict("en"),
    ]
    return any([d.check(word) for d in dicts])

def normalice(string: str) -> str:
    symbol_subs = {
        '$' : 's',
        '5' : 's',
        '1' : 'i',
        '*' : 'u',
        '7' : 't',
        '3' : 'e',
        '6' : 'g',
        '0' : 'o',
        '8' : 'b'
    }

    homoglyphs_subs = json.load(open(f"{HERE}/homoglyphs_subs.json", "r"))

    result: List[str] = []

    for word in string.split(" "):

        # matchs = chars that are not allowed
        matchs = list(re.findall(r"[^a-zA-Z0-9_ ]", word))

        is_caps = (word == word.upper())

        # homyglyphs sub (similar letters sub)
        for char, sub in homoglyphs_subs.items():
            word = re.sub(char, sub.upper() if is_caps else sub, word)

        # if no char needs to be replaced with symbol sub then continue
        if not matchs or all([(char in matchs) for char in word]):
            result.append(word)
            continue

        # if there are not allowed chars, then replace them
        for match in matchs:

            # symbol substitution process
            sub = symbol_subs.get(match, None)

            if not sub:
                result.append(word)
                continue

            sub = sub.upper() if is_caps else sub 
            new_word = word.replace(match, sub)

            # if symbol sub made a word keep it as new word if not keep old word
            result.append(new_word if is_word(new_word) else word)

    return " ".join(result)
    