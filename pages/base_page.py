from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Поиск элемента: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввод текста '{text}' в поле: {locator}")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста из элемента: {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Скролл до элемента: {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Поиск всех элементов по локатору: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    