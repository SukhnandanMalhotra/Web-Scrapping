import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time
import random

url =  "https://www.graduateshotline.com/gre-word-list.html"

r= requests.get(url)

html_content = r.text

soup = BeautifulSoup(html_content, "lxml")
w=[]
m=[]

fw =open('word_list.txt','w')

for tr in soup.find('table',{'class': 'tablex border1'}).find_all('tr'):
    tds=tr.find_all('td')
    fw.write(tds[0].text + ':'+tds[1].text+'\n')
fw.close()

fw = open('word_list.txt','r')
words=fw.read()
words = words.split('\n')

while True:
    i = random.randrange(0,len(words))
    os.system('notify-send -i edit-find "Word No. '+str(i)+' " "'+words[i]+'"')
    time.sleep (120)
    






    
