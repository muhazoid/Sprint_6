from selenium.webdriver.common.by import By


# Локаторы главной страницы 
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


# Локаторы страницы заказа 
class OrderPageLocators:

    NAME_INPUT = (By.XPATH, './/input[@placeholder="* Имя"]') # Поле ввода имени
    LAST_NAME_INPUT = (By.XPATH, './/input[@placeholder="* Фамилия"]') # Поле ввода фамилии
    ADDRESS_INPUT = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]') # Поле ввода адреса
    METRO_STATION = (By.XPATH, './/input[@placeholder="* Станция метро"]') # Поле ввода станции метро
    METRO_STATION_OPTION = (By.XPATH, './/div[contains(@class, "Order_SelectOption")]')  # Варианты станций метро в выпадающем списке
    PHONE_INPUT = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]') # Поле ввода телефона
    NEXT_BUTTON = (By.XPATH, './/button[text()="Далее"]') # Кнопка "Далее" (переход к следующей форме)

    DATE_INPUT = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')  # Поле выбора даты доставки
    RENTAL_PERIOD = (By.XPATH, './/div[text()="* Срок аренды"]') # Поле выбора срока аренды
    RENTAL_PERIOD_OPTION = (By.XPATH, './/div[contains(@class, "Dropdown-option")]')# Варианты срока аренды в выпадающем списке
    COLOR_BLACK = (By.ID, 'black') # Чекбокс черного цвета самоката
    COLOR_GREY = (By.ID, 'grey') # Чекбокс серого цвета самоката
    COMMENT_INPUT = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]') # Поле для комментария курьеру
    ORDER_BUTTON = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]') # Кнопка "Заказать" в форме оформления

    CONFIRM_BUTTON = (By.XPATH, './/button[text()="Да"]') # Кнопка "Да" в модальном окне подтверждения
    SUCCESS_MESSAGE = (By.XPATH, './/div[contains(@class, "Order_ModalHeader")]') # Сообщение об успешном создании заказа