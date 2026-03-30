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


class OrderPageLocators:

    NAME_INPUT = (By.XPATH, './/input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION = (By.XPATH, './/input[@placeholder="* Станция метро"]')
    METRO_STATION_OPTION = (By.XPATH, './/div[contains(@class, "Order_SelectOption")]')
    PHONE_INPUT = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, './/button[text()="Далее"]')

    DATE_INPUT = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD = (By.XPATH, './/div[text()="* Срок аренды"]')
    RENTAL_PERIOD_OPTION = (By.XPATH, './/div[contains(@class, "Dropdown-option")]')
    COLOR_BLACK = (By.ID, 'black')
    COLOR_GREY = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')

    CONFIRM_BUTTON = (By.XPATH, './/button[text()="Да"]')
    SUCCESS_MESSAGE = (By.XPATH, './/div[contains(@class, "Order_ModalHeader")]')