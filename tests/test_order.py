import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA_1, ORDER_DATA_2



class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката через кнопку вверху")
    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
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
            order_data["color"],
            order_data["comment"]
        )
        order_page.confirm_order()
        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message

    @allure.title("Позитивный сценарий заказа самоката через кнопку внизу")
    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
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
            order_data["color"],
            order_data["comment"]
        )
        order_page.confirm_order()
        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message
