import requests
import json
from urllib.parse import urljoin
from bs4 import BeautifulSoup

FILE = 'books.json'

url = 'http://books.toscrape.com/'
count = 1
dct = {}

def parse_page(url, count):
    
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
        if not status == 200:
            print(f"Ошибка HTTP: {status}")
    except requests.ConnectionError:
        print("❌ Нет подключения к интернету")
        return
    except requests.Timeout:
        print("❌ Сервер не отвечает")
        return
    except Exception as e:
        print(f'❌ Неизвестная ошибка: {e}')
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')

    l = soup.find('ol', class_='row')
    if not l:
        print("❌ Контейнер с книгами не найден")
        return
    books = l.find_all('li')

    s = f'Страница {count}:'
    all_books = soup.find_all('h3')
    for num, book in enumerate(books, 1):
        title = book.find('h3').text
        price = book.find('p', class_='price_color').text

        if not title or not price:
            print('❌ Название или цена пустые')
            continue

        nal = book.find('p', class_="instock availability")
        nal_text = nal.text.strip() if nal else 'unknown'

        rating_tag = book.find('p', class_='star-rating')
        if rating_tag and rating_tag.get('class'):
            rating = rating_tag['class'][1]
        else:
            rating = 'unknown'
        dct.setdefault(s, {})[title] = {'цена': price, 'рейтинг': rating, 'наличие': nal_text}

    
    next_tag = soup.find('li', class_='next')
    if next_tag:
        next_url = urljoin(url, next_tag.find('a')['href'])
        count += 1
        parse_page(next_url, count)

def save(data):
    try:
        with open(FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
            print('Данные сохранены')
    except TypeError as e:
        print(f"❌ Ошибка: в данных есть несериализуемый тип ({e})")
        return
    except PermissionError:
        print("❌ Нет прав на запись файла")
        return
    except IOError as e:
        print(f"❌ Ошибка ввода-вывода: {e}")
        return
    except Exception as e:
        print(f"❌ Неизвестная ошибка при сохранении: {e}")
        return

print('Подождите идет парсинг...')
parse_page(url, 1)
save(dct)