# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     svg
   Description :
   Author :       liaozhaoyan
   date：          2022/10/3
-------------------------------------------------
   Change Activity:
                   2022/10/3:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'


from soda import Tag


class eTag(Tag):
    def __init__(self,
                 tag_name: str,
                 *children,
                 self_closing: bool = True,
                 **attributes,
                 ):
        self.tag_name = tag_name
        self.children = list(children)
        self.attributes = {k.replace("__", ":").replace("_", "-"): v for k, v in attributes.items()}
        self.self_closing = self_closing




if __name__ == "__main__":
    pass
