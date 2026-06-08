from selenium.webdriver.common.by import By



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
    
    BODY_CLICK = (By.TAG_NAME, 'body')

    COLOR_BLACK = (By.ID, 'black')
    COLOR_GREY = (By.ID, 'grey')

    @staticmethod
    def get_metro_station_option(station_name):
        return (By.XPATH, f'.//div[text()="{station_name}"]')
    
    @staticmethod
    def get_rental_period_option(period_text):
        return (By.XPATH, f'.//div[text()="{period_text}"]')