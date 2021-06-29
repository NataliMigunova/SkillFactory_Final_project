import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver')
   pytest.driver.get('https://royalfashion.com.ua')
   yield
   pytest.driver.quit()


def test_add_item_to_cart():
    search_page_for_shorts()
    item1_price = open_item_on_screen('Сірі жіночі шорти в смужку')
    add_current_item_to_cart()
    close_cart_dialog()

    assert_cart_contains_items_and_sum(1, item1_price)


def test_add_couple_of_items_to_cart_should_calculate_both():
    search_page_for_shorts()

    item1_price = open_item_on_screen('Сірі жіночі шорти в смужку')
    add_current_item_to_cart()
    close_cart_dialog()

    # adding 2nd item to the cart
    pytest.driver.get('https://royalfashion.com.ua')
    search_page_for_shorts()

    item2_price = open_item_on_screen('Темно-сині жіночі спортивні шорти')
    add_current_item_to_cart()
    close_cart_dialog()

    assert_cart_contains_items_and_sum(2, item1_price+item2_price)


def test_should_add_1_item_and_then_remove_it_from_the_cart():
    search_page_for_shorts()
    item1_price = open_item_on_screen('Сірі жіночі шорти в смужку')
    add_current_item_to_cart()
    close_cart_dialog()
    assert_cart_contains_items_and_sum(1, item1_price)

    open_cart()

    remove_item_from_cart('Сірі жіночі шорти в смужку')


def test_should_add_2_elements_calculate_sum_then_remove_1_and_recalculate():
    search_page_for_shorts()

    item1_price = open_item_on_screen('Сірі жіночі шорти в смужку')
    add_current_item_to_cart()
    close_cart_dialog()

    # adding 2nd item to the cart
    pytest.driver.get('https://royalfashion.com.ua')
    search_page_for_shorts()

    item2_price = open_item_on_screen('Темно-сині жіночі спортивні шорти')
    add_current_item_to_cart()
    close_cart_dialog()

    assert_cart_contains_items_and_sum(2, item1_price+item2_price)

    open_cart()

    remove_item_from_cart('Сірі жіночі шорти в смужку')

    assert_cart_contains_items_and_sum(1, item2_price)


# ------------------------------------------------------------------


def open_cart():
    cart_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_basket"]/a[1]/span[1]')))
    cart_button.click()


def remove_item_from_cart(item_name):
    all_items = pytest.driver.find_elements_by_class_name('productslist_item')
    for every_item in all_items:
        if item_name.upper() in every_item.text:
            remove_button = every_item.find_elements_by_class_name('productslist_product_remove')
            remove_button[0].click()
            break


def assert_cart_contains_items_and_sum(item_number, total_amount_to_pay):
    number_of_items_element = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_basket"]/a[1]/span[1]')))
    total_amount_element = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_basket"]/a[1]/strong[1]')))
    assert item_number == int(number_of_items_element.text)
    assert total_amount_to_pay == split_price_and_convert_to_float(total_amount_element.text)


def open_item_on_screen(item_name):
    screen_item = get_item_from_the_screen(item_name)
    item_price = get_item_price(screen_item)
    url_to_open = screen_item.find_elements_by_xpath('.//a')[1].get_attribute('href')
    pytest.driver.get(url_to_open)
    return item_price


def get_item_price(item_on_screen):
    item_text = item_on_screen.text
    item_text_array = item_text.split('\n')
    item_price_text = item_text_array[len(item_text_array) - 2]
    return split_price_and_convert_to_float(item_price_text)

def split_price_and_convert_to_float(price_text):
    item_price_splited = price_text.split()
    return float(item_price_splited[0].replace(',', '.'))


def add_current_item_to_cart():
    size_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="projector_sizes_cont"]/div[1]/a[1]')))
    size_button.click()

    add_to_cart_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.ID, 'projector_button_basket')))
    add_to_cart_button.click()

def close_cart_dialog():
    close_dialog_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.ID, 'dialog_close')))
    close_dialog_button.click()


def get_item_from_the_screen(item_text):
    all_search_div_elements = pytest.driver.find_elements_by_xpath('//*[@id="search"]/div')
    filtered_items = []
    for div_element in all_search_div_elements:
        if item_text in div_element.text:
            filtered_items.append(div_element)

    return filtered_items[0]

def search_page_for_shorts():
    pytest.driver.find_element_by_id('menu_search_text').send_keys('Шорти жіночі')
    search_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_search"]/button[1]')))
    search_button.click()

    target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text
    assert "Результати пошуку" == target_text
    items_number_label = pytest.driver.find_element_by_xpath("//*[@id=\"content\"]/div[1]/span[1]/b[1]").text
    number_of_all_shorts_found = int(items_number_label)
    assert number_of_all_shorts_found > 0