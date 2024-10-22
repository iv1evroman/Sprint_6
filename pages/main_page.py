from pages.base_page import BasePage
from locators.main_page_locators import (MainPageLocators)
from locators.header_locators import HeaderLocators
import allure


class MainPage(BasePage):
    @allure.step('Открываем главную страницу и закрываем сообщение про куки')
    def open_main_page_and_close_cookie_message(self):
        self.get_main_page()
        self.click_to_element(MainPageLocators.COOKIE_LOCATOR)

    @allure.step('Открываем страницу заказа нажав на верхню кнопку "Заказать"')
    def get_order_page_by_clicking_upper_order_page(self):
        self.get_main_page()
        self.click_to_element(MainPageLocators.COOKIE_LOCATOR)
        self.click_to_element(HeaderLocators.UPPER_ORDER_BUTTON)

    @allure.step('Открываем страницу заказа нажав на нижнюю кнопку "Заказать"')
    def get_order_page_by_clicking_lower_order_page(self):
        self.get_main_page()
        self.click_to_element(MainPageLocators.COOKIE_LOCATOR)
        self.scroll_to_element(MainPageLocators.QUESTIONS_HEADER_LOCATOR)
        self.find_element_with_wait(MainPageLocators.LOWER_ORDER_BUTTON)
        self.click_to_element(MainPageLocators.LOWER_ORDER_BUTTON)

    @allure.step('Переходим на страницу заказа и нажимаем на лого самоката чтобы вернутся на главную страницу и'
                 ' получаем текст заголовка главной страницы для проверки')
    def clicking_to_scooter_logo_and_getting_main_page_header(self):
        self.open_main_page_and_close_cookie_message()
        self.click_to_element(HeaderLocators.UPPER_ORDER_BUTTON)
        self.click_to_element(HeaderLocators.SCOOTER_LOGO_BUTTON)
        return self.get_text_from_element(MainPageLocators.HOME_PAGE_HEADER)

    @allure.step('Открываем главную страницу, нажимаем на лого яндекса и переходим на страницу дзена в новой вкладке'
                 ' где для проверки получаем текст с кнопки "Найти"')
    def clicking_to_yandex_logo_and_getting_search_button_text(self):
        self.open_main_page_and_close_cookie_message()
        self.click_to_element(HeaderLocators.YANDEX_LOGO_BUTTON)
        self.switch_to_new_page()
        self.find_element_with_wait(HeaderLocators.SEARCH_BUTTON_ON_DZEN_PAGE)
        return self.get_text_from_element(HeaderLocators.SEARCH_BUTTON_ON_DZEN_PAGE)

    @allure.step('Получаем текст с ответа')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_8)
        self.find_element_with_wait(locator_q_formatted)
        self.click_to_element(locator_q_formatted)
        self.find_element_with_wait(locator_a_formatted)
        return self.get_text_from_element(locator_a_formatted)



