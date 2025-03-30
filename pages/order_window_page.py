import time
from pages.base_page import BasePage
from locators.order_window_locators import OrderWindowLocators
import allure


class OrderWindowPage(BasePage):
    @allure.step("Ждем загрузку последнего заказа в ленте заказов")
    def wait_last_order(self):
        self.wait_for_element(OrderWindowLocators.first_order)

    @allure.step("Нажимаем на последний заказ в ленте заказов")
    def click_last_order(self):
        return self.click_element(OrderWindowLocators.first_order)

    @allure.step("Ждем загрузку окна с заказом")
    def wait_window_order(self):
        return self.wait_for_element(OrderWindowLocators.window_order)

    @allure.step("Ждем загрузку счетчика заказов за все время")
    def wait_counter_value(self):
        return self.wait_for_element(OrderWindowLocators.order_number)

    @allure.step("Получаем текущее значение счетчика заказов")
    def get_initial_counter_value_old(self):
        return int(self.get_text_from_element(OrderWindowLocators.order_number))

    @allure.step("Получаем значение счетчика заказов после нового заказа")
    def get_initial_counter_value_now(self):
        return int(self.get_text_from_element(OrderWindowLocators.order_number))

    @allure.step("Ждем загрузку счетчика заказов за сегодня")
    def wait_counter_value_today(self):
        return self.wait_for_element(OrderWindowLocators.order_number_today)

    @allure.step("Получаем текущее значение счетчика заказов за сегодня")
    def get_initial_counter_value_old_today(self):
        return int(self.get_text_from_element(OrderWindowLocators.order_number_today))

    @allure.step("Получаем значение счетчика заказов за сегодня после нового заказа")
    def get_initial_counter_value_now_today(self):
        return int(self.get_text_from_element(OrderWindowLocators.order_number_today))

    @allure.step("Ждем загрузку номера заказа В работе")
    def wait_counter_value_work(self):
        time.sleep(2)
        return self.wait_for_element(OrderWindowLocators.number_new_order_work)

    @allure.step("Получаем текущее значение заказа В работе")
    def get_order_number_work(self):
        try:
            self.find_element(OrderWindowLocators.number_new_order_work)
            order_number_text = self.get_text_from_element(OrderWindowLocators.number_new_order_work)
            while not order_number_text.isdigit():
                time.sleep(0.5)
                order_number_text = self.get_text_from_element(OrderWindowLocators.number_new_order_work)
            return int(order_number_text)
        except Exception as e:
            raise RuntimeError(f"Ошибка при получении номера заказа: {str(e)}")


    @allure.step("Получаем номер заказа из истории заказов")
    def get_order_number_history(self):
        try:
            order_number_element = self.find_element(OrderWindowLocators.number_order_last)
            order_number_text = order_number_element.text
            order_number = order_number_text.lstrip('#')
            return int(order_number)
        except ValueError:
            raise ValueError(f"Невозможно преобразовать в число: stroky")

    @allure.step("Ждем номер заказа из истории заказов")
    def wait_order_number_history(self):
        self.wait_for_element(OrderWindowLocators.number_order_last)
