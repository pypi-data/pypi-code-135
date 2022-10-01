# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['legendyoutube']
setup_kwargs = {
    'name': 'legendyoutube',
    'version': '0.0.1',
    'description': 'yuklovchi',
    'long_description': '```python \nfrom youtubepy import *\nfrom pytube import YouTube\nimport eel\nfrom pywebio import *\nfrom pywebio import start_server\nfrom pywebio.input import *\nfrom pywebio.output import *\n\neel.init("web")\n#ask for the link from user\nlink = input("Enter the link of YouTube video you want to download:  ")\nyt = YouTube(link)\n\n#Showing details\nprint("Title: ",yt.title)\nprint("Number of views: ",yt.views)\nprint("Length of video: ",yt.length)\nprint("Rating of video: ",yt.rating)\n#Getting the highest resolution possible\nys = yt.streams.get_highest_resolution()\n\n#Starting download\nprint("Downloading...")\nys.download()\nprint("Download completed!!")\neel.start("index.html")\n\n\nstart_server( port=8080)\n',
    'author': 'Ibragimov Ravshanbek',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
