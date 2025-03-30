from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):

    @allure.step("Заполняем поле 'email' для входа")
    def filling_email_field_login(self, email):
        self.wait_for_element(LoginPageLocators.email_field_login, timeout=10)
        email_field = self.find_element(LoginPageLocators.email_field_login)
        email_field.click()
        email_field.send_keys(email)

    @allure.step("Заполняем поле 'пароль' для входа в аккаунт")
    def filling_password_field_login(self, password):
        self.wait_for_element(LoginPageLocators.password_field_login, timeout=10)
        password_field = self.find_element(LoginPageLocators.password_field_login)
        password_field.click()
        password_field.send_keys(password)

    @allure.step("Ждем загрузку кннопки 'Войти'")
    def wait_button_login(self):
        self.wait_for_element(LoginPageLocators.button_login)

    @allure.step("Кликаем на кнопку 'Войти'")
    def click_button_login(self):
        self.click_element(LoginPageLocators.button_login)
