from web_locators.locators import *


class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login):
        """Проверка перехода на "Соусы" """
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_sauces_button).click()
        
        # Verify sauces tab is active
        sauces_tab = driver.find_element(*MainPage.mn_sauces_button)
        assert "tab_tab_type_current" in sauces_tab.get_attribute("class"), "Sauces tab is not active"
        
        h_sauce = driver.find_element(*MainPage.mn_h_sauces)
        assert h_sauce.text == 'Соусы'

    def test_constructor_go_to_filling_scroll_to_filling(self, login):
        """Проверка перехода на "Начинки" """
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_filling_button).click()
        
        # Verify filling tab is active
        filling_tab = driver.find_element(*MainPage.mn_filling_button)
        assert "tab_tab_type_current" in filling_tab.get_attribute("class"), "Filling tab is not active"
        
        h_filling = driver.find_element(*MainPage.mn_h_filling)
        assert h_filling.text == 'Начинки'

    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        """Проверка перехода на "Булки" """
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_filling_button).click()
        driver.find_element(*MainPage.mn_ban_button).click()
        
        # Verify bun tab is active
        bun_tab = driver.find_element(*MainPage.mn_ban_button)
        assert "tab_tab_type_current" in bun_tab.get_attribute("class"), "Bun tab is not active"
        
        h_ban = driver.find_element(*MainPage.mn_h_ban)
        assert h_ban.text == 'Булки'