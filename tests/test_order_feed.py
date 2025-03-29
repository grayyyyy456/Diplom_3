import allure
from helper import perform_login, go_to_constructor, go_to_order_feed, create_order, go_to_orders_history, go_to_personal_account
from pages.order_page import OrderPage
from pages.order_window_page import OrderWindowPage
import time


class TestOrderFeed:
    @allure.title("Проверка если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order(self, browser):
        order = OrderWindowPage(browser)
        go_to_order_feed(browser)
        order.wait_last_order()
        order.click_last_order()
        window = order.wait_window_order()
        assert window.is_displayed()

    @allure.title("Проверка, что заказ пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_list(self, browser):
        perform_login(browser)
        order_window_page = OrderWindowPage(browser)
        create_order(browser)
        go_to_personal_account(browser)
        go_to_orders_history(browser)
        time.sleep(2)
        order_number = order_window_page.get_order_number_history()
        go_to_order_feed(browser)
        time.sleep(2)
        order_list = order_window_page.get_order_number_history()
        assert order_number == order_list

    @allure.title("Проверка при создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_increase_order_counter(self, browser):
        perform_login(browser)
        counter = OrderWindowPage(browser)
        go_to_order_feed(browser)
        counter.wait_counter_value()
        old_counter_value = counter.get_initial_counter_value_old()
        go_to_constructor(browser)
        create_order(browser)
        go_to_order_feed(browser)
        counter.wait_counter_value()
        new_counter_value = counter.get_initial_counter_value_now()
        assert old_counter_value < new_counter_value

    @allure.title("Проверка при создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_increase_order_counter_today(self, browser):
        perform_login(browser)
        counter = OrderWindowPage(browser)
        go_to_order_feed(browser)
        counter.wait_counter_value_today()
        old_counter_value = counter.get_initial_counter_value_old_today()
        go_to_constructor(browser)
        create_order(browser)
        go_to_order_feed(browser)
        counter.wait_counter_value_today()
        new_counter_value = counter.get_initial_counter_value_now_today()
        assert old_counter_value < new_counter_value

    @allure.title("Проверка после оформления заказа его номер появляется в разделе В работе")
    def test_after_order_number_in_work(self, browser):
        perform_login(browser)
        counter = OrderPage(browser)
        today = OrderWindowPage(browser)
        counter.wait_first_ingredient()
        counter.drag_and_drop_ingredient()
        counter.wait_button_order()
        counter.click_button_order()
        counter.wait_order_number_new()
        time.sleep(4)
        order_new = counter.get_order_number_new()
        counter.wait_window_exit_order()
        time.sleep(1)
        counter.click_window_exit_order()
        go_to_order_feed(browser)
        today.wait_counter_value_work()
        time.sleep(4)
        order_work = today.get_order_number_work()
        assert order_new == order_work

