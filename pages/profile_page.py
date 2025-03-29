from pages.base_page import BasePage
from locators.profile_locators import ProfilePageLocators
import allure


class ProfilePage(BasePage):
    @allure.step("Ждем загрузку кнопки 'История заказов'")
    def wait_orders_button(self):
        self.wait_for_element(ProfilePageLocators.order_history)

    @allure.step("Кликаем на кнопку 'История заказов'")
    def click_orders_button(self):
        self.click_element(ProfilePageLocators.order_history)

    @allure.step("Ждем загрузку кнопки 'Выход'")
    def wait_exit_button(self):
        self.wait_for_element(ProfilePageLocators.exit_button)

    @allure.step("Кликаем на кнопку 'Выход'")
    def click_exit_button(self):
        self.click_element(ProfilePageLocators.exit_button)