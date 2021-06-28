import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver')
   # Переходим на страницу авторизации
   pytest.driver.get('https://royalfashion.com.ua/product-ukr-470386-ZELENI-ZHINOCHI-KAMUFLIAZHNI-SHORTI.html')

   yield

   pytest.driver.quit()


# def test_breadcrumbs():
#     breadcrumbs_item = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.ID, 'breadcrumbs_sub')))
#     breadcrumbs_text = breadcrumbs_item.text
#     assert 'Ви знаходитесь тут:' in breadcrumbs_text
#     assert 'Головна сторінка' in breadcrumbs_text
#     assert 'ДЛЯ НЕЇ' in breadcrumbs_text
#     assert 'Новинки' in breadcrumbs_text
#     assert 'Зелені жіночі камуфляжні шорти' in breadcrumbs_text


# def test_item_has_description_header():
#     header_text = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="projector_form"]/div[1]/h1[1]')))
#     assert 'Зелені жіночі камуфляжні шорти' == header_text.text

# def test_item_has_price():
#     price_text = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="projector_price_value"]')))
#     assert 'ГРН'in price_text.text