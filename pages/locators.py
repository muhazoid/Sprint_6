from selenium.webdriver.common.by import By


class MainPageLocators:
    
    ORDER_BUTTON_TOP = (By.XPATH, './/button[@class="Button_Button__ra12g" and text()="Заказать"]')
    ORDER_BUTTON_BOTTOM = (By.XPATH, './/button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp" and text()="Заказать"]')

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
    
    SCOOTER_LOGO = (By.XPATH, './/img[@alt="Scooter"]')
    YANDEX_LOGO = (By.XPATH, './/img[@alt="Yandex"]')