import allure
from pages.order_page import OrderPage
from pages.order_window_page import OrderWindowPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage


class TestOrderFeed:
    @allure.title("Проверка если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order(self, browser):
        order = OrderWindowPage(browser)
        profile_page = HomePage(browser)
        profile_page.wait_button_order_feed()
        profile_page.click_button_order_feed()
        order.wait_last_order()
        order.click_last_order()
        window = order.wait_window_order()
        assert window.is_displayed()

    @allure.title("Проверка, что заказ пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_list(self, browser, perform_login, create_order):  # Хром работает, мозила без слипа нет
        order_window_page = OrderWindowPage(browser)
        home = HomePage(browser)
        profile_page = ProfilePage(browser)

        home.wait_button_personal_account()
        home.click_button_personal_account()
        profile_page.wait_orders_button()
        profile_page.click_orders_button()
        order_window_page.wait_order_number_history()
        order_number = order_window_page.get_order_number_history()
        home.wait_button_order_feed()
        home.click_button_order_feed()
        order_window_page.wait_order_number_history()
        order_list = order_window_page.get_order_number_history()
        assert order_number == order_list

    @allure.title("Проверка при создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_increase_order_counter(self, browser, perform_login):  # Хром работает, мозила без слипа нет
        counter = OrderWindowPage(browser)
        profile_page = HomePage(browser)
        order = OrderPage(browser)

        profile_page.wait_button_order_feed()
        profile_page.click_button_order_feed()
        counter.wait_counter_value()
        old_counter_value = counter.get_initial_counter_value_old()
        profile_page.wait_button_constructor()
        profile_page.click_button_constructor()

        order.wait_first_ingredient()
        order.drag_and_drop_ingredient()
        order.wait_button_order()
        order.click_button_order()
        order.wait_window_exit_order()
        order.click_window_exit_order()

        profile_page.wait_button_order_feed()
        profile_page.click_button_order_feed()
        counter.wait_counter_value()
        new_counter_value = counter.get_initial_counter_value_now()
        assert old_counter_value < new_counter_value

    @allure.title("Проверка при создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_increase_order_counter_today(self, browser, perform_login):  # Хром работает, мозила без слипа нет
        counter = OrderWindowPage(browser)
        profile_page = HomePage(browser)
        order = OrderPage(browser)

        profile_page.wait_button_order_feed()
        profile_page.click_button_order_feed()
        counter.wait_counter_value_today()
        old_counter_value = counter.get_initial_counter_value_old_today()
        profile_page.wait_button_constructor()
        profile_page.click_button_constructor()

        order.wait_first_ingredient()
        order.drag_and_drop_ingredient()
        order.wait_button_order()
        order.click_button_order()
        order.wait_window_exit_order()
        order.click_window_exit_order()

        profile_page.wait_button_order_feed()
        profile_page.click_button_order_feed()
        counter.wait_counter_value_today()
        new_counter_value = counter.get_initial_counter_value_now_today()
        assert old_counter_value < new_counter_value

    @allure.title("Проверка после оформления заказа его номер появляется в разделе В работе")
    def test_after_order_number_in_work(self, browser, perform_login):
        counter = OrderPage(browser)
        today = OrderWindowPage(browser)
        profile_page = HomePage(browser)

        counter.wait_first_ingredient()
        counter.drag_and_drop_ingredient()
        counter.wait_button_order()
        counter.click_button_order()
        counter.wait_order_number_new()
        order_new = counter.get_order_number_new()
        counter.wait_window_exit_order()
        counter.click_window_exit_order()
        profile_page.wait_button_order_feed()
        profile_page.click_button_order_feed()
        today.wait_counter_value_work()
        order_work = today.get_order_number_work()
        assert order_new == order_work
