from time import sleep
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
import allure


class HomePage(BasePage):
    @allure.step("Ждем загрузку кнопки 'Войти в аккаунт'")
    def wait_button_login(self):
        self.wait_for_element(HomePageLocators.login_button)

    @allure.step("Кликаем на кнопку 'Войти в аккаунт'")
    def click_button_login(self):
        self.click_element(HomePageLocators.login_button)

    @allure.step("Ждем загрузку кнопки 'Личный аккаунт'")
    def wait_button_personal_account(self):
        self.wait_for_element(HomePageLocators.personal_account)
        sleep(1)

    @allure.step("Кликаем на кнопку 'Личный кабинет'")
    def click_button_personal_account(self):
        self.click_element(HomePageLocators.personal_account)

    @allure.step("Ждем загрузку кнопки 'Конструктор'")
    def wait_button_constructor(self):
        self.wait_for_element(HomePageLocators.constructor_button)
        sleep(1)

    @allure.step("Кликаем на кнопку 'Конструктор'")
    def click_button_constructor(self):
        self.click_element(HomePageLocators.constructor_button)

    @allure.step("Ждем загрузку кнопки 'Лента Заказов'")
    def wait_button_order_feed(self):
        self.wait_for_element(HomePageLocators.order_feed)
        sleep(1)

    @allure.step("Кликаем на кнопку 'Лента Заказов'")
    def click_button_order_feed(self):
        self.click_element(HomePageLocators.order_feed)
