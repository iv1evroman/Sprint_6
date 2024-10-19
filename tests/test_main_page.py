import pytest
from data import ANSWER_TEXTS
from pages.main_page import MainPage
import allure


class TestMainPage:
    @allure.description('Добавляем параметризацию для теста FAQ')
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, ANSWER_TEXTS[0]),
            (1, ANSWER_TEXTS[1]),
            (2, ANSWER_TEXTS[2]),
            (3, ANSWER_TEXTS[3]),
            (4, ANSWER_TEXTS[4]),
            (5, ANSWER_TEXTS[5]),
            (6, ANSWER_TEXTS[6]),
            (7, ANSWER_TEXTS[7]),
        ]
    )
    @allure.title('Проверка, что при клике на вопрос ответ правильный')
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.open_main_page_and_close_cookie_message()
        assert main_page.get_answer_text(num) == result

    @allure.title('Проверка, что при клике на логотип "Самоката" открывается главная страница')
    def test_scooter_logo_click(self, driver):
        main_page = MainPage(driver)
        assert 'на пару дней' in main_page.clicking_to_scooter_logo_and_getting_main_page_header()

    @allure.title('Проверка того, что при клике на логотип яндекса происходит редирект и открывается '
                  'главная страница Дзена.')
    def test_yandex_logo_click(self, driver):
        main_page = MainPage(driver)
        assert 'Найти' in main_page.clicking_to_yandex_logo_and_getting_search_button_text()
