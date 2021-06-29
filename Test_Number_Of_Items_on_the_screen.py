import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

number_of_elements_on_the_screen = {'#90', '#180', '#270', '#300'}

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver')
   pytest.driver.get('https://royalfashion.com.ua/')

   yield

   pytest.driver.quit()


def test_check_deafult_number_of_items_on_the_screen_is_90():
    search_page_for_shorts()
    assert_number_in_dropbox(90)
    assert_number_of_items_on_the_screen(90)

def test_check_deafult_number_of_items_on_the_screen_is_180():
    search_page_for_shorts()
    switch_number_in_dropbox(180)
    assert_number_in_dropbox(180)
    assert_number_of_items_on_the_screen(180)

def test_check_deafult_number_of_items_on_the_screen_is_270():
    search_page_for_shorts()
    switch_number_in_dropbox(180)
    assert_number_in_dropbox(270)
    assert_number_of_items_on_the_screen(270)

def test_check_deafult_number_of_items_on_the_screen_is_300():
    search_page_for_shorts()
    switch_number_in_dropbox(300)
    assert_number_in_dropbox(300)
    assert_number_of_items_on_the_screen(300)

# ------------------------------------------------------------------

def switch_number_in_dropbox(number_to_select):
    item_number_dropdown = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="s_setting_1"]')))
    item_number_dropdown.click()

    link_for_items = get_link_for_items_on_the_screen_by_value(number_to_select)
    link_for_items.click()


def get_link_for_items_on_the_screen_by_value(number_of_items):
    all_links = pytest.driver.find_elements_by_css_selector('li a')
    link_number_text = '#' + str(number_of_items)
    print('Link number value - {}'.format(link_number_text))

    for a in all_links:
        print("Link value: {}".format(a.get_attribute('href')))
        if a.get_attribute('href').endswith(link_number_text):
            print("Found link - {}".format(a.get_attribute('href')))
            return a

def assert_number_in_dropbox(number_of_items):
    item_number_dropdown = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="s_setting_1"]')))
    items_number_on_the_screen = int(item_number_dropdown.text)
    assert items_number_on_the_screen == number_of_items

def assert_number_of_items_on_the_screen(number_of_items):
    all_search_div_elements = pytest.driver.find_elements_by_xpath('//*[@id="search"]/div')
    filtered_items = []
    for div_element in all_search_div_elements:
        if div_element.text != '':
            filtered_items.append(div_element)

    assert number_of_items == len(filtered_items)


def search_page_for_shorts():
   pytest.driver.find_element_by_id('menu_search_text').send_keys('Шорти жіночі')
   search_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_search"]/button[1]')))
   search_button.click()

   target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text
   assert "Результати пошуку" == target_text
   items_number_label = pytest.driver.find_element_by_xpath("//*[@id=\"content\"]/div[1]/span[1]/b[1]").text
   number_of_all_shorts_found = int(items_number_label)
   assert number_of_all_shorts_found > 0