# -*- coding: utf-8 -*-

#Ваша программа должна выполнить следующие шаги:
#Открыть страницу http://SunInJuly.github.io/execute_script.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x.
#Проскроллить страницу вниз.
#Ввести ответ в текстовое поле.
#Отметить checkbox "I'm the robot".
#Выбрать radiobutton "Robots rule!".
#Нажать на кнопку Submit.

from selenium import webdriver
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#    x_element = browser.find_element_by_xpath("//*/@valuex") - не работает
    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    find_element = browser.find_element_by_id("answer")
    find_element.send_keys(y)

    find_element = browser.find_element_by_id("robotCheckbox")
    find_element.click()

    find_element = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", find_element)
    find_element.click()

    browser.find_element_by_class_name("btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
