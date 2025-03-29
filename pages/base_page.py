from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from locators.order_locators import OrderLocators



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ожидание загрузки элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Кликаем на элемент")
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Ищем элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Получаем url на котором находимся")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ждем загрузку страницы")
    def wait_load_page(self, url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step("Получаем текст из элемента")
    def get_text_from_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Перетаскиваем ингредиент в заказ")
    def drag_and_drop_ingredient(self):
        ingredient_element = self.find_element(OrderLocators.first_ingredient)
        target_element = self.find_element(OrderLocators.order_field)

        js_script = """
        function simulateDragDrop(sourceNode, destinationNode) {
            var EVENT_TYPES = {
                DRAG_START: 'dragstart',
                DRAG_ENTER: 'dragenter',
                DRAG_OVER: 'dragover',
                DROP: 'drop',
                DRAG_END: 'dragend'
            };

            function dispatchEvent(node, type) {
                var event = new Event(type, { bubbles: true, cancelable: true });
                node.dispatchEvent(event);
            }

            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START);
            dispatchEvent(destinationNode, EVENT_TYPES.DRAG_ENTER);
            dispatchEvent(destinationNode, EVENT_TYPES.DRAG_OVER);
            dispatchEvent(destinationNode, EVENT_TYPES.DROP);
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END);
        }

        simulateDragDrop(arguments[0], arguments[1]);
        """

        self.driver.execute_script(js_script, ingredient_element, target_element)
