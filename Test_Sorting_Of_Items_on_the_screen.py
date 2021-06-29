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


def test_check_deafult_items_sorting_is_AZ():
    search_page_for_shorts()
    switch_sorting_in_dropbox('по назві по зростанню')
    check_sorting_in_dropbox_is('по назві по зростанню')
    check_items_are_sorted('AZ')


def test_items_sorting_ZA():
    search_page_for_shorts()
    switch_sorting_in_dropbox('за назвою за спаданням')
    check_sorting_in_dropbox_is('за назвою за спаданням')
    check_items_are_sorted('ZA')


def test_items_sorting_price_low_hight():
    search_page_for_shorts()
    switch_sorting_in_dropbox('за ціною по зростанню')
    check_sorting_in_dropbox_is('за ціною по зростанню')
    check_items_are_sorted('price_low_high')


def test_items_sorting_price_hight_low():
    search_page_for_shorts()
    switch_sorting_in_dropbox('за ціною за спаданням')
    check_sorting_in_dropbox_is('за ціною за спаданням')
    check_items_are_sorted('price_high_low')


def test_items_sorting_by_date_low_high():
    search_page_for_shorts()
    switch_sorting_in_dropbox('за датою за зростанням')
    check_sorting_in_dropbox_is('за датою за зростанням')


def test_items_sorting_by_date_high_low():
    search_page_for_shorts()
    switch_sorting_in_dropbox('за датою за спаданням')
    check_sorting_in_dropbox_is('за датою за спаданням')

    # ------------------------------------------------------------------



def check_sorting_in_dropbox_is(sorting_type):
    sorting_dropdown = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="s_setting_0"]')))
    sorting_dropdown_text = sorting_dropdown.text
    assert sorting_type in sorting_dropdown_text


def check_items_are_sorted(sorting_type):
    all_search_div_elements = pytest.driver.find_elements_by_xpath('//*[@id="search"]/div')
    filtered_items = []
    for div_element in all_search_div_elements:
        if div_element.text != '':
            filtered_items.append(div_element)

    first_element = filtered_items[0]
    last_element = filtered_items[len(filtered_items) - 1]

    if 'AZ' == sorting_type:
        print('Checking AZ sorting')
        first_item_name = get_item_name(first_element)
        last_item_name = get_item_name(last_element)
        assert first_item_name < last_item_name

    if 'ZA' == sorting_type:
        print('Checking ZA sorting')
        first_item_name = get_item_name(first_element)
        last_item_name = get_item_name(last_element)
        assert first_item_name > last_item_name

    if 'price_low_high' == sorting_type:
        print('Checking price low high sorting')
        first_item_price = get_item_price(first_element)
        last_item_price = get_item_price(last_element)
        assert first_item_price < last_item_price

    if 'price_high_low' == sorting_type:
        print('Checking price high low sorting')
        first_item_price = get_item_price(first_element)
        last_item_price = get_item_price(last_element)
        assert first_item_price > last_item_price


def get_item_price(element):
    item_text_array = element.text.split('\n')
    item_price_text = item_text_array[len(item_text_array) - 2].split()
    item_price = float(item_price_text[0].replace(',', '.'))
    return item_price



def get_item_name(element):
    item_text_array = element.text.split('\n')
    item_text = item_text_array[len(item_text_array) - 3]
    return item_text


def switch_sorting_in_dropbox(sorting_type):
    item_number_dropdown = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="s_setting_0"]')))
    item_number_dropdown.click()

    link_for_items = get_link_for_items_on_the_screen_by_value(sorting_type)
    link_for_items.click()


def get_link_for_items_on_the_screen_by_value(sorting_type):
    all_links = pytest.driver.find_elements_by_css_selector('li a')

    for a in all_links:
        print("Link text: {}".format(a.text))
        if sorting_type in a.text:
            print("Found link - {}".format(a.text))
            return a

def search_page_for_shorts():
   pytest.driver.find_element_by_id('menu_search_text').send_keys('Шорти жіночі')
   search_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_search"]/button[1]')))
   search_button.click()

   target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text
   assert "Результати пошуку" == target_text
   items_number_label = pytest.driver.find_element_by_xpath("//*[@id=\"content\"]/div[1]/span[1]/b[1]").text
   number_of_all_shorts_found = int(items_number_label)
   assert number_of_all_shorts_found > 0