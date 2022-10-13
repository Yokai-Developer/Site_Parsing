from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import time

product_list = []

browser = webdriver.Chrome()
browser.get('https://www.citilink.ru/catalog/chistyaschie-sredstva--pnevmaticheskie-ochistiteli/')

cards = browser.find_element(By.CLASS_NAME, 'ProductCardCategoryList__grid').text
for card in cards:
    product_list.append(card)
print(product_list)

time.sleep(2)
browser.close()
