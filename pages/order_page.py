from pages.base_page import BasePage
from locators.order_locators import OrderLocators
import allure
from time import sleep


class OrderPage(BasePage):
    @allure.step("Ждем загрузку первого ингредиента")
    def wait_first_ingredient(self):
        self.wait_for_element(OrderLocators.first_ingredient)
        sleep(1)

    @allure.step("Кликаем на первый элемент")
    def click_first_ingredient(self):
        self.click_element(OrderLocators.first_ingredient)

    @allure.step("Ждем загрузку поля с информацией первого ингредиента")
    def wait_window_first_ingredient(self):
        return self.wait_for_element(OrderLocators.window_first_ingredient)

    @allure.step("Ждем загрузку крестика для закрытия окна с деталями")
    def wait_window_exit(self):
        self.wait_for_element(OrderLocators.window_exit)
        sleep(1)

    @allure.step("Нажимаем на крестик для выхода из окна с деталями ингредиента")
    def click_window_exit(self):
        return self.click_element(OrderLocators.window_exit)

    @allure.step("Получаем начальное значение счетчика ингредиента")
    def get_initial_counter_value(self):
        return int(self.get_text_from_element(OrderLocators.quantity_first))

    @allure.step("Получаем новое значение счетчика ингредиента")
    def get_new_counter_value(self):
        return int(self.get_text_from_element(OrderLocators.quantity_first))

    @allure.step("Ждем загрузку кнопки 'Оформить заказ'")
    def wait_button_order(self):
        self.wait_for_element(OrderLocators.order_button)
        sleep(1)

    @allure.step("Кликаем на кнопку 'Оформить заказ'")
    def click_button_order(self):
        self.click_element(OrderLocators.order_button)

    @allure.step("Ждем загрузку поля после оформления заказа")
    def wait_order_window(self):
        return self.wait_for_element(OrderLocators.order_window)

    @allure.step("Ждем загрузку крестика для закрытия окна после заказа")
    def wait_window_exit_order(self):
        self.wait_for_element(OrderLocators.window_exit_order)
        sleep(1)

    @allure.step("Нажимаем на крестик для выхода из окна после заказа")
    def click_window_exit_order(self):
        return self.click_element(OrderLocators.window_exit_order)

    @allure.step("Ждем загрузку номера заказа в окне после его оформления")
    def wait_order_number_new(self):
        return self.wait_for_element(OrderLocators.number_new_order)

    @allure.step("Получаем текущее значение заказа после его оформления")
    def get_order_number_new(self):
        return int(self.get_text_from_element(OrderLocators.number_new_order))