from pages.base_page import BasePage
from locators.order_page import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderPage(BasePage):

    @allure.step("Заполнение формы 'Для кого самокат'")
    def fill_personal_info(self, name, last_name, address, metro, phone):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)

        self.click_element(OrderPageLocators.METRO_STATION)
    
        station_locator = OrderPageLocators.get_metro_station_option(metro)
        self.wait.until(EC.element_to_be_clickable(station_locator))
    
        self.click_element(station_locator)

        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение формы 'Про аренду'")
    def fill_rent_info(self, date, rental_period, color_locator, comment=None):
        self.send_keys(OrderPageLocators.DATE_INPUT, date)

        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT))
        self.click_element(OrderPageLocators.BODY_CLICK)
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT))

        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.RENTAL_PERIOD_OPTION))
        
        period_locator = OrderPageLocators.get_rental_period_option(rental_period)
        self.click_element(period_locator)

        self.click_element(color_locator)

        if comment:
            self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    
    @allure.step("Проверка успешного оформления заказа")
    def is_order_successful(self):
        return self.is_element_displayed(OrderPageLocators.SUCCESS_MESSAGE)
    
