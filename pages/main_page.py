from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage(BasePage):
    
    @allure.step("Клик по кнопке 'Заказать' вверху страницы")
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
    
    @allure.step("Клик по кнопке 'Заказать' внизу страницы")
    def click_order_button_bottom(self):
        self.wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON_BOTTOM))
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    @allure.step("Клик по вопросу №{index}")
    def click_question(self, index):
        question_locator = MainPageLocators.QUESTIONS[index]
        self.click_element(question_locator)
    
    @allure.step("Получение текста ответа на вопрос №{index}")
    def get_answer_text(self, index):
        answer_locator = MainPageLocators.ANSWERS[index]
        element = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return element.text
    
    @allure.step("Клик по логотипу 'Самоката'")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step("Клик по логотипу 'Яндекса'")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
    
    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url
    