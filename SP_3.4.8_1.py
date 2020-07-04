# -*- coding: utf-8 -*-

#Открыть страницу http://suninjuly.github.io/file_input.html
#Заполнить текстовые поля: имя, фамилия, email
#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#Нажать кнопку "Submit"

from selenium import webdriver
import os


def file_path(file_name):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(current_dir, file_name)
    return path

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)


browser.find_element_by_name("firstname").send_keys("VoV")
browser.find_element_by_name("lastname").send_keys("Ya")
browser.find_element_by_name("email").send_keys("test@test.ru")
browser.find_element_by_css_selector('[type="file"]').send_keys(file_path('file.txt'))
browser.find_element_by_class_name("btn").click()
