from selenium.webdriver.common.by import By



class MainPageLocators:
    
    ORDER_BUTTON_TOP = (By.XPATH, './/button[@class="Button_Button__ra12g" and text()="Заказать"]') # Кнопка "Заказать" вверху страницы
    ORDER_BUTTON_BOTTOM = (By.XPATH, '(//button[text()="Заказать"])[2]') # Кнопка "Заказать" внизу страницы

    # Список вопросов в разделе "Вопросы о важном"
    QUESTIONS = [
        (By.ID, 'accordion__heading-0'),
        (By.ID, 'accordion__heading-1'),
        (By.ID, 'accordion__heading-2'),
        (By.ID, 'accordion__heading-3'),
        (By.ID, 'accordion__heading-4'),
        (By.ID, 'accordion__heading-5'),
        (By.ID, 'accordion__heading-6'),
        (By.ID, 'accordion__heading-7'),
    ]
    
    # Список ответов в разделе "Вопросы о важном"
    ANSWERS = [
        (By.XPATH, './/div[@id="accordion__panel-0"]/p'),
        (By.XPATH, './/div[@id="accordion__panel-1"]/p'),
        (By.XPATH, './/div[@id="accordion__panel-2"]/p'),
        (By.XPATH, './/div[@id="accordion__panel-3"]/p'),
        (By.XPATH, './/div[@id="accordion__panel-4"]/p'),
        (By.XPATH, './/div[@id="accordion__panel-5"]/p'),
        (By.XPATH, './/div[@id="accordion__panel-6"]/p'),
        (By.XPATH, './/div[@id="accordion__panel-7"]/p'),
    ]
    
    SCOOTER_LOGO = (By.XPATH, './/img[@alt="Scooter"]') # Логотип "Самоката"
    YANDEX_LOGO = (By.XPATH, './/img[@alt="Yandex"]') # Логотип "Яндекса" 

