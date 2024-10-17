from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import (OrderPageLocators)
import allure
from helpers import Helpers


class OrderPage(BasePage):
    @allure.step('Открываем страницу заказа нажав на верхню кнопку "Заказать"')
    def get_order_page_by_clicking_upper_order_page(self):
        self.get_main_page()
        self.click_to_element(MainPageLocators.COOKIE_LOCATOR)
        self.click_to_element(MainPageLocators.UPPER_ORDER_BUTTON)
        return self.get_text_from_element(OrderPageLocators.ORDER_PAGE_HEADER_LOCATOR)

    @allure.step('Открываем страницу заказа нажав на нижнюю кнопку "Заказать"')
    def get_order_page_by_clicking_lower_order_page(self):
        self.get_main_page()
        self.click_to_element(MainPageLocators.COOKIE_LOCATOR)
        self.scroll_to_element(MainPageLocators.QUESTIONS_HEADER_LOCATOR)
        self.find_element_with_wait(MainPageLocators.LOWER_ORDER_BUTTON)
        self.click_to_element(MainPageLocators.LOWER_ORDER_BUTTON)
        return self.get_text_from_element(OrderPageLocators.ORDER_PAGE_HEADER_LOCATOR)

    @allure.step('Создаем заказ')
    def set_order(self, name, last_name, address, day):
        self.click_to_element(OrderPageLocators.STATION_INPUT_LOCATOR)
        self.click_to_element(OrderPageLocators.STATION_LOCATOR)
        self.add_text_to_element(OrderPageLocators.NAME_INPUT_LOCATOR, name)
        self.add_text_to_element(OrderPageLocators.LAST_NAME_INPUT_LOCATOR, last_name)
        self.add_text_to_element(OrderPageLocators.ADRESS_INPUT_LOCATOR, address)
        self.add_text_to_element(OrderPageLocators.PHONE_INPUT_LOCATOR, Helpers.random_phone_number(self))
        self.click_to_element(OrderPageLocators.NEXT_PAGE_BUTTON_LOCATOR)
        self.add_text_to_element(OrderPageLocators.DELIVERY_DAY_INPUT_LOCATOR, day)
        self.click_to_element(OrderPageLocators.DURATION_CHOICE_LOCATOR)
        self.click_to_element(OrderPageLocators.ONE_DAY_LOCATOR)
        self.click_to_element(OrderPageLocators.COLOR_CHECKBOX_LOCATOR)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_LOCATOR)
        self.click_to_element(OrderPageLocators.CONFIRMATION_BUTTON_LOCATOR)

    @allure.step('Проверяем, что заказ создался')
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_CONFIRMATION_TEXT_LOCATOR)