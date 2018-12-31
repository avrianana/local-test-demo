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
        driver.get("https://www.saucedemo.com")
        driver.set_page_load_timeout(2)
        driver.maximize_window()
        # driver.set_window_size(1341, 810)
        driver.implicitly_wait(2)
        time.sleep(2)
        print("navigate to link")
	
# test logged in account
# enter username and password
elem = driver.find_element_by_xpath("//input[@placeholder=' Username']")
elem.send_keys("standard_user")
time.sleep(2)
print("username data is true")
elem = driver.find_element_by_xpath("//input[@placeholder='Password']")
elem.send_keys("secret_sauce")
time.sleep(2)
print("password data is true")
# test click to submit login account
elem = driver.find_element_by_name("LOGIN")
elem.click()
time.sleep(2)
print("user can logged in account")

# test logged in account
# enter username and password
# elem = driver.find_element_by_xpath("//input[@placeholder=' Username']")
# elem.send_keys("locked_out_user")
# time.sleep(2)
# print("username data is true")
# elem = 
# driver.find_element_by_xpath("//input[@placeholder='Password']")
# elem.send_keys("secret_sauce")
# time.sleep(2)
# print("password data is true")
# test click to login account
# elem = driver.find_element_by_name("LOGIN")
# elem.click()
# time.sleep(2)
# print("this user has been locked out")

# test logged in account
# enter username and password
# elem = driver.find_element_by_xpath("//input[@placeholder='
Username']")
# elem.send_keys("problem_user")
# time.sleep(2)
# print("username data is true")
# elem = 
# driver.find_element_by_xpath("//input[@placeholder='Password']")
# elem.send_keys("secret_sauce")
# time.sleep(2)
# print("password data is true")
# test click to submit login account
# elem = driver.find_element_by_name("LOGIN")
# elem.click()
# time.sleep(2)
# print("user can logged in account")

   def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
