from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
    
    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    def click_question(self, index):
        question_locator = MainPageLocators.QUESTIONS[index]
        self.click_element(question_locator)
    
    def get_answer_text(self, index):
        answer_locator = MainPageLocators.ANSWERS[index]
        element = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return element.text
    
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
    
    def get_current_url(self):
        return self.driver.current_url