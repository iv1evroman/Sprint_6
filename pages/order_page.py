from pages.base_page import BasePage
from locators.order_page_locators import (OrderPageLocators)
import allure
class OrderPage(BasePage):

    @allure.step('Создаем заказ')
    def set_order(self, station_locator, name_locator, name, last_name, address, time, button_locator):
        self.click_to_element(OrderPageLocators.Station_Locator)
        self.add_text_to_element(name_locator, name)
        self.add_text_to_element(last_name, last_name)
        self.add_text_to_element(address, address)
        self.click_to_element(time)
        self.click_to_element(button_locator)

    @allure.step('Проверяем, что заказ создался')
    def check_order(self, locator):
        return self.get_text_from_element(locator)