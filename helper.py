import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.order_page import OrderPage
import allure
import random
import string
import requests




def register_new_user_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=payload)
    return {
        "email": email,
        "password": password
    }

@allure.step("Авторизация с предоставленными данными")
def perform_login(browser):
    data_create_user = register_new_user_and_return_login_password()

    email = data_create_user["email"]
    password = data_create_user["password"]

    home_page = HomePage(browser)
    login_page = LoginPage(browser)

    home_page.wait_button_personal_account()
    home_page.click_button_personal_account()

    login_page.filling_email_field_login(email)
    login_page.filling_password_field_login(password)

    login_page.wait_button_login()
    time.sleep(2)

    login_page.click_button_login()

    return login_page

@allure.step("Переход в личный кабинет")
def go_to_personal_account(browser):
    home_page = HomePage(browser)
    home_page.wait_button_personal_account()
    home_page.click_button_personal_account()

@allure.step("Переход в историю заказов")
def go_to_orders_history(browser):
    profile_page = ProfilePage(browser)
    profile_page.wait_orders_button()
    profile_page.click_orders_button()

@allure.step("Переход в конструктор")
def go_to_constructor(browser):
    profile_page = HomePage(browser)
    profile_page.wait_button_constructor()
    profile_page.click_button_constructor()
    return profile_page

@allure.step("Переход в Ленту заказов")
def go_to_order_feed(browser):
    profile_page = HomePage(browser)
    profile_page.wait_button_order_feed()
    profile_page.click_button_order_feed()
    return profile_page

@allure.step("Выход из аккаунта")
def logout(browser):
    profile_page = ProfilePage(browser)
    profile_page.wait_exit_button()
    profile_page.click_exit_button()


@allure.step("Процесс создания нового заказа")
def create_order(browser):
    counter = OrderPage(browser)
    counter.wait_first_ingredient()
    counter.drag_and_drop_ingredient()
    counter.wait_button_order()
    counter.click_button_order()
    counter.wait_window_exit_order()
    time.sleep(2)
    counter.click_window_exit_order()

