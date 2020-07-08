import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

def pytest_addoption(parser):
#    language_choices = ['ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr',
#                        'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk',
#                        'zh-cn']
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', type=str,
#                     choices=language_choices,
                     default='en-gb', action='store'
#                     , help=f'Set the site language from the list: {language_choices}'
                            f'')
#    parser = argparse.ArgumentParser(description='Set the site language')
#    parser.add_argument('--language', type=str, choices=language_choices,
#                        default='en-gb', action='store', help=f'Set the site language from '
#                                                           f'the list: {language_choices}')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    site_language = request.config.getoption("language")
    language_choices = ['ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr',
                       'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk',
                       'zh-cn']
    browser = None
    if site_language in language_choices:
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': site_language})
            browser = webdriver.Chrome(options=options)
#           browser = webdriver.Chrome()
            browser.implicitly_wait(5)
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", site_language)
            browser = webdriver.Firefox(firefox_profile=fp)
#           browser = webdriver.Firefox()
            browser.implicitly_wait(5)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    else:
        raise pytest.UsageError(f'Set the site language from the list: {language_choices}')
    yield browser
    print("\nquit browser..")
#    sleep(5)
    browser.quit()
