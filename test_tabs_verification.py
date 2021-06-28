import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver')
   # Переходим на страницу авторизации
   pytest.driver.get('https://royalfashion.com.ua/')

   yield

   pytest.driver.quit()

def test_bestseller_tab_opens_on_click():
    enter_cabinet_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_categories"]/ul[2]/li[1]/a[1]')))
    enter_cabinet_button.click()

    target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text

    assert 'Bestseller' == target_text

def test_newitems_tab_opens_on_click():
    enter_cabinet_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_categories"]/ul[2]/li[2]/a[1]')))
    enter_cabinet_button.click()

    target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text

    assert 'Новинки' == target_text

def test_for_her_tab_opens_on_click():
    enter_cabinet_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_categories"]/ul[2]/li[3]/a[1]')))
    enter_cabinet_button.click()

    target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text

    assert 'ДЛЯ НЕЇ' == target_text\

def test_for_him_tab_opens_on_click():
    enter_cabinet_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_categories"]/ul[2]/li[4]/a[1]')))
    enter_cabinet_button.click()

    target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text

    assert 'ДЛЯ НЬОГО' == target_text

def test_for_kid_tab_opens_on_click():
    enter_cabinet_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_categories"]/ul[2]/li[5]/a[1]')))
    enter_cabinet_button.click()

    target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text

    assert 'ДЛЯ ДИТИНИ' == target_text

def test_for_home_tab_opens_on_click():
    enter_cabinet_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_categories"]/ul[2]/li[6]/a[1]')))
    enter_cabinet_button.click()

    target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text

    assert 'ДЛЯ ДОМУ' == target_text

def test_outlet_tab_opens_on_click():
    enter_cabinet_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_categories"]/ul[2]/li[7]/a[1]')))
    enter_cabinet_button.click()

    target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text

    assert 'OUTLET' == target_text

def test_deals_tab_opens_on_click():
    enter_cabinet_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_categories"]/ul[2]/li[8]/a[1]')))
    enter_cabinet_button.click()

    target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text

    assert 'Акція %' == target_text

def test_last_things_tab_opens_on_click():
    enter_cabinet_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_categories"]/ul[2]/li[9]/a[1]')))
    enter_cabinet_button.click()

    target_text = pytest.driver.find_element_by_css_selector("div#content > div > h1").text

    assert 'Останні пари' == target_text