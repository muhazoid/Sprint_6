import allure
import pytest
from pages.main_page import MainPage
from locators.main_page import MainPageLocators
from data import TestData


class TestFAQ:
    @allure.title("Проверка текста ответа на вопрос №{index}")
    @pytest.mark.parametrize("index, expected_text", TestData.FAQ_DATA)
    def test_faq_answer_text(self, driver, index, expected_text):
        main_page = MainPage(driver)
        question_locator = MainPageLocators.QUESTIONS[index]
        main_page.scroll_to_element(question_locator)
        main_page.click_question(index)
        actual_text = main_page.get_answer_text(index)
        assert actual_text == expected_text
        