# -*- coding: utf-8 -*-

#Ваша программа должна выполнить следующие шаги:

#Открыть страницу http://suninjuly.github.io/selects1.html
#Посчитать сумму заданных чисел
#Выбрать в выпадающем списке значение равное расчитанной сумме
#Нажать кнопку "Submit"

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element_by_id("num1").text
    x2 = browser.find_element_by_id("num2").text
    x = int(x1) + int(x2)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(x))

    browser.find_element_by_class_name("btn-default").click()

finally:
    # успеваем скопировать код за 30 секунд
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
