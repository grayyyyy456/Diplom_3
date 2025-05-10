from selenium.webdriver.common.by import By


class LoginPageLocators:
    email_field_login = (By.CSS_SELECTOR, 'input[type="text"].text.input__textfield.text_type_main-default')  # Поле емейл для авторизации
    password_field_login = (By.CSS_SELECTOR, 'input[type="password"].text.input__textfield.text_type_main-default')  # Поле пароль для авторизации
    button_login = (By.XPATH, './/button[text()="Войти"]')  #  Кнопка 'Войти' на странице авторизации


