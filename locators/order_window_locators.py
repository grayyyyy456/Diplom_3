from selenium.webdriver.common.by import By


class OrderWindowLocators:
    first_order = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_list')]//li[contains(@class, 'OrderHistory_listItem')])[1]")  # Первый заказ в Ленте заказов
    order_number = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ') and contains(@class, 'text_type_digits-large')])[1]")  # Счетчик заказов за все время
    order_number_today = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ') and contains(@class, 'text_type_digits-large')])[2]")  # Счетчик заказов за сегодня
    number_new_order_work = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li)[1]")  # Номер заказа в работе в ленте заказов
    window_order = (By.XPATH, "//p[contains(@class, 'text_type_main-default') and contains(text(), 'Выполнен')]")  # Страница заказов
    list_orders_history = (By.CSS_SELECTOR, "ul.OrderHistory_profileList__374GU.OrderHistory_list__KcLDB li")  # Список заказов в истории заказов
    number_order = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_list')]//li[contains(@class, 'OrderHistory_listItem')])")  # Последний заказ
    number_order_last = (By.XPATH, '//p[@class="text text_type_digits-default"]')  # Номер последнего заказа



