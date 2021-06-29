import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver')
   pytest.driver.get('https://royalfashion.com.ua/')

   yield

   pytest.driver.quit()

def test_search_for_proper_item_should_find_elements():
   pytest.driver.find_element_by_id('menu_search_text').send_keys('Шорти жіночі')

   search_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_search"]/button[1]')))
   search_button.click()

   target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text
   assert "Результати пошуку" == target_text

   items_number_label = pytest.driver.find_element_by_xpath("//*[@id=\"content\"]/div[1]/span[1]/b[1]").text
   number_of_elements_found = int(items_number_label)

   assert number_of_elements_found > 0


def test_search_for_inproper_item_should_return_can_not_find_label():
   pytest.driver.find_element_by_id('menu_search_text').send_keys('dflgjdfklgdfkg')
   search_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_search"]/button[1]')))
   search_button.click()

   target_text = pytest.driver.find_element_by_css_selector("div#menu_messages_warning > div > p").text
   assert "На жаль, ми не знайшли продуктів, які ви шукаєте." == target_text


def test_should_filter_shorts_by_size_universal():
   run_test_for_size_by('//*[@id="filter_checkbox_1098261179_val257"]', '//*[@id="filter_checkbox_1098261179_val257"]')

def test_should_filter_shorts_by_size_XS():
   run_test_for_size_by('//*[@id="filter_checkbox_1098261179_val10"]', '//*[@id="filter_item_1098261179_10_box"]/div[1]/label[1]')

def test_should_filter_shorts_by_size_S():
   run_test_for_size_by('//*[@id="filter_checkbox_1098261179_val11"]', '//*[@id="filter_item_1098261179_11_box"]/div[1]/label[1]')

def test_should_filter_shorts_by_size_M():
   run_test_for_size_by('//*[@id="filter_checkbox_1098261179_val12"]', '//*[@id="filter_item_1098261179_12_box"]/div[1]/label[1]')

def test_should_filter_shorts_by_size_L():
   run_test_for_size_by('//*[@id="filter_checkbox_1098261179_val13"]', '//*[@id="filter_item_1098261179_13_box"]/div[1]/label[1]')

def test_should_filter_shorts_by_size_XL():
   run_test_for_size_by('//*[@id="filter_checkbox_1098261179_val14"]', '//*[@id="filter_item_1098261179_14_box"]/div[1]/label[1]')


def test_should_filter_shorts_by_color_pink():
   run_test_for_color_filter('/*[@id="filter_traits62_val99"]', '//*[@id="filter_traits62_val99_quantity"]/span[1]')

def test_should_filter_shorts_by_color_blue():
   run_test_for_color_filter('//*[@id="filter_traits62_val83"]', '//*[@id="filter_traits62_val83_quantity"]/span[1]')

def test_should_filter_shorts_by_color_dark_blue():
   run_test_for_color_filter('//*[@id="filter_traits62_val815"]', '//*[@id="filter_traits62_val815_quantity"]/span[1]')

def test_should_filter_shorts_by_color_yellow():
   run_test_for_color_filter('//*[@id="filter_traits62_val456"]', '//*[@id="filter_traits62_val456_quantity"]/span[1]')

def test_should_filter_shorts_by_color_black():
   run_test_for_color_filter('//*[@id="filter_traits62_val270"]', '//*[@id="filter_traits62_val270_quantity"]/span[1]')

# ------------------------------------------------------------------

def run_test_for_size_by (xpath_size_selector, xpath_item_number):
   search_page_for_shorts()

   filter_sizes_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.ID, 'filter_sizes')))
   filter_sizes_button.click()

   spodnie_filter_button = WebDriverWait(pytest.driver, 10).until(
      presence_of_element_located((By.XPATH, '//*[@id="filter_sizes_content"]/div[1]/div[3]')))
   spodnie_filter_button.click()

   size_flag_checkbutton = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, xpath_size_selector)))
   size_flag_checkbutton.click()

   items_expected_number_label_str = pytest.driver.find_element_by_xpath(xpath_item_number).text
   items_expected_number_label = int(items_expected_number_label_str.split('(')[1].split(')')[0])

   close_filters_button = WebDriverWait(pytest.driver, 10).until(
      presence_of_element_located((By.XPATH, '//*[@id="filter_options_1098261179_options"]/a[1]')))
   close_filters_button.click()

   target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text
   assert "Результати пошуку" == target_text

   items_number_label = pytest.driver.find_element_by_xpath("//*[@id=\"content\"]/div[1]/span[1]/b[1]").text
   number_of_elements_found = int(items_number_label)

   assert number_of_elements_found == items_expected_number_label


def search_page_for_shorts():
   pytest.driver.find_element_by_id('menu_search_text').send_keys('Шорти жіночі')
   search_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_search"]/button[1]')))
   search_button.click()

   target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text
   assert "Результати пошуку" == target_text
   items_number_label = pytest.driver.find_element_by_xpath("//*[@id=\"content\"]/div[1]/span[1]/b[1]").text
   number_of_all_shorts_found = int(items_number_label)
   assert number_of_all_shorts_found > 0


def run_test_for_color_filter(xpath_color_selector, xpath_color_filter_label):
   search_page_for_shorts()

   filter_color_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.ID, 'filter_traits62')))
   filter_color_button.click()

   color_flag_checkbutton = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, xpath_color_selector)))
   color_flag_checkbutton.click()

   items_expected_number_label_str = pytest.driver.find_element_by_xpath(xpath_color_filter_label).text
   items_expected_number_label = int(items_expected_number_label_str.split('(')[1].split(')')[0])

   close_filters_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="filter_traits62_submit"]')))
   close_filters_button.click()

   target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text
   assert "Результати пошуку" == target_text

   items_number_label = pytest.driver.find_element_by_xpath("//*[@id=\"content\"]/div[1]/span[1]/b[1]").text
   number_of_elements_found = int(items_number_label)

   assert number_of_elements_found == items_expected_number_label
