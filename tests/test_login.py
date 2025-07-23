from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_locators.locators import *
from data.urls import Urls
from data.data import PersonData

class TestStellarBurgersAuthAndNavigation:
    """Тесты авторизации и навигации для Stellar Burgers"""

    def test_login_via_main_page_button(self, driver):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        driver.get(Urls.url_main_page)
        driver.find_element(*MainPage.mn_login_button).click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthLogin.al_login_form)
        )
        
        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.valid_email)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.valid_password)
        driver.find_element(*AuthLogin.al_login_button).click()
        
        WebDriverWait(driver, 5).until(
            EC.url_to_be(Urls.url_main_page)
        )

    def test_login_via_personal_account_button(self, driver):
        """Вход через кнопку 'Личный кабинет'"""
        driver.get(Urls.url_main_page)
        driver.find_element(*MainPage.mn_profile_button).click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthLogin.al_login_form)
        )
        
        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.valid_email)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.valid_password)
        driver.find_element(*AuthLogin.al_login_button).click()
        
        WebDriverWait(driver, 5).until(
            EC.url_to_be(Urls.url_main_page)
        )

    def test_login_via_registration_form_button(self, driver):
        """Вход через кнопку в форме регистрации"""
        driver.get(Urls.url_register)
        driver.find_element(*AuthRegister.ar_login_link).click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthLogin.al_login_form)
        )
        
        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.valid_email)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.valid_password)
        driver.find_element(*AuthLogin.al_login_button).click()
        
        WebDriverWait(driver, 5).until(
            EC.url_to_be(Urls.url_main_page)
        )

    def test_login_via_password_recovery_form_button(self, driver):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(Urls.url_forgot_password)
        driver.find_element(*AuthPassword.ap_login_link).click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthLogin.al_login_form)
        )
        
        driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.valid_email)
        driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.valid_password)
        driver.find_element(*AuthLogin.al_login_button).click()
        
        WebDriverWait(driver, 5).until(
            EC.url_to_be(Urls.url_main_page)
        )

    def test_personal_account_access(self, login):
        """Переход в личный кабинет после авторизации"""
        driver = login
        driver.find_element(*MainPage.mn_profile_button).click()
        
        WebDriverWait(driver, 5).until(
            EC.url_contains(Urls.url_profile)
        )

    def test_navigate_to_constructor_via_button(self, login):
        """Переход из ЛК в конструктор через кнопку"""
        driver = login
        driver.get(Urls.url_profile)
        driver.find_element(*MainPage.mn_constructor_button).click()
        
        WebDriverWait(driver, 5).until(
            EC.url_to_be(Urls.url_main_page)
        )

    def test_navigate_to_constructor_via_logo(self, login):
        """Переход из ЛК в конструктор через логотип"""
        driver = login
        driver.get(Urls.url_profile)
        driver.find_element(*MainPage.mn_logo).click()
        
        WebDriverWait(driver, 5).until(
            EC.url_to_be(Urls.url_main_page)
        )