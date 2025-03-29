from selenium.webdriver.common.by import By


class OrderLocators:
    window_first_ingredient = (By.XPATH,"//h2[contains(@class, 'Modal_modal__title__') and text()='Детали ингредиента']")  # Всплывающее окно первого ингредиента
    window_exit = (By.CSS_SELECTOR,".Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")  # Крестик закрытия окна с деталями заказа
    order_button = (By.XPATH, './/button[text()="Оформить заказ"]')  # Кнопка 'Оформить заказ'
    order_window = (By.XPATH,"//p[contains(@class, 'undefined') and text()='Ваш заказ начали готовить']")  # Окно после оформления заказа
    window_exit_order = (By.XPATH,"//button[contains(@class, 'Modal_modal__close_') and @type='button']")  # Крестик закрытия окна после заказа
    number_new_order = (By.XPATH,"//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'Modal_modal__title__2L34m')]")  # Номер заказа после его оформления
    first_ingredient = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient__1TVf6")]')  # Первый ингредиент- булочка
    quantity_first = (By.XPATH,"//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')][1]//p[contains(@class, 'counter_counter__num__3nue1')]")  # Счетчик сколько добавили соуса
    order_field = (By.CSS_SELECTOR, "ul[class^='BurgerConstructor_basket__list']")  # Поле для перетаскивания ингредиентов
