from mussum_ipsun.create import Ipsum


class GenerateMussumIpsun:
    def __init__(self):
        self.ipsum = Ipsum()

    def generate_word(self):
        return self.ipsum.get_random_word()

    def generate_phrase(self):
        return self.ipsum.get_random_phrase()

    def generate_paragraph(self):
        return self.ipsum.get_random_paragraph()

    def generate_text(self):
        return self.ipsum.get_random_text()


if __name__ == '__main__':
    mussum = GenerateMussumIpsun()
    print(mussum.generate_word())
    print(mussum.generate_phrase())
    print(mussum.generate_paragraph())
    print(mussum.generate_text())