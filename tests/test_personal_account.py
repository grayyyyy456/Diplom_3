import allure
from curl import url_personal_account, url_order_history, url_login
from pages.home_page import HomePage
from pages.profile_page import ProfilePage


class TestPersonalAccount:
    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_click_personal_account_after_authorization(self, browser, perform_login): # Хром работает, мозила без слипа нет
        login_page = perform_login
        home = HomePage(browser)
        home.wait_button_personal_account()
        home.click_button_personal_account()
        login_page.wait_load_page(url_personal_account)
        assert login_page.get_current_url() == url_personal_account

    @allure.title("Проверка переход в раздел «История заказов»")
    def test_click_orders_history(self, browser, perform_login):  # Хром работает, мозила без слипа нет
        login_page = perform_login
        home = HomePage(browser)
        home.wait_button_personal_account()
        home.click_button_personal_account()
        profile_page = ProfilePage(browser)
        profile_page.wait_orders_button()
        profile_page.click_orders_button()
        login_page.wait_load_page(url_order_history)
        assert login_page.get_current_url() == url_order_history

    @allure.title("Проверка выхода из аккаунта")
    def test_logout(self, browser, perform_login):  # Убрал слипы, хром работает, мозила нет
        login_page = perform_login
        home = HomePage(browser)
        home.wait_button_personal_account()
        home.click_button_personal_account()
        profile_page = ProfilePage(browser)
        profile_page.wait_exit_button()
        profile_page.click_exit_button()
        login_page.wait_load_page(url_login)
        assert login_page.get_current_url() == url_login
