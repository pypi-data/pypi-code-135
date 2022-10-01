import re
from random import choice


class Ipsum:
    def __init__(self):
        self.final_list = list()
        self.final_list_phrase = list()
        self.word = """
            Cacilds vidis litro abertis.
            Quem manda na minha terra sou euzis.
            Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis.
            Não sou faixa preta cumpadi, sou preto inteiris, inteiris.
            Manduma pindureta quium dia nois paga.
            Copo furadis é disculpa de bebadis, arcu quam euismod magna.
            Manduma pindureta quium dia nois paga.
            Em pé sem cair, deitado sem dormir, sentado sem cochilar e fazendo pose.
            Mauris nec dolor in eros commodo tempor.
            Aenean aliquam molestie leo, vitae iaculis nisl."""

    def edict_word(self):
        list_strings = self.word.split()
        for index in list_strings:
            new_string: str = re.sub(r"[^a-zA-Z0-9]", "", index)
            if len(new_string) > 3:
                self.final_list.append(new_string.capitalize())
        return self.final_list

    def get_random_word(self):
        return choice(self.edict_word())

    def get_random_phrase(self):
        list_str = self.word.split(".")
        for index in list_str:
            if len(index) > 3:
                self.final_list_phrase.append(index.strip())
        phrase = choice(self.final_list_phrase)
        return f"{phrase.strip()}."

    def get_random_paragraph(self):
        paragraf = ""
        for _ in range(5):
            phrase = self.get_random_phrase()
            paragraf = paragraf + " " + phrase
        return paragraf.strip()

    def get_random_text(self):
        text = ""
        for _ in range(40):
            phrase = self.get_random_phrase()
            text = text + " " + phrase
        return text.strip()


if __name__ == '__main__':

    ipsum = Ipsum()

    print(ipsum.get_random_word())
    print(ipsum.get_random_phrase())
    print(ipsum.get_random_paragraph())
    print(ipsum.get_random_text())
