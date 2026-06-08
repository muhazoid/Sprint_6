import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData
from locators.order_page import OrderPageLocators



class TestOrder:

    @allure.title("Заказ самоката через кнопку вверху")
    @pytest.mark.parametrize("order_data", [TestData.ORDER_DATA_1, TestData.ORDER_DATA_2])
    def test_order_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_order_button_top()
        
        order_page.fill_personal_info(
            order_data["name"],
            order_data["last_name"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )
        
        order_page.fill_rent_info(
            order_data["date"],
            order_data["rental_period"],
            OrderPageLocators.COLOR_BLACK,
            order_data["comment"]
        )
        
        order_page.confirm_order()
        assert order_page.is_order_successful()
    
    @allure.title("Заказ самоката через кнопку внизу")
    @pytest.mark.parametrize("order_data", [TestData.ORDER_DATA_1, TestData.ORDER_DATA_2])
    def test_order_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_order_button_bottom()
        
        order_page.fill_personal_info(
            order_data["name"],
            order_data["last_name"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )
        
        order_page.fill_rent_info(
            order_data["date"],
            order_data["rental_period"],
            OrderPageLocators.COLOR_GREY,
            order_data["comment"]
        )
        
        order_page.confirm_order()
        assert order_page.is_order_successful()

