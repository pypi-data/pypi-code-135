import os
import re


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CleanText:
    """
    this function clean and prepare text to analysis
    """

    def __init__(self, input_txt, verbose=False):
        """
        This functions validates if the input of the class is a string.

        Parameters
        ----------
        input_txt:
            type: str
            String to clean.
        """
        method_name = "__init__"

        self.bad_words = ["y","de", "que", "la", "los", "el", "las"]
        with open(BASE_DIR + "/common/stopwords/English.txt", "r") as file:
            self.stopwords = file.read().splitlines()
        self.bad_words.extend(self.stopwords)
        with open(BASE_DIR + "/common/stopwords/Spanish.txt", "r") as file:
            self.stopwords = file.read().splitlines()
        self.bad_words.extend(self.stopwords)

        if type(input_txt) == str:
            self.input_txt = input_txt
        else:
            if verbose:
                print(f'WARNING: Input {input_txt} is not a string. Default set to "".')
                print(f"Class: {self.__str__()}\nMethod: {method_name}")
            self.input_txt = ""

    def process_text(
        self,
        rts=True,
        mentions=True,
        hashtags=True,
        links=True,
        spec_chars=True,
        stop_words=True,
    ):
        """
        This functions cleans the input text.

        Parameters
        ----------
        rts:
            type: bool
            If True the patterns associated with retweets are removed
            from the text, default=False.
        mentions:
            type: bool
            If True the mentions are removed from the text, default=False.
        hashtags:
            type: bool
            If True the hashtags are removed from the text, default=False.
        links:
            type: bool
            If True the patterns associated with links (urls) are removed
            from the text, default=False.
        spec_chars:
            type: bool
            If True all special characters (except accents, # and @) are removed
            from the text, default=False.
        stop_words:
            type: bool
            If True stop_words are removed from the, text, default=True.

        Returns
        -------
        str
        """

        input_txt = self.input_txt.lower()
        if rts:
            rt_pattern = re.compile(r"^(?:RT|rt) \@[a-zA-Z0-9\-\_]+\b")
            input_txt = re.sub(rt_pattern, "", input_txt)
        if mentions:
            mention_pattern = re.compile(r"\@[a-zA-Z0-9\-\_]+\b")
            input_txt = re.sub(mention_pattern, "", input_txt)
        else:
            # procect '@' signs of being removed in spec_chars
            input_txt = input_txt.replace("@", "xxatsignxx")
        if hashtags:
            hashtag_pattern = re.compile(r"\#[a-zA-Z0-9\-\_]+\b")
            input_txt = re.sub(hashtag_pattern, "", input_txt)
        else:
            # procect '#' signs to being removed in spec_chars
            input_txt = input_txt.replace("#", "xxhashtagsignxx")
        if links:
            link_pattern = re.compile(r"\bhttps:.+\b")
            input_txt = re.sub(link_pattern, "", input_txt)
            link_pattern = re.compile(r"\bhttp:.+\b")
            input_txt = re.sub(link_pattern, "", input_txt)
        if spec_chars:
            input_txt = re.sub(r"[^a-zA-Z\u00C0-\u00FF ]", " ", input_txt)

        if stop_words:
            temp_txt = input_txt.split()
            temp_txt = [word for word in temp_txt if word not in self.bad_words]
            output_txt = " ".join(temp_txt)

        output_txt = output_txt.replace("xxatsignxx", "@")
        output_txt = output_txt.replace("xxhashtagsignxx", "#")

        return output_txt
