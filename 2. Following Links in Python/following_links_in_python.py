# -*- coding: utf-8 -*-
"""Following Links in Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rHuVoTwDQ1WCWfDmMghWq-DDlMk5VGbx
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
href = soup('a')
for i in range(count):
    link = href[position].get('href', None)
    print(href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')

