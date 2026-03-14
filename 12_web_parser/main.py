import requests
import json
from urllib.parse import urljoin
from bs4 import BeautifulSoup

FILE = 'books.json'

url = 'http://books.toscrape.com/'
count = 1
dct = {}

def parse_page(url, count):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    l = soup.find('ol', class_='row')
    books = l.find_all('li')

    s = f'Страница {count}:'
    all_books = soup.find_all('h3')
    for num, book in enumerate(books, 1):
        title = book.find('h3').text
        price = book.find('p', class_='price_color').text
        nal = book.find('p', class_="instock availability").text.strip()
        rating = book.find('p', class_='star-rating')['class'][1]
        dct.setdefault(s, {})[title] = {'цена': price, 'рейтинг': rating, 'наличие': nal}

    
    next_tag = soup.find('li', class_='next')
    if next_tag:
        next_url = urljoin(url, next_tag.find('a')['href'])
        count += 1
        parse_page(next_url, count)

parse_page(url, 1)