import requests
import json
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
count = 1

def parse_page(url, count):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    l = soup.find('ol', class_='row')
    books = l.find_all('li')

    print(f'Страница {count}:')
    all_books = soup.find_all('h3')
    for num, book in enumerate(books, 1):
        title = book.find('h3')
        price = book.find('p', class_='price_color')
        print(f'{num}. {title.text} - {price.text}')

parse_page(url, 1)