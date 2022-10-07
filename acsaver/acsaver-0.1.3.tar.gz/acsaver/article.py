# coding=utf-8
from .utils import os, Bs, SaverBase, downloader

__author__ = 'dolacmeo'


class ArticleSaver(SaverBase):

    def __init__(self, acer, ac_obj):
        self.acer = acer
        self.ac_obj = ac_obj
        super().__init__(acer, ac_obj)

    def _gen_html(self) -> bool:
        page_html = self.page_template.render(dict(saver=self))
        html_obj = Bs(page_html, 'lxml')
        img_tasks = list()
        for img in html_obj.select('.article-content img'):
            if img.attrs['src'].startswith('http') or img.attrs['src'].startswith('//'):
                img_name = img.attrs['src'].split('/')[-1]
                saved_path = os.path.join(self._img_path, img_name)
                img_tasks.append((img.attrs['src'], saved_path))
                img.attrs['alt'] = img.attrs['src']
                img.attrs['class'] = "lazy"
                img.attrs['src'] = "../../assets/img/logo-gray.png"
                img.attrs['data-src'] = f"./img/{img_name}"
        if len(img_tasks) > 0:
            downloader(self.acer.client, img_tasks, display=True)
        html_path = os.path.join(self._save_path, f"{self.rid}.html")
        with open(html_path, 'wb') as html_file:
            html_file.write(html_obj.prettify().encode())
        return os.path.isfile(html_path)

    def save_all(self):
        self._save_raw()
        self._save_image()
        self._gen_html()
        self._save_comment()
        self.update_js_data()
