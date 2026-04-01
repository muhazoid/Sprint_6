import allure
import time
from pages.main_page import MainPage
from data import Urls


class TestNavigation:
    @allure.title("Логотип Самоката ведет на главную страницу")
    def test_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_top()
        main_page.click_scooter_logo()
        assert driver.current_url == Urls.SCOOTER_URL
    
    @allure.title("Логотип Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo(self, driver):
        main_page = MainPage(driver)
        old_tab = driver.current_window_handle
        main_page.click_yandex_logo()
        time.sleep(5)
        new_tab = driver.window_handles[-1]
        driver.switch_to.window(new_tab)
        assert "dzen.ru" in driver.current_url
        driver.close()
        driver.switch_to.window(old_tab)
        