# -*- coding: utf-8 -*-
# @Time    : 2022/10/6 10:51
# @Author  : LiZhen
# @FileName: string_utils.py
# @github  : https://github.com/Lizhen0628
# @Description:

import os
from collections import defaultdict

import regex as re
from pathlib import Path
from weathon.utils.char_utils import CharUtils
from weathon.utils.string_converter import ConvertMap,Converter
from typing import List, Union


def add_curr_dir(name):
    return os.path.join(os.path.dirname(__file__), name)


class StringUtils:

    @staticmethod
    def cut_sentences(sentence: str) -> List[str]:
        sentence_delimiters = ['。', '？', '！', '…']
        sents = []
        tmp = []
        for ch in sentence:  # 遍历字符串中的每一个字
            tmp.append(ch)
            if ch in sentence_delimiters:
                sents.append(''.join(tmp))
                tmp = []
        if len(tmp) > 0:  # 如以定界符结尾的文本的文本信息会在循环中返回，无需再次传递
            sents.append(''.join(tmp))
        return sents

    @staticmethod
    def is_number_string(string: str) -> bool:
        """判断字符串是否全为数字"""
        return all(CharUtils.is_number(c) for c in string)

    @staticmethod
    def is_chinese_string(string: str) -> bool:
        """判断字符串是否全为汉字"""
        return all(CharUtils.is_chinese_char(c) for c in string)

    @staticmethod
    def escape_re_character(s: str) -> str:
        """对正则字符添加转义"""
        escape_char = ["\\", "\"", "*", ".", "?", "+", "$", "^", "[", "]", "(", ")", "{", "}", "|", "-"]
        for c in escape_char:
            if c in s:
                s = s.replace(c, re.escape(c))
        return s

    @staticmethod
    def B2Q(text: str) -> str:
        """
        字符串半角转全角
        Args:
            text: 输入字符串

        Returns:转化后字符串
        """
        return "".join([CharUtils.B2Q(c) for c in text])

    @staticmethod
    def Q2B(text: str) -> str:
        """
        字符串全角转半角
        Args:
            text: 输入字符串

        Returns:转化后字符串
        """
        return "".join([CharUtils.Q2B(c) for c in text])

    @staticmethod
    def as_text(text: str) -> Union[str, None]:
        """生成unicode字符串"""
        if text is None:
            return text
        elif isinstance(text, bytes):
            return text.decode('utf-8', errors='ignore')
        elif isinstance(text, str):
            return text
        else:
            raise ValueError('Unknown type %r' % type(text))

    @staticmethod
    def wechat_expression_2_word(text: str) -> str:
        """将文本中的微信表情代码转化成文字"""
        from weathon.utils.constants import wechat_face as code_expression

        for key, value in code_expression.items():
            text = text.replace(key, value)
        return text

    @staticmethod
    def traditional2simple(text: str) -> str:
        """将繁体字符串转化为简体字符串"""
        dic_file = Path(__file__).parent.parent / "data/traditional2simple.txt"
        lines = dic_file.read_text().split("\n")
        word_map = defaultdict()
        for line in lines:
            splits = line.split()
            if len(splits) == 2:
                word_map[splits[0]] = splits[1]
        return Converter(ConvertMap(word_map)).convert(text)


if __name__ == '__main__':
    print(StringUtils.traditional2simple("現代社會，很多人都想有個紅顏知己，也就是異性朋友，在自己孤獨寂寞時，可以有個出口。只是異性朋友在一起，難免會引人遐想，或許你只是單純地認為，有個這樣的朋友，能讓自己可以放心訴說心事，還能夠保持單純的朋友關係。"))