import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import *
from data.urls import Urls
from data.data import ValidData


class TestStellarBurgersRegistration:
    """Тесты регистрации в Stellar Burgers (адаптировано для Артура Галояна)"""

    def test_registration_correct_email_and_pwd_successful_registration(self, driver):
        """Успешная регистрация с корректными данными - переход на страницу входа"""
        driver.get(Urls.url_register)

        # Ввод данных для регистрации
        driver.find_element(*AuthRegistre.ar_name_field).send_keys("Галоян Артур")
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(ValidData.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(ValidData.password)

        # Нажатие кнопки регистрации
        driver.find_element(*AuthRegistre.ar_register_button).click()
        
        # Ожидание перехода на страницу входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AuthLogin.al_element_with_login_text),
            message="Не произошел переход на страницу входа после регистрации"
        )

        # Проверки
        login_button = driver.find_element(*AuthLogin.al_element_with_login_text)
        assert driver.current_url == Urls.url_login, "URL не соответствует странице входа"
        assert login_button.text == 'Вход', "Не найдена кнопка 'Вход' на странице"

    def test_registration_empty_name_field_validation(self, driver):
        """Валидация поля 'Имя' - нельзя зарегистрироваться без имени"""
        driver.get(Urls.url_register)

        # Заполнение всех полей кроме имени
        driver.find_element(*AuthRegistre.ar_email_field).send_keys('artur_g@example.com')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('123456')
        
        # Попытка регистрации
        driver.find_element(*AuthRegistre.ar_register_button).click()
        
        # Явное ожидание и проверка, что остаемся на той же странице
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(AuthRegistre.ar_register_button),
            message="Кнопка регистрации не кликабельна"
        )
        
        # Проверка URL и отсутствия сообщений об ошибке
        assert driver.current_url == Urls.url_register, "Произошел переход со страницы регистрации"
        errors = driver.find_elements(*AuthRegistre.ar_error_message)
        assert len(errors) == 0, "Обнаружены неожиданные сообщения об ошибке"

    @pytest.mark.parametrize('invalid_email', [
        'artur@example',          # отсутствует домен верхнего уровня
        'artur.example.com',      # отсутствует @
        'artur @example.com',     # пробел в email
        'artur@exa mple.com',     # пробел в домене
        '@example.com',           # отсутствует имя пользователя
        'artur@.com',            # отсутствует домен
        'artur@example.'          # отсутствует TLD
    ], ids=[
        'missing TLD', 
        'missing @', 
        'space before @', 
        'space in domain', 
        'missing username', 
        'missing domain', 
        'missing TLD after dot'
    ])
    def test_registration_invalid_email_formats(self, driver, invalid_email):
        """Проверка валидации некорректных форматов email"""
        driver.get(Urls.url_register)

        # Заполнение формы с невалидными email
        driver.find_element(*AuthRegistre.ar_name_field).send_keys("Галоян Артур")
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(invalid_email)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('123456')

        driver.find_element(*AuthRegistre.ar_register_button).click()
        
        # Проверка сообщения об ошибке
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(AuthRegistre.ar_error_message_2),
            message="Не появилось сообщение об ошибке для невалидного email"
        )
        
        error = driver.find_element(*AuthRegistre.ar_error_message_2)
        assert error.text == 'Такой пользователь уже существует', "Неверное сообщение об ошибке"

    @pytest.mark.parametrize('short_password', ['1', '12', '123', '1234', '12345'], 
                            ids=['1 symbol', '2 symbols', '3 symbols', '4 symbols', '5 symbols'])
    def test_short_password_validation(self, driver, short_password):
        """Проверка валидации короткого пароля (менее 6 символов)"""
        driver.get(Urls.url_register)

        # Заполнение формы с коротким паролем
        driver.find_element(*AuthRegistre.ar_name_field).send_keys("Галоян Артур")
        driver.find_element(*AuthRegistre.ar_email_field).send_keys('artur_g@example.com')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(short_password)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        
        # Проверка сообщения об ошибке
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(AuthRegistre.ar_error_message),
            message="Не появилось сообщение об ошибке для короткого пароля"
        )
        
        error = driver.find_element(*AuthRegistre.ar_error_message)
        assert error.text == 'Некорректный пароль', "Неверное сообщение об ошибке для пароля"