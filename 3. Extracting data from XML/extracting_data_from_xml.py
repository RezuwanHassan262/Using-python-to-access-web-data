# -*- coding: utf-8 -*-
"""Extracting data from XML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rHuVoTwDQ1WCWfDmMghWq-DDlMk5VGbx
"""

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_851240.xml (Sum ends with 51)

import xml.etree.ElementTree as ET
from urllib.request import urlopen
a = 0
url = input('Enter - ')
html = urlopen(url).read()
tree = ET.fromstring(html)
for item in tree.iter():
    if item.tag == "count":
        b = int(item.text)
        a = a +b
print(a)

