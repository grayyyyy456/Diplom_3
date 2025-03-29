import allure
from curl import home_page, url_feed
from helper import perform_login, go_to_personal_account, go_to_constructor, go_to_order_feed
from pages.order_page import OrderPage
import time


class TestMainFunctionality:
    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_click_constructor(self, browser):
        constructor = go_to_constructor(browser)
        go_to_personal_account(browser)
        go_to_constructor(browser)
        constructor.wait_load_page(home_page)
        assert constructor.get_current_url() == home_page

    @allure.title("Проверка перехода по клику на «Лента Заказов»")
    def test_click_order_feed(self, browser):
        constructor = go_to_order_feed(browser)
        constructor.wait_load_page(url_feed)
        assert constructor.get_current_url() == url_feed

    @allure.title("Проверка, при нажатии на ингредиент, появляется окно с деталями игредиента")
    def test_window_ingredient(self, browser):
        ingredient = OrderPage(browser)
        ingredient.wait_first_ingredient()
        ingredient.click_first_ingredient()
        window = ingredient.wait_window_first_ingredient()
        assert window.is_displayed()

    @allure.title("Проверка что окно с деталями ингредиента закрывается на крестик")
    def test_exit_window(self, browser):
        window = OrderPage(browser)
        window.wait_first_ingredient()
        window.click_first_ingredient()
        button_exit = window.wait_window_first_ingredient()
        window.wait_window_exit()
        window.click_window_exit()
        time.sleep(0.5)
        assert not button_exit.is_displayed()

    @allure.title("Проверка увеличения показателя после перетаскивания элемента")
    def test_drag_and_drop_increases_value(self, browser):
        window = OrderPage(browser)
        window.wait_first_ingredient()
        initial_value = window.get_initial_counter_value()
        window.drag_and_drop_ingredient()
        new_value = window.get_new_counter_value()
        assert new_value > initial_value

    @allure.title("Проверка, что авторизированный пользователь может сделать заказ")
    def test_authorized_user_can_place_order(self, browser):
        perform_login(browser)
        order = OrderPage(browser)
        order.wait_first_ingredient()
        order.drag_and_drop_ingredient()
        order.wait_button_order()
        time.sleep(2)
        order.click_button_order()
        window = order.wait_order_window()
        assert window.is_displayed()

    




