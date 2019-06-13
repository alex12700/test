# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen #urllib2
 
html_doc = urlopen('https://www.xmeye.net/index').read()
soup = BeautifulSoup(html_doc)
 
for img in soup.find_all('img'):
    print('https://www.xmeye.net/index' + img.get('src'))