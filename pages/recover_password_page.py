from pages.base_page import BasePage
from locators.recover_password_page_locators import RecoverPasswordPageLocators
import allure
import database

class RecoverPasswordPage(BasePage):

    @allure.step("Заполняем поле 'email' для восстановления пароля")
    def filling_email_field(self):
        self.wait_for_element(RecoverPasswordPageLocators.field_email, timeout=10)
        email_field = self.find_element(RecoverPasswordPageLocators.field_email)
        email_field.click()
        email_field.send_keys(database.email)

    @allure.step("Кликаем на кнопку 'Восстановить'")
    def click_restore_button(self):
        self.click_element(RecoverPasswordPageLocators.restore_button)

    @allure.step("Ждем загрузку кнопки 'Сохранить'")
    def wait_save_button(self):
        return self.wait_for_element(RecoverPasswordPageLocators.save_button)

    @allure.step("Ищем поле 'Пароль'")
    def find_password(self):
        self.wait_for_element(RecoverPasswordPageLocators.field_password)

    @allure.step("Ждем загрузку поля 'Пароль' после фокуса")
    def wait_password_active(self):
        return self.wait_for_element(RecoverPasswordPageLocators.field_password_active)

    @allure.step("Кликаем на значок глаза в поле 'Пароль'")
    def click_glass_password(self):
        self.find_element(RecoverPasswordPageLocators.glass_button)
        self.click_element(RecoverPasswordPageLocators.glass_button)

    @allure.step("Кликаем на кнопку 'Восстановить пароль'")
    def click_recover_password_button(self):
        self.click_element(RecoverPasswordPageLocators.recover_password)

