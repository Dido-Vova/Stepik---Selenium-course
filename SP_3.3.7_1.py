# -*- coding: utf-8 -*-

#Ваша программа должна выполнить следующие шаги:
#Открыть страницу http://suninjuly.github.io/get_attribute.html.
#Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
#Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
#Считать значение для переменной x.
#Посчитать математическую функцию от x (код для этого приведён ниже).
#Ввести ответ в текстовое поле.
#Отметить checkbox "I'm the robot".
#Выбрать radiobutton "Robots rule!".
#Нажать на кнопку Submit.

from selenium import webdriver
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
#    x_element = browser.find_element_by_xpath("//*/@valuex") - не работает
    x = x_element.get_attribute("valuex")
    y = calc(x)

    find_element = browser.find_element_by_id("answer")
    find_element.send_keys(y)
    find_element = browser.find_element_by_id("robotCheckbox")
    find_element.click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_class_name("btn-default").click()

finally:
    # успеваем скопировать код за 30 секунд
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
