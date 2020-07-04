# -*- coding: utf-8 -*-

"""
Created on Sat Jun 28 20:22:06 2020

@author: Vovka Ya
"""

# Регистрация нового пользователя.
# 1. Предусловия. Нет
# 2. Шаги теста:
#           - Открыть страницу,
#           - Нажать "Войти или Зарегистрироваться"
#           - Заполнить форму "Зарегистрироваться" (использовать логин::пароль test1234@test.ru::986754?Нг)
#           - Нажать кнопку "Зарегистрироваться";
# 3. Ожидаемый результат:
#           - Показывается сообщение об успешной регистрации;
# 4. Пост-условия:
#           - Удалить созданного пользователя,
#           - Закрыть браузер.

from selenium import webdriver
import time

#функция вернет 1, если список с выбранным селектором не пустой
def check_exists_by_css_selector(css_selector):
    return len(browser.find_elements_by_css_selector(css_selector)) > 0

browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    #***Предусловия
    #***Шаги теста
    # Открыть основную страницу сайта
    browser.get("http://selenium1py.pythonanywhere.com/ru/")

    #Нажать "Войти и зарегистрироваться"
    find_element = browser.find_element_by_id("login_link")
    find_element.click()

    #Открылась страница входа и регистрации
    #current_url = browser.current_url

    #http://selenium1py.pythonanywhere.com/ru/accounts/login/

    # Заполнить форму "Зарегистрироваться"
    # используя логин::пароль test1234@test.ru::986754?Нг
    # Нажать кнопку зарегистрироваться
    user_name = "test1234@test.ru"
    find_element = browser.find_element_by_id("id_registration-email")
    find_element.send_keys(user_name)

    user_password = "986754?Нг"
    find_element = browser.find_element_by_id("id_registration-password1")
    find_element.send_keys(user_password)

    find_element = browser.find_element_by_id("id_registration-password2")
    find_element.send_keys(user_password)

    find_element = browser.find_element_by_name("registration_submit")
    find_element.click()

    #***Проверка результата
    # Проверить, что открывшаяся страница содержит галку об успешной регистрации
    # Не стал использовать текст "Спасибо за регистрацию!" т.к. это приведет к ошибке
    # в другой локализации.
    assert 1 == check_exists_by_css_selector("i.icon-ok-sign")

    # пауза перед закрытием для посмотреть
    #time.sleep(10)

    #***Постусловия
    #Удалить созданный профиль
    find_element = browser.find_element_by_css_selector("i.icon-user")
    find_element.click()
    find_element = browser.find_element_by_id("delete_profile")
    find_element.click()
    find_element = browser.find_element_by_id("id_password")
    find_element.send_keys(user_password)
    find_element = browser.find_element_by_css_selector("button.btn-danger")
    find_element.click()

finally:

    # пауза перед закрытием для посмотреть
    #time.sleep(10)

    # закрываем браузер после всех манипуляций
    browser.quit()
