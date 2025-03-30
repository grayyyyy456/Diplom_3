import allure
from curl import home_page, url_feed
from pages.order_page import OrderPage
from pages.home_page import HomePage


class TestMainFunctionality:
    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_click_constructor(self, browser):
        constructor = HomePage(browser)
        constructor.wait_button_personal_account()
        constructor.click_button_personal_account()
        constructor.wait_button_constructor()
        constructor.click_button_constructor()
        constructor.wait_load_page(home_page)
        assert constructor.get_current_url() == home_page

    @allure.title("Проверка перехода по клику на «Лента Заказов»")
    def test_click_order_feed(self, browser):
        constructor = HomePage(browser)
        constructor.wait_button_order_feed()
        constructor.click_button_order_feed()
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
        window.wait_exit_to_disappear()
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
    def test_authorized_user_can_place_order(self, browser, perform_login):  # Без слипа хром работает, мозила нет
        order = OrderPage(browser)
        order.wait_first_ingredient()
        order.drag_and_drop_ingredient()
        order.wait_button_order()
        order.click_button_order()
        window = order.wait_order_window()
        assert window.is_displayed()
