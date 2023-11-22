import requests as requests
from bs4 import BeautifulSoup


ZILLOW_API = 'https://appbrewery.github.io/Zillow-Clone/'  # Zillow webpage of renting in California

r = requests.get(ZILLOW_API)
r.raise_for_status()
zillow_web_contents = r.text

rent_data = BeautifulSoup(zillow_web_contents, 'html.parser')

data = rent_data.findAll(name='a', class_='StyledPropertyCardDataArea-anchor')
data1 = rent_data.findAll(name='div', class_='PropertyCardWrapper')
list_add = [_.getText().strip() for _ in data]
list_links = [links.get("href") for links in data]
list_prices = [price.getText().strip()[:6] for price in data1]

# print(list_prices)
# print(list_links)
# print(list_add)