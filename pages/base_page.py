from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from data import Urls


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
    
    @allure.step("Проверка, отображается ли элемент: {locator}")
    def is_element_displayed(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()
    
    @allure.step("Переключение на новую вкладку")
    def switch_to_new_tab(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        WebDriverWait(self.driver, 5).until(EC.url_contains(Urls.DZEN_PAGE))
    
    @allure.step("Закрыть текущую вкладку и вернуться на предыдущую")
    def close_current_tab_and_go_back(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])