import allure
from helper import perform_login, go_to_personal_account, go_to_orders_history, logout
from curl import url_personal_account, url_order_history, url_login


class TestPersonalAccount:
    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_click_personal_account_after_authorization(self, browser):
        login_page = perform_login(browser)
        go_to_personal_account(browser)
        login_page.wait_load_page(url_personal_account)
        assert login_page.get_current_url() == url_personal_account

    @allure.title("Проверка переход в раздел «История заказов»")
    def test_click_orders_history(self, browser):
        login_page = perform_login(browser)
        go_to_personal_account(browser)
        go_to_orders_history(browser)
        login_page.wait_load_page(url_order_history)
        assert login_page.get_current_url() == url_order_history

    @allure.title("Проверка выхода из аккаунта")
    def test_logout(self, browser):
        login_page = perform_login(browser)
        go_to_personal_account(browser)
        logout(browser)
        login_page.wait_load_page(url_login)
        assert login_page.get_current_url() == url_login
