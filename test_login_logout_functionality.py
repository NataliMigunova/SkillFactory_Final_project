import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

email = "prostogelya@gmail.com"
password = "6Hpf4ws!ants9_h"

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver')
   # Переходим на страницу авторизации
   pytest.driver.get('https://royalfashion.com.ua/')

   yield

   pytest.driver.quit()

def test_login_to_account():
   enter_cabinet_button = WebDriverWait(pytest.driver, 10).until(presence_of_element_located((By.XPATH, '//*[@id="menu_basket"]/div[1]/a[1]')))
   enter_cabinet_button.click()

   pytest.driver.find_element_by_id('signin_login_input').send_keys('Prostogelya')
   pytest.driver.find_element_by_id('signin_pass_input').send_keys('ehYZHh6htEPm4aZ')

   login_button = pytest.driver.find_element_by_css_selector("div#signin-form_box_sub_1 > form > button")
   login_button.click()

   time.sleep(1)

   target_text = pytest.driver.find_element_by_css_selector("div#menu_basket > div > a").text

   assert 'ВАШ СЧЕТ' == target_text

def test_logout_from_account():
   enter_cabinet_button = WebDriverWait(pytest.driver, 10).until(
      presence_of_element_located((By.XPATH, '//*[@id="menu_basket"]/div[1]/a[1]')))
   enter_cabinet_button.click()

   pytest.driver.find_element_by_id('signin_login_input').send_keys('Prostogelya')
   pytest.driver.find_element_by_id('signin_pass_input').send_keys('ehYZHh6htEPm4aZ')

   login_button = pytest.driver.find_element_by_css_selector("div#signin-form_box_sub_1 > form > button")
   login_button.click()

   time.sleep(1)

   target_button = pytest.driver.find_element_by_css_selector("div#menu_basket > div > a")

   assert 'ВАШ СЧЕТ' == target_button.text

   target_button.click()

   logout_button = pytest.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/a[1]')
   logout_button.click()

   new_login_button = pytest.driver.find_element_by_css_selector("div#signin-form_box_sub_1 > form > button")

   assert new_login_button
