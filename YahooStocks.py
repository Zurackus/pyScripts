#! python 3
import bs4
import requests
from bs4 import beautifulsoup

def parsePrice():
    r=requests.get('yahoo url')
    soup=bs4.beautifulsoup(r.text,"xml")
    price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

while True:
    print('The current price: '+str(parsePrice()))