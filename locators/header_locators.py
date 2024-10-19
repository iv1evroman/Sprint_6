from selenium.webdriver.common.by import By


class HeaderLocators:
    SCOOTER_LOGO_BUTTON = By.XPATH, './/img[@alt ="Scooter"]'
    YANDEX_LOGO_BUTTON = By.XPATH, './/img[@alt ="Yandex"]'
    SEARCH_BUTTON_ON_DZEN_PAGE = By.XPATH, './/button[contains(text(),"Найти")]'
    UPPER_ORDER_BUTTON = By.CLASS_NAME, 'Button_Button__ra12g'
