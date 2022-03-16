import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language:")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language is None:
        language = "en"
    print(f"\nstart browser for {language} language test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_experimental_option('excludeSwitches', ['enable-logging']) #Игнорирование сообщений от DevTools
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()