from pages.base_page import BasePage
from pages.locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class OrderPage(BasePage):

    def fill_personal_info(self, name, last_name, address, metro, phone):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)

        self.click_element(OrderPageLocators.METRO_STATION)
    
        station_locator = (By.XPATH, f'.//div[text()="{metro}"]')
        self.wait.until(EC.element_to_be_clickable(station_locator))
    
        self.click_element(station_locator)

        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_rent_info(self, date, rental_period, color, comment=None):
        self.send_keys(OrderPageLocators.DATE_INPUT, date)

        time.sleep(0.5)
        self.driver.find_element(By.TAG_NAME, 'body').click()
        time.sleep(0.5)

        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.RENTAL_PERIOD_OPTION))
        
        period_locator = (By.XPATH, f'.//div[text()="{rental_period}"]')
        self.click_element(period_locator)

        if color == 'black':
            self.click_element(OrderPageLocators.COLOR_BLACK)
        elif color == 'grey':
            self.click_element(OrderPageLocators.COLOR_GREY)

        if comment:
            self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

        self.click_element(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    def get_success_message(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)