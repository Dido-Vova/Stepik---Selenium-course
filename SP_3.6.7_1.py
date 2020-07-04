# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import sin, fabs, log
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Locators:
    btn_book = (By.ID, 'book')
    field_input_answer = (By.ID, 'answer')
    btn_submit = (By.ID, 'solve')
    x_value = (By.ID, 'input_value')
    price = (By.ID, 'price')

#Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#Нажать на кнопку "Book"
#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

def compute_capcha(x):
    c = log(fabs(12 * sin(x)))
    return c

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(Locators.price, "$100")
    )
    browser.find_element(*Locators.btn_book).click()
#    button.click()

    # акцептуем модальное окошко
#    confirm = browser.switch_to.alert
#    confirm.accept()

#    # находим элемент, содержащий значение х
#    input_value = browser.find_element(*x_value).text
#    # записываем в переменную число из элемента input_value
#    x_value_text = browser.find_element(*Locators.x_value).text
    x_value = int(browser.find_element(*Locators.x_value).text)
    input_answer_value = str(compute_capcha(x_value))
#    print(input_answer_value)
#    browser.find_element(*Locators.field_input_answer).send_keys(str(compute_capcha(int(browser.find_element(*Locators.x_value)))))
    browser.find_element(*Locators.field_input_answer).send_keys(input_answer_value)
#    input_answer.send_keys(input_answer_value)
    browser.find_element(*Locators.btn_submit).click()
    # читаем )
    #time.sleep(1)

#    button.click()

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
