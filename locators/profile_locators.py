from selenium.webdriver.common.by import By


class ProfilePageLocators:
    order_history = (By.CSS_SELECTOR, "a[href='/account/order-history']")  # Кнопка Истории заказов
    exit_button = (By.XPATH, './/button[text()="Выход"]')  # Кнопка выхода
