import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_PositiveLogin(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3) 
        driver.find_element(By.CSS_SELECTOR,'[name="username"]').send_keys('Admin')
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@name="password"]').send_keys('admin123')
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@type="submit"]').click()
        time.sleep(5)
        dashboard_text = driver.find_element(By.XPATH,"//h6[1]").text
        self.assertEqual(dashboard_text, "Dashboard")

    def tearDown(self):
        self.driver.close()
