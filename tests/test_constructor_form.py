from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_locators.locators import *

class TestStellarBurgersConstructorSections:
    """Тесты разделов конструктора бургеров"""

    def test_switch_to_buns_section(self, driver):
        """Проверка перехода к разделу 'Булки'"""
        driver.get(Urls.url_main_page)
        
        # Переходим сначала в другой раздел
        driver.find_element(*ConstructorPage.sauces_section).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPage.active_section)
        )
        
        # Переход в раздел "Булки"
        driver.find_element(*ConstructorPage.buns_section).click()
        
        # Проверка активного раздела
        active_section = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPage.active_section)
        )
        assert active_section.text == 'Булки', "Раздел 'Булки' не стал активным"

    def test_switch_to_sauces_section(self, driver):
        """Проверка перехода к разделу 'Соусы'"""
        driver.get(Urls.url_main_page)
        
        # Переход в раздел "Соусы"
        driver.find_element(*ConstructorPage.sauces_section).click()
        
        # Проверка активного раздела
        active_section = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPage.active_section)
        )
        assert active_section.text == 'Соусы', "Раздел 'Соусы' не стал активным"

    def test_switch_to_toppings_section(self, driver):
        """Проверка перехода к разделу 'Начинки'"""
        driver.get(Urls.url_main_page)
        
        # Переход в раздел "Начинки"
        driver.find_element(*ConstructorPage.toppings_section).click()
        
        # Проверка активного раздела
        active_section = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPage.active_section)
        )
        assert active_section.text == 'Начинки', "Раздел 'Начинки' не стал активным"