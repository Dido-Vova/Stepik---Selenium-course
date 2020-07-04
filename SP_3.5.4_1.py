# -*- coding: utf-8 -*-


from selenium import webdriver
import time
from math import sin, fabs, log


# решить капчу для роботов, чтобы получить число с ответом
# What is ln(abs(12*sin(x))), where x =

def compute_capcha(x):
    c = log(fabs(12 * sin(x)))
    return c

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # акцептуем модальное окошко
    confirm = browser.switch_to.alert
    confirm.accept()

    # находим элемент, содержащий значение х
    input_value = browser.find_element_by_id("input_value")
    # записываем в переменную число из элемента input_value
    x_value_text = input_value.text
    x_value = int(x_value_text)
    input_answer_value = str(compute_capcha(x_value))
    print(input_answer_value)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(input_answer_value)

    # читаем )
    #time.sleep(1)

    button.click()

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
