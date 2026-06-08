import allure
from pages.main_page import MainPage
from data import Urls


class TestNavigation:
    @allure.title("Логотип Самоката ведет на главную страницу")
    def test_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_top()
        main_page.click_scooter_logo()
        assert main_page.get_current_url() == Urls.SCOOTER_URL
    
    @allure.title("Логотип Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        assert "dzen.ru" in main_page.get_current_url()
        main_page.close_current_tab_and_go_back()
        