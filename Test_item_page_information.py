import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver')
   pytest.driver.get('https://royalfashion.com.ua/product-ukr-470386-ZELENI-ZHINOCHI-KAMUFLIAZHNI-SHORTI.html')

   yield

   pytest.driver.quit()


def test_breadcrumbs():
    breadcrumbs_item = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.ID, 'breadcrumbs_sub')))
    breadcrumbs_text = breadcrumbs_item.text
    assert 'Ви знаходитесь тут:' in breadcrumbs_text
    assert 'Головна сторінка' in breadcrumbs_text
    assert 'ДЛЯ НЕЇ' in breadcrumbs_text
    assert 'Новинки' in breadcrumbs_text
    assert 'Зелені жіночі камуфляжні шорти' in breadcrumbs_text


def test_item_has_description_header():
    header_text = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="projector_form"]/div[1]/h1[1]')))
    assert 'Зелені жіночі камуфляжні шорти' == header_text.text


def test_item_has_price():
    price_element = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="projector_price_value"]')))
    assert 'ГРН' in price_element.text


def test_other_color_variants_are_present():
   all_links = pytest.driver.find_elements_by_css_selector('form#projector_form > div:nth-of-type(3) > div:nth-of-type(2) > div > a > img')
   assert len(all_links) > 0


def test_size_mesh_is_present():
   size_mesh_buttons = pytest.driver.find_elements_by_css_selector('div#projector_sizes_cont > div > a')
   assert len(size_mesh_buttons) > 0


def test_add_to_cart_button_is_present():
   add_to_cart_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.ID, 'projector_button_basket')))
   assert add_to_cart_button.text == 'ДОДАТИ ДО КОШИКА'


def test_favorite_button_is_present():
   add_to_favorite_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.ID, 'projector_button_observe')))
   assert add_to_favorite_button.get_attribute('href').endswith('#add_favorite')


def test_return_disclaimer_is_present():
   return_disclaimer_header = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="n67367_returns"]/h3[1]')))
   return_disclaimer_header_text = return_disclaimer_header.text
   return_disclaimer = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="n67367_returns"]/div[1]')))
   return_disclaimer_text = return_disclaimer.text
   return_disclaimer_additional_info_link = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.CSS_SELECTOR, 'div#n67367_returns > a')))
   return_disclaimer_additional_info_link_text = return_disclaimer_additional_info_link.text

   assert 'ПРОСТЕ ПОВЕРНЕННЯ ТОВАРУ' == return_disclaimer_header_text
   assert 'Придбайте і перевірте спокійно вдома. Впродовж 365 днів Ви можете відмовитися від договору без пояснення причин.' == return_disclaimer_text
   assert 'Показати подробиці' == return_disclaimer_additional_info_link_text


def test_should_open_returns_additional_info():
   return_disclaimer_additional_info_link = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.CSS_SELECTOR, 'div#n67367_returns > a')))
   return_disclaimer_additional_info_link_text = return_disclaimer_additional_info_link.text
   additional_return_info_block = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.CSS_SELECTOR, 'div#n67367_returns > div:nth-of-type(2)')))

   assert 'Показати подробиці' == return_disclaimer_additional_info_link_text
   assert 0 == additional_return_info_block.location['x']
   assert 0 == additional_return_info_block.location['y']

   return_disclaimer_additional_info_link.click()

   assert 'Приховати подробиці' == return_disclaimer_additional_info_link.text
   assert 0 != additional_return_info_block.location['x']
   assert 0 != additional_return_info_block.location['y']


def test_element_precise_description_is_present():
   precise_description_block = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="content"]/div[4]')))
   precise_description_text = precise_description_block.text
   assert 100 < len(precise_description_text)


def test_information_blocks_are_present():
    assert 'Довжина' == pytest.driver.find_elements_by_xpath('//*[@id="component_projector_dictionary_no"]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/span')[0].text
    assert len(pytest.driver.find_elements_by_xpath('//*[@id="component_projector_dictionary_no"]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]')[0].text) > 0
    assert 'Стан' == pytest.driver.find_elements_by_xpath('//*[@id="component_projector_dictionary_no"]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/span')[0].text
    assert len(pytest.driver.find_elements_by_xpath('//*[@id="component_projector_dictionary_no"]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[2]')[0].text) > 0
    assert 'Матеріал' == pytest.driver.find_elements_by_xpath('//*[@id="component_projector_dictionary_no"]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[1]/span')[0].text
    assert len(pytest.driver.find_elements_by_xpath('//*[@id="component_projector_dictionary_no"]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[2]')[0].text) > 0
    assert 'Склад' == pytest.driver.find_elements_by_xpath('//*[@id="component_projector_dictionary_no"]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[1]/span')[0].text
    assert len(pytest.driver.find_elements_by_xpath('//*[@id="component_projector_dictionary_no"]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[2]')[0].text) > 0


def test_alert_disclaimer_block_is_present():
   alert_disclaimer_line_1 = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="component_projector_cms"]/div[1]/div[1]/p[1]')))
   alert_disclaimer_line_2 = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="component_projector_cms"]/div[1]/div[1]/p[2]')))
   alert_disclaimer_line_1_text = alert_disclaimer_line_1.text
   alert_disclaimer_line_2_text = alert_disclaimer_line_2.text

   assert 'УВАГА! Перед замовленням перевіряйте таблицю розмірів. В таблиці вказані розміри устілки в сантиметрах.' == alert_disclaimer_line_1_text
   assert 'У випадку перевищення суми замовлення більше ніж на 100 EUR будуть нараховані митні збори. Детальніше тут Доставка' == alert_disclaimer_line_2_text


def test_review_button_is_present():
   review_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.ID, 'opinions_58676')))
   assert 'відгуки' in review_button.text


def test_ask_question_button():
   ask_question_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.ID, 'askforproduct_58676')))
   assert 'поставити питання' == ask_question_button.text

