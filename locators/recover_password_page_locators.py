from selenium.webdriver.common.by import By


class RecoverPasswordPageLocators:
    recover_password = (By.XPATH, './/a[@href="/forgot-password"]')  # Кнопка 'Восстановить пароль'

    field_email = (By.CSS_SELECTOR, ".text.input__textfield.text_type_main-default")  # Поле 'email' для восстановления пароля
    field_email_active = (By.CSS_SELECTOR,'.input.pr-6.pl-6.input_type_text.input_size_default.input_status_active')  # Поле 'email' подсвечивается
    restore_button = (By.XPATH, './/button[text()="Восстановить"]')  # Кнопка 'Восстановить'
    placeholder_code = (By.CSS_SELECTOR, '.input.pr-6.pl-6.input_type_text.input_size_default')  # Поле для заполнения ответа из письма
    save_button = (By.XPATH, './/button[text()="Сохранить"]')  # Кнопка 'Сохранить'

    field_password = (By.CSS_SELECTOR, 'input[type="password"].text.input__textfield.text_type_main-default')  # Поле пароля
    field_password_active = (By.CSS_SELECTOR, 'input[type="text"].text.input__textfield.text_type_main-default')  # Поле пароля после фокуса
    glass_button = (By.CSS_SELECTOR,'.input__icon.input__icon-action')  # Кнопка глаза в поле пароль