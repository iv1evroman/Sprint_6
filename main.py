import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFaqTexts:
    @pytest.mark.parametrize(
        'question_locator, answer_locator, answer_text',
        [
            [(By.XPATH, '//*[@id="accordion__heading-0"]'), (By.ID, "accordion__panel-0"), 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']
        ]
    )
    def test_faq_texts(self, question_locator, answer_locator, answer_text, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(question_locator))
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(question_locator))
        driver.find_element(question_locator).click()
        assert driver.find_element(answer_locator).text == answer_text