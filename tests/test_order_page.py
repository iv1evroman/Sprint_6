import pytest
from pages.order_page import OrderPage
import allure


class TestOrderPage:
    @allure.description('Проверяем, что при клике на верхнюю кнопку "заказать" открывается страница заказа')
    def test_upper_order_button(self, driver):
        order_page = OrderPage(driver)
        assert order_page.get_order_page_by_clicking_upper_order_page() == 'Для кого самокат'

    @allure.description('Проверяем, что при клике на нижнюю кнопку "заказать" открывается страница заказа')
    def test_lower_order_button(self, driver):
        order_page = OrderPage(driver)
        assert order_page.get_order_page_by_clicking_lower_order_page() == 'Для кого самокат'

    @allure.description('Тестируем весь флоу оформления заказа и убеждаемся что он оформлен')
    @pytest.mark.parametrize(
        'name, last_name, address, day',
        [
            ('Петя', 'Иванов', 'Москва', '11.11.2024'),
            ('Вася', 'Сидоров', 'Химки', '14.11.2024')
        ]
    )
    def test_successful_order(self, driver, name, last_name, address, day):
        order_page = OrderPage(driver)
        order_page.get_order_page_by_clicking_upper_order_page()
        order_page.set_order(name, last_name, address, day)
        assert 'Заказ оформлен' in order_page.check_order()
