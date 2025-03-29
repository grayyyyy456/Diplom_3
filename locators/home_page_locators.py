from selenium.webdriver.common.by import By


class HomePageLocators:
    login_button = (By.XPATH, './/button[text()="Войти в аккаунт"]')  # Кнопка 'Войти в аккаунт' на главной странице
    personal_account = (By.CSS_SELECTOR, "a[href='/account']")   # Кнопка 'Личный кабинет' на главной странице
    recover_password = (By.XPATH, './/a[@href="/forgot-password"]')  # Кнопка 'Восстановить пароль'
    constructor_button = (By.XPATH, './/a[@href="/"]')  # Кнопка 'Конструктор'
    order_feed = (By.XPATH, './/a[@href="/feed"]')  # Кнопка 'Лента заказов'




