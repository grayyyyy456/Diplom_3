import time
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.recover_password_page import RecoverPasswordPage
import allure
from curl import url_recover_password



class TestRecoverPassword:
    @allure.title("Проверка нажатия на кнопку 'Войти в аккаунт' и перехода на страницу восстановления пароля")
    def test_go_password_recovery_page(self, browser):
        home_page = HomePage(browser)
        login_page = LoginPage(browser)
        recover_page = RecoverPasswordPage(browser)

        home_page.wait_button_login()
        time.sleep(1)
        home_page.click_button_login()
        recover_page.click_recover_password_button()

        assert login_page.get_current_url() == url_recover_password

    @allure.title("Проверка ввода почты и клик по кнопку 'Восстановить'")
    def test_recover_password_process(self, browser):
        home_page = HomePage(browser)
        recover_page = RecoverPasswordPage(browser)
        home_page.wait_button_login()
        time.sleep(1)
        home_page.click_button_login()
        recover_page.click_recover_password_button()
        recover_page.filling_email_field()
        recover_page.click_restore_button()

        assert recover_page.wait_save_button().is_displayed()

    @allure.title("Проверка клика по иконке 'глаз' в поле 'Пароль'")
    def test_password_visibility_toggle(self, browser):
        home_page = HomePage(browser)
        recover_page = RecoverPasswordPage(browser)

        home_page.wait_button_login()
        time.sleep(1)
        home_page.click_button_login()
        recover_page.find_password()
        recover_page.click_glass_password()

        assert recover_page.wait_password_active().is_displayed()