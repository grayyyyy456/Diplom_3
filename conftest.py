import pytest
from selenium import webdriver
from curl import home_page
import allure
from helper import register_new_user_and_return_login_password
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_page import OrderPage



@pytest.fixture(params=["firefox", "chrome"], scope="session")
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


@allure.step("Авторизация с предоставленными данными")
@pytest.fixture(scope="session")
def perform_login(browser):
    data_create_user = register_new_user_and_return_login_password()

    email = data_create_user["email"]
    password = data_create_user["password"]

    page = HomePage(browser)
    login_page = LoginPage(browser)

    page.wait_button_personal_account()
    page.click_button_personal_account()

    login_page.filling_email_field_login(email)
    login_page.filling_password_field_login(password)

    login_page.wait_button_login()
    login_page.click_button_login()
    return login_page


@allure.step("Процесс создания нового заказа")
@pytest.fixture(scope="session")
def create_order(browser):
    counter = OrderPage(browser)
    counter.wait_first_ingredient()
    counter.drag_and_drop_ingredient()
    counter.wait_button_order()
    counter.click_button_order()
    counter.wait_window_exit_order()
    counter.click_window_exit_order()
    return counter
