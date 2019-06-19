import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from random import randint

class Webdriver(unittest.TestCase):
    def setUp(self):
        # test open web browser with chrome
        self.driver = webdriver.Chrome()
        print("access to google chrome")

    def test_url_function(self):
        driver = self.driver
        driver.get("https://www.localtest.com")
        driver.set_page_load_timeout(2)
        driver.maximize_window()
        # driver.set_window_size(1341, 810)
        driver.implicitly_wait(2)
        time.sleep(2)
        print("navigate to link")

# test logged in account
# enter username and password
elem = driver.find_element_by_xpath("//input[@placeholder='
Username']")
elem.send_keys("standard_user")
time.sleep(2)
print("username data is true")
elem = driver.find_element_by_xpath("//input[@placeholder='Password']")
elem.send_keys("local_test")
time.sleep(2)
print("password data is true")
# test click to submit login account
elem = driver.find_element_by_name("LOGIN")
elem.click()
time.sleep(2)
print("user can logged in account")

# random test from product list
print("Random Product List")
# random click from product list to choose products
elem = driver.find_elements_by_css_selector('div.inventory_item_price')
product = elem[randint(0, len(elem) - 1)]
product.click()
time.sleep(2)
print("success click to random product")
driver.execute_script("window.scrollBy(0,-200);")
time.sleep(2)
print("success smooth scrolling the page")

# test click to cart button
elem = driver.find_element_by_xpath("//a[@href='./cart.html']")

elem.click()
time.sleep(2)
print("user can click cart and navigate to cart.html")

# test click to checkout
elem = driver.find_element_by_xpath("//a[@href='./checkout-step-one.html']")
elem.click()
time.sleep(2)
print("user checkout product")

# checkout information
elem = driver.find_element_by_xpath("//input[@placeholder='
First Name']")
elem.send_keys("Avriana")
time.sleep(2)
print("first name is true")
elem = driver.find_element_by_xpath("//input[@placeholder='Last Name']")
elem.send_keys("Indarwasti")
time.sleep(2)
print("last name is true")
elem = driver.find_element_by_xpath("//input[@placeholder='Zip/Postal Code']")
elem.send_keys("15417")
time.sleep(2)
print("zip/postal code is true")
# test click to submit login account
elem = driver.find_element_by_name("CONTINUE")
elem.click()
time.sleep(2)
print("user submit information for checkout")

# finish checkout overview
elem = driver.find_element_by_xpath("//a[@href='./checkout-complete.html']")
elem.click()
time.sleep(2)
print("user success checkout")

# test logged in account
# enter username and password
# elem = driver.find_element_by_xpath("//input[@placeholder='
Username']")
# elem.send_keys("problem_user")
# time.sleep(2)
# print("username data is true")
# elem = driver.find_element_by_xpath("//input[@placeholder='Password']")
# elem.send_keys("local_test")
# time.sleep(2)
print("password data is true")
# test click to submit login account
# elem = driver.find_element_by_name("LOGIN")
# elem.click()
# time.sleep(2)
# print("user can logged in account")

# random test from product list
# print("Random Product List")
# random click from product list to choose products
# elem = driver.find_elements_by_css_selector('div.inventory_item_price')
# product = elem[randint(0, len(elem) - 1)]
# product.click()
# time.sleep(2)
# print("success click to random product")
# driver.execute_script("window.scrollBy(0,-200);")
# time.sleep(2)
# print("success smooth scrolling the page")

# test click to cart button
# elem = driver.find_element_by_xpath("//a[@href='./cart.html']")

# elem.click()
# time.sleep(2)
# print("user can click cart and navigate to cart.html")

# test click to checkout
# elem = driver.find_element_by_xpath("//a[@href='./checkout-step-one.html']")
# elem.click()
# time.sleep(2)
# print("user checkout product")

# checkout information
# elem = driver.find_element_by_xpath("//input[@placeholder='
First Name']")
# elem.send_keys("Avriana")
# time.sleep(2)
# print("first name is true")
# elem = driver.find_element_by_xpath("//input[@placeholder='Last Name']")
# elem.send_keys("Indarwasti")
# time.sleep(2)
# print("last name is false")
# elem = driver.find_element_by_xpath("//input[@placeholder='Zip/Postal Code']")
# elem.send_keys("15417")
# time.sleep(2)
# print("zip/postal code is true")
# test click to submit login account
# elem = driver.find_element_by_name("CONTINUE")
# elem.click()
# time.sleep(2)
# print("user submit information for checkout")

# checkout overview
# elem = driver.find_element_by_xpath("//a[@href='./checkout-complete.html']")
# elem.click()
# time.sleep(2)
# print("user success checkout")




    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()
