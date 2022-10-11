import json
import requests  # HTTP-запросы
from bs4 import BeautifulSoup  # разбор html файлов с помощью библиотеки BeautifulSoup

# Парсинг файла Json
datafile = open('D:\Project\Site_Parsing\Practice\webinars.json', 'r', encoding='utf-8')
data = json.load(datafile)
print([webinar['speaker'] for webinar in data])

# Парсинг файла HTML
html_file = open('D:\Project\Site_Parsing\Practice\skillbox.html', 'r', encoding='utf-8')
code = html_file.read()
soup = BeautifulSoup(code, 'html.parser')  # Парсинг html-кода => суп (из html-элементов)
# CSS-селекторы: способ найти что-то на HTML-страницы
links = soup.find_all('a')  # Найти все ссылки
print([link["href"] for link in links])

# Парсинг сайта Skillbox (названия вебинаров)
skillbox = requests.get('https://live.skillbox.ru/')
skill_soup = BeautifulSoup(skillbox.content, 'html.parser')
webinars = skill_soup.find_all(class_="webinar-card__title")  # Обращение к классу названий вебинаров HTTP страницы
print([webinar.string.strip() for webinar in webinars])

# Парсинг сайта Skillbox (получение полной информации о вебинаре)
items = skill_soup.find_all(class_='webinars__item')  # Список карточек вебинара
for webinar in items:
    title = webinar.find(class_="webinar-card__title").string.strip()  # Заголовок конкретного вебинара
    date = webinar.find(class_="webinar-card__date").string.strip()  # Дата конкретного вебинара
    print(f'Вебинар {title} прошел {date}')
