





#Кириллица в имени Email
#1. Нажать "Войти или Зарегистрироваться"Открылись 2 формы Войти и Зарегистрироваться
#2. Заполнить форму Зарегистрироваться Успешно
#email - тест@test.ru
#пароль - 986754?Нг
#повторить пароль - 986754?Нг
#3. Нажать кнопку "Зарегистрироваться"
#Показывается сообщение "Часть адреса до символа @ не должно содержать кириллицу"

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
#browser = webdriver.Chrome()
#browser.implicitly_wait(5)

try:
    #_____Test 2. Пароль <9 символов

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

    #***Test steps
    fill_out_regform(login, "11111111")  #Create a user with password less than 9 characters

    #***Check the result
    # Check whether error message occurred
    assert 1 == check_exists_by_css_selector("i.icon-exclamation-sign")
    sleep(5)

    #***Postconditions

finally:
    browser.quit() #quit the browser
