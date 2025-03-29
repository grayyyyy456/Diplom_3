import pytest
from selenium import webdriver
from curl import home_page



@pytest.fixture(params=["firefox", "chrome"], scope="function")
def browser(request):
    driver = None
    if request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(home_page)
    yield driver
    driver.quit()


