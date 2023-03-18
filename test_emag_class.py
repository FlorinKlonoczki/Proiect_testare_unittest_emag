import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestEmag(unittest.TestCase):
    search_box = (By.ID, 'searchboxTrigger')
    produs = (By.CLASS_NAME, 'pad-hrz-xs')
    pret = (By.CLASS_NAME, 'product-new-price')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.emag.ro/')
        self.driver.maximize_window()

    def test_search(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(3)
        laptop = self.driver.find_element(*self.produs).text
        self.assertIn('Nitro 5', laptop)

    def test_price(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(3)
        pret = self.driver.find_element(*self.pret).text
        print(pret)
        self.assertIn('Lei', pret)