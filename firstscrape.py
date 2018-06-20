#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import os

import sys
sys.path.append("/usr/lib/python3/dist-packages")

res = requests.get('https://www.merriam-webster.com/word-of-the-day')
soup = BeautifulSoup(res.text , 'lxml')
word = soup.find('h1')
content = soup.find('div',{'class':'wod-definition-container'}).find('p')
    
l1=word.text
l2=content.text
l=l1+l2
print(l)

os.system('notify-send "Word of the day! -" "'+l+'"')

    
