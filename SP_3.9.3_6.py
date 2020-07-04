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
    browser.implicitly_wait(5)
    browser.get(link)
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
def delete_test_profile():
    click_btn_css("i.icon-user") #Click account button
    click_btn_id("delete_profile") #Click button delete profile
    input_text_id("id_password", password)
    click_btn_css("button.btn-danger")


#Регистрация на существующий Email
#Предусловия: Создать пользователя с заданным логином и паролем
#1. Нажать "Войти или Зарегистрироваться"Открылись 2 формы Войти и Зарегистрироваться
#2. Заполнить форму Зарегистрироваться
#3. Нажать кнопку "Зарегистрироваться"
#Показывается сообщение "Опаньки! Мы нашли какие-то ошибки - пожалуйста,
#проверьте сообщения об ошибках ниже и попробуйте еще раз"
#Пользователь с таким адресом электронной почты уже зарегистрирован.
# Использовать:
# login = "test1234@test.ru"
#password = "986754?Нг"

login = "test1234@test.ru"
password = "986754?Нг"
link = "http://selenium1py.pythonanywhere.com/ru/"
browser = webdriver.Chrome()

try:
    #_____Test 5. Спецсимволы в домене Email (допустимые)
    #1. Нажать "Войти или Зарегистрироваться"Открылись 2 формы Войти и Зарегистрироваться
    #2. Заполнить форму Зарегистрироваться Успешно
    #3. Нажать кнопку "Зарегистрироваться" Показывается сообщение "Спасибо за регистрацию!"
    #Все спецсимволы согласно спецификации

    # Использовать:
    # login = "test@t-est1234.р-ф567890"
    # password = "986754?Нг"

    # ***Preconditions. Create a user
    browser = webdriver.Chrome()
    init_browser()

    #***Test steps
    fill_out_regform(login, "111111111")  #Create a user with simple password

    #***Check the result
    # Check whether error message occurred
    assert 1 == check_exists_by_xpath('//*[text()=" Введённый пароль слишком широко распространён."]')
    sleep(5)

    #***Postconditions

finally:
    browser.quit()  #quit the browser
