import json
# разбор html файлов с помощью библиотеки BeautifulSoup
from bs4 import BeautifulSoup

datafile = open('D:\Project\Site_Parsing\Practice\webinars.json', 'r', encoding='utf-8')
data = json.load(datafile)

# [webinar['speaker'] for webinar in data]
for webinar in data:
    print(webinar['speaker'])

html_file = open('D:\Project\Site_Parsing\Practice\skillbox.html', 'r', encoding='utf-8')
code = html_file.read()
soup = BeautifulSoup(code, 'html.parser')  # Парсинг html-кода => суп (из html-элементов)
# CSS-селекторы: способ найти что-то на HTML-страницы
links = soup.find_all('a')  # Найти все ссылки
for link in links:
    print(link['href'])
