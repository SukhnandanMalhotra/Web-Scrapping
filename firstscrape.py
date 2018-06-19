import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.merriam-webster.com/word-of-the-day')
soup = BeautifulSoup(res.text , 'lxml')
word = soup.find('h1')
content = soup.find('div',{'class':'wod-definition-container'}).find('p')
    
l1=word.text
l2=content.text
print(l1,l2)
L=['Word of the day!\n',l1,l2]
file1=open('wotd.txt','w')
file1.writelines(L)
file1.close()

