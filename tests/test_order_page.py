import pytest
from pages.order_page import OrderPage
from pages.main_page import MainPage
import allure


class TestOrderPage:
    @allure.title('Проверка, что при клике на верхнюю кнопку "заказать" открывается страница заказа')
    def test_upper_order_button(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.get_order_page_by_clicking_upper_order_page()
        assert order_page.get_order_page_header_text() == 'Для кого самокат'

    @allure.title('Проверка, что при клике на нижнюю кнопку "заказать" открывается страница заказа')
    def test_lower_order_button(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.get_order_page_by_clicking_lower_order_page()
        assert order_page.get_order_page_header_text() == 'Для кого самокат'

    @allure.description('Параметризуем тестовые данные для оформления заказа')
    @pytest.mark.parametrize(
        'name, last_name, address, day',
        [
            ('Петя', 'Иванов', 'Москва', '11.11.2024'),
            ('Вася', 'Сидоров', 'Химки', '14.11.2024')
        ]
    )
    @allure.title('Тест на весь флоу успешного оформления заказа и подтверждение что он оформлен')
    def test_successful_order(self, driver, name, last_name, address, day):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.get_order_page_by_clicking_upper_order_page()
        order_page.set_order(name, last_name, address, day)
        assert 'Заказ оформлен' in order_page.check_order()
