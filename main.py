import requests as requests
from bs4 import BeautifulSoup

API = 'https://appbrewery.github.io/Zillow-Clone/'

r = requests.get(API)
r.raise_for_status()
zillow_web_contents = r.text

rent_data = BeautifulSoup(zillow_web_contents, 'html.parser')
data = rent_data.findAll(name='a', class_='StyledPropertyCardDataArea-anchor')
for _ in data:
    print(f'{_.getText().strip()} | {_.get("href")}')
data1 = rent_data.findAll(name='div', class_='PropertyCardWrapper')
for _ in data1:
    price = _.getText().strip()[:6]
    print(price)