from selenium.webdriver.common.by import By

class Locators:
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    btn = (By.XPATH, "//form[@id='add_to_basket_form']/button")

def test_btn_add_to_basket_available(browser):
    browser.get(Locators.link)
    assert True == (len(browser.find_elements(*Locators.btn)) == 1), "There is no button 'Add to basket' at the page"
