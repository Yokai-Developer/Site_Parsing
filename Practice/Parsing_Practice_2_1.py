# Парсинг hh.ru с помощью Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
import re

browser = webdriver.Chrome()  # Запускаем браузер
browser.get('http://hh.ru')  # Открываем hh.ru

search_input = browser.find_element(By.ID, 'a11y-search-input')  # Находим поле поискового запроса
search_input.send_keys('Junior Python')  # Вводим Junior Python

search_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="search-button"]')  # Идентифицируем кнопку
search_button.click()  # Нажимаем кнопку "Найти работу"

# Заголовок с кол-вом вакансий
job_count = browser.find_element(By.CSS_SELECTOR, '[data-qa="vacancies-search-header"] h1')
# re.sub - сделать замену
# \D символы, не являющиеся цифрой
count = re.sub(r'\D', '', job_count.text)
print(f'Found exactle {count} jobs')

browser.close()  # Закрываем браузер
