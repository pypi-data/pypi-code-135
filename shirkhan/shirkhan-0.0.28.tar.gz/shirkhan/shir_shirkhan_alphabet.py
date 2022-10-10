"""
elipbe   字母表  alphabet
suzuq -> 元音 -> vowels
vzvk  -> 辅音 -> consonant
"""


class ShirkhanAlphabet:
    """
    elipbe   字母表  alphabet

    suzuq -> 元音 -> vowels

    vzvk  -> 辅音 -> consonant

    table

    HEMZE
    """

    HEMZE = "ئ"
    """
    [0] uy   母语字符
    [1] replacement 替代词[转码处理时可以参考]
    [2] is_vowels 是否元音
    [uly] uly 
    """
    table = {
        "ئ": ("ئ", "^", 0, "x"),  # 因分音节考虑 暂定为辅音
        "ا": ("ا", "a", 1, "a"),
        "ە": ("ە", "1", 1, "e"),
        "ې": ("ې", "e", 1, "ê"),
        "ى": ("ى", "i", 1, "i"),
        "و": ("و", "o", 1, "o"),
        "ۇ": ("ۇ", "u", 1, "u"),
        "ۆ": ("ۆ", "2", 1, "ô"),
        "ۈ": ("ۈ", "v", 1, "v"),
        "ب": ("ب", "b", 0, "b"),
        "پ": ("پ", "p", 0, "p"),
        "ت": ("ت", "t", 0, "t"),
        "ج": ("ج", "j", 0, "j"),
        "چ": ("چ", "q", 0, "ĉ"),  # ch
        "خ": ("خ", "h", 0, "ħ"),
        "د": ("د", "d", 0, "d"),
        "ر": ("ر", "r", 0, "r"),
        "ز": ("ز", "z", 0, "z"),
        "ژ": ("ژ", "3", 0, "ĵ"),  # zh
        "س": ("س", "s", 0, "s"),
        "ش": ("ش", "x", 0, "ŝ"),  # sh
        "غ": ("غ", "4", 0, "ĝ"),  # gh
        "ق": ("ق", "5", 0, "q"),
        "ف": ("ف", "f", 0, "f"),
        "ك": ("ك", "k", 0, "k"),
        "گ": ("گ", "g", 0, "g"),
        "ڭ": ("ڭ", "6", 0, "ñ"),  # ng
        "ل": ("ل", "l", 0, "l"),
        "م": ("م", "m", 0, "m"),
        "ن": ("ن", "n", 0, "n"),
        "ھ": ("ھ", "7", 0, "ĥ"),  # h
        "ۋ": ("ۋ", "w", 0, "w"),
        "ي": ("ي", "y", 0, "y"),
        "-": ("-", "-", 1, "-"),
    }

    @staticmethod
    def alpha_info(alpha: str):
        table = ShirkhanAlphabet.table
        if alpha in table:
            return table.get(alpha)
        else:
            return None

    @staticmethod
    def is_vowels(alpha: str):
        info = ShirkhanAlphabet.alpha_info(alpha)
        if info is None:
            return info
        return info[2]


class ShirkhanConverter:
    def __init__(self, word: str):
        self.word = word
        # 吧非母语部分清理掉
        # todo

    def toShirkhan(self):
        # 如果开头是 Hemze 得去掉,还原时补充即可
        word = self.word

        if word[0] == ShirkhanAlphabet.HEMZE:
            word = word[1:]
        return "".join([ShirkhanAlphabet.alpha_info(alpha)[3] for alpha in word])

    def shirkhanToUg(self):
        # 生成 shirkhan ,ug 映射关系
        khan_ug = []
        for key in ShirkhanAlphabet.table:
            info = ShirkhanAlphabet.table.get(key)
            ug, khan = info[0], info[3]
            khan_ug.append((khan, ug))

        # 倒序排序，从最长的开始替换
        khan_ug = sorted(khan_ug, key=lambda x: len(x[0]), reverse=True)

        result = self.word
        for item in khan_ug:
            if len(item[0]) == 0:
                continue
            result = result.replace(item[0], item[1])

        # 如果第一个字符是元音，需要补充Hemze
        if ShirkhanAlphabet.is_vowels(result[0]):
            result = ShirkhanAlphabet.HEMZE + result
        return result


def ug2shirkhan(word):
    """
    吧给定单词转换成uly
    :param word:
    :return:
    """
    return ShirkhanConverter(word).toShirkhan()


def shirkhan2ug(word):
    """
    吧给定uly 转换回ug
    :param word:
    :return:
    """
    return ShirkhanConverter(word).shirkhanToUg()


if __name__ == '__main__':
    pass
