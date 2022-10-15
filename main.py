from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary

product_list = []
modtoplist = []
reslist = []

def structure_list(product_list, modtoplist, reslist):
    i = 1
    j = 0
    # Собираем данные полученные с сайта в слова и значения
    while i < len(product_list):
        if product_list[i] == '\n':
            modtoplist.append(product_list[0])
            product_list.pop(i)
            product_list.pop(0)
        else:
            product_list[0] += product_list[i]
            product_list.pop(i)
    product_list.clear()
    # Структурируем данные в удобный и читаемый вид по индексам
    while j < len(modtoplist):
        if len(modtoplist[j]) > 20:
            if modtoplist[j] != 0:
                if len(modtoplist[j - 2]) == 3:
                    layout = modtoplist[j + 2] + ' ' + modtoplist[j - 2] + ' ' + modtoplist[j] + ' ' + \
                             modtoplist[j + 3] + modtoplist[j + 4]
                else:
                    layout = modtoplist[j + 2] + ' ' + modtoplist[j] + ' ' + \
                             modtoplist[j + 3] + modtoplist[j + 4]
                reslist.append(layout)
        j += 1
    for i in reslist:
        print(i)


browser = webdriver.Chrome()
browser.get('https://www.citilink.ru/catalog/chistyaschie-sredstva--pnevmaticheskie-ochistiteli/')

cards = browser.find_element(By.CLASS_NAME, 'ProductCardCategoryList__grid').text
for card in cards:
    product_list.append(card)
print(product_list)

structure_list(product_list, modtoplist, reslist)
browser.close()
