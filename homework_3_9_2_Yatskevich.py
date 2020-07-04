# -*- coding: utf-8 -*-

"""
Created on Wed Jul 01 2020 17:49:06

@author: Vovka Ya
"""

from selenium import webdriver
from time import sleep

#function find element by "element" name and send click
def click_btn_name(element):
    return browser.find_element_by_name(element).click()

#function find element by "element" id and send click
def click_btn_id(element):
    return browser.find_element_by_id(element).click()

#function find "element" by id and input "text"
def input_text_id(element, text):
    return browser.find_element_by_id(element).send_keys(text)

#function find element by "element" css selector and send click
def click_btn_css(element):
    return browser.find_element_by_css_selector(element).click()

#function return 1, in case of non empty list
def check_exists_by_css_selector(css_selector):
    return len(browser.find_elements_by_css_selector(css_selector)) > 0

#function return 1, in case of non empty list
def check_exists_by_xpath(xpath_selector):
    return len(browser.find_elements_by_xpath(xpath_selector)) > 0

def init_browser():
    browser.get(link)
    browser.implicitly_wait(5)
    return

#function for fill out login in form
def fill_out_loginform(login_def, password_def):
    browser.get(link)
    click_btn_id("login_link") #Click "Login in and registration" button
    input_text_id("id_login-username", login_def)  #Input login
    input_text_id("id_login-password", password_def) #Input password
    click_btn_name("login_submit") #Submit
    return

#function for fill out registration form
def fill_out_regform(login_def, password_def):
    browser.get(link)
    click_btn_id("login_link") #Click "Login in and registration" button
    input_text_id("id_registration-email", login_def)  #Input login
    input_text_id("id_registration-password1", password_def) #Input password
    input_text_id("id_registration-password2", password_def) #Repeat password
    click_btn_name("registration_submit") #Submit
    return

#function for delete created test profile
def delete_test_profile(password_def):
    click_btn_css("i.icon-user")    #Click account button
    click_btn_id("delete_profile")  #Click button delete profile
    input_text_id("id_password", password_def)
    click_btn_css("button.btn-danger")


login = "test1234@test.ru"
password = "986754?Нг"
link = "http://selenium1py.pythonanywhere.com/ru/"

try:
    #_____Test 1_Регистрация нового пользователя.
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
    # ***Preconditions
    browser = webdriver.Chrome()
    init_browser()
    print('Test 1. Preconditions executed')

    #***Test steps
    fill_out_regform(login, password)  # Fill out Registration form
    print('Test 1. Test steps executed')

    #***Check the result
    # Check whether existing message about successful registrationn
    assert 1 == check_exists_by_css_selector("div.alertinner.wicon")
#    sleep(5)
    print('Test 1. Result is expected')

    #***Postconditions
    delete_test_profile(password) #delete created test profile
    print('Test 1. Postconditions executed')

finally:
    browser.quit() #quit the browser
    print('Test 1. Passed')

try:
    #_____Test 2_Регистрация на существующий Email
    # Предусловия: Создать пользователя с заданным логином и паролем
    # 1. Нажать "Войти или Зарегистрироваться"Открылись 2 формы Войти и Зарегистрироваться
    # 2. Заполнить форму Зарегистрироваться
    # 3. Нажать кнопку "Зарегистрироваться"
    # Показывается сообщение "Опаньки! Мы нашли какие-то ошибки - пожалуйста,
    # проверьте сообщения об ошибках ниже и попробуйте еще раз"
    # Пользователь с таким адресом электронной почты уже зарегистрирован.
    # Использовать:
    # login = "test1234@test.ru"
    # password = "986754?Нг"

    # ***Preconditions. Create a user
    browser = webdriver.Chrome()
    init_browser()
    fill_out_regform(login, password)     #Create a test user
    click_btn_id("logout_link")     #Click logout button
    print('Test 2. Preconditions executed')

    #***Test steps
    fill_out_regform(login, password)     #Create the duplicated user
    print('Test 2. Test steps executed')

    #***Check the result
    # Check whether existing message about duplicated email
    assert 1 == check_exists_by_xpath('//*[text()=" Пользователь с таким адресом электронной почты уже зарегистрирован."]')
#    sleep(5)
    print('Test 2. Result is expected')

    #***Postconditions
    fill_out_loginform(login, password)  # Fill out login form
    delete_test_profile(password)   #delete created test profile
    print('Test 2. Postconditions executed')

finally:
    browser.quit() #quit the browser
    print('Test 2. Passed')
try:
    #_____Test 3_Пароль <9 символов

    # Предусловия: нет
    #1. Нажать "Войти или Зарегистрироваться"Открылись 2 формы Войти и Зарегистрироваться
    #2. Заполнить форму Зарегистрироваться Успешно
    #3. Нажать кнопку "Зарегистрироваться"
    #Показывается сообщение "Введённый пароль слишком короткий. Он должен
    #содержать как минимум 9 символов. Введённый пароль слишком широко распространён."

    # Использовать:
    # login = "test1234@test.ru"
    # password = "111111"

    # ***Preconditions. Create a user
    browser = webdriver.Chrome()
    init_browser()
    print('Test 3. Preconditions executed')

    #***Test steps
    fill_out_regform(login, "12345678")  #Create a user with password less than 9 characters
    print('Test 3. Test steps executed')

    #***Check the result
    # Check whether existing message about duplicated email
    assert 1 == check_exists_by_css_selector("i.icon-exclamation-sign")
#    sleep(5)
    print('Test 3. Result is expected')

    #***Postconditions
    print('Test 3. Postconditions executed')

finally:
#    browser.quit() #quit the browser
    print('Test 3. Passed')

try:
    #_____Test 4. Пароль = 9 символов
    # Предусловия: нет
    #Шаги.
    #1. Нажать "Войти или Зарегистрироваться"Открылись 2 формы Войти и Зарегистрироваться
    #2. Заполнить форму Зарегистрироваться Успешно
    #3. Нажать кнопку "Зарегистрироваться"
    #Ожидаемый результат. Показывается сообщение "Введённый пароль слишком широко распространён."
    #Постусловий нет
    # Использовать:
    # login = "test1234@test.ru"
    # password = "111111111"

    # ***Preconditions.
#    browser = webdriver.Chrome()
#    init_browser()
    click_btn_id("login_link") #Click "Login in and registration" button
    print('Test 4. Preconditions executed')

    #***Test steps
    fill_out_regform(login, "111111111")  #Create a user with simple password
    print('Test 4. Test steps executed')

    #***Check the result
    # Check whether error message occurred
    assert 1 == check_exists_by_xpath('//*[text()=" Введённый пароль слишком широко распространён."]')
#    sleep(5)
    print('Test 4. Result is expected')

    #***Postconditions
    print('Test 3. Postconditions executed')

finally:
#    browser.quit()  #quit the browser
    print('Test 4. Passed')

try:
    #_____Test 5. Спецсимволы в домене Email (допустимые)
    #Предусловий нет
    #1. Нажать "Войти или Зарегистрироваться"Открылись 2 формы Войти и Зарегистрироваться
    #2. Заполнить форму Зарегистрироваться Успешно
    #3. Нажать кнопку "Зарегистрироваться" Показывается сообщение "Спасибо за регистрацию!"
    #Все спецсимволы согласно спецификации
    #Постусловия:
    #1. Удалить созданного пользователя
    #2. Закрыть браузер

    # Использовать:
    # login = "test@t-est1234.р-ф567890"
    # password = "986754?Нг"

    # ***Preconditions
#    browser = webdriver.Chrome()
#    init_browser()
    print('Test 5. Preconditions executed')

    #***Test steps
    fill_out_regform("test@t-est1234.р-ф567890", password)  # Fill out Registration form
    print('Test 5. Test steps executed')

    #***Check the result
    # Check whether existing message about successful registrationn
    assert 1 == check_exists_by_css_selector("div.alertinner.wicon")
#    sleep(5)
    print('Test 5. Result is expected')

    #***Postconditions
    delete_test_profile(password) #delete created test profile
    print('Test 5. Postconditions executed')

finally:
    browser.quit() #quit the browser
    print('Test 5. Passed')

