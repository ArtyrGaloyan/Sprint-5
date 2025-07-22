import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from web_locators.locators import *
from data.urls import Urls
from data.data import ValidData


class TestStellarBurgersRegistration:

    def test_registration_correct_email_and_pwd_successful_registration(self, driver):
        """При успешной регистрации перебрасывает на страницу входа"""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys(ValidData.user_name)
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(ValidData.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(ValidData.password)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(AuthLogin.al_element_with_login_text))

        login_button = driver.find_element(*AuthLogin.al_element_with_login_text)
        assert driver.current_url == Urls.url_login and login_button.text == 'Вход'

    def test_registration_empty_name_nothing_happens(self, driver):
        """ При пустом поле Имя ничего не происходит: ошибки и перехода на страницу входа нет """
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_email_field).send_keys('Артур@yan.ru')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('1234567')

        register_button = driver.find_element(*AuthRegistre.ar_register_button)
        register_button.click()
        
        WebDriverWait(driver, 5).until(
            lambda d: d.current_url == Urls.url_register
        )
        
        errors_messages = driver.find_elements(*AuthRegistre.ar_error_message)
        assert len(errors_messages) == 0

    @pytest.mark.parametrize('email_list', ['Артур@yanru', 'Артур.ru', 'Арт у р@yan.ru', 'Артур@ya n.ru',
                                            '@yan.ru', 'Артур@.ru', 'Артур@yan.'])
    def test_registration_incorrect_email_show_error(self, driver, email_list):
        """ При некорректном email появляется ошибка, что пользователь уже существует """
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys('Артур Галоян')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(email_list)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys('123456')

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthRegistre.ar_error_message_2))
        error_message = driver.find_element(*AuthRegistre.ar_error_message_2)

        assert error_message.text == 'Такой пользователь уже существует'

    @pytest.mark.parametrize('password_list', ['1', '12345'])
    def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password_list):
        """При вводе некорректного пароля, отображает ошибку 'Некорректный пароль'"""
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys('Артур Галоян')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys('Артур@yan.ru')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(password_list)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthRegistre.ar_error_message))
        error_message = driver.find_element(*AuthRegistre.ar_error_message)

        assert error_message.text == 'Некорректный пароль'