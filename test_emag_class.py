import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestEmag(unittest.TestCase):
    search_box = (By.ID, 'searchboxTrigger')
    produs = (By.CLASS_NAME, 'pad-hrz-xs')
    pret = (By.CLASS_NAME, 'product-new-price')
    descriere_produs = (By.CLASS_NAME, 'card-v2-title-wrapper')
    deschidereProdus = (By.CLASS_NAME, 'card-v2-info')
    verificare_stoc = (By.CLASS_NAME, 'stock-and-genius')
    ridicare_produs = (By.CLASS_NAME, 'de-content')
    adaugareLaFovorit = (By.CLASS_NAME, 'product-buy-area-wrapper')
    checkFovorit = (By.ID, 'my_wishlist')
    stergereFovorite = (By.CSS_SELECTOR, '#list-of-favorites > div > div > div.d-flex.flex-item.flex-wrap.'
                                         'card-container > div.card-secondary.pad-hrz-sm.flex-item.text-right'
                                         '> div.actions-wrapper > div:nth-child(2)')
    adaugareCos = (By.CLASS_NAME, 'actions-wrapper')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.emag.ro/')
        self.driver.maximize_window()

    def test_search(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(2)
        laptop = self.driver.find_element(*self.produs).text
        self.assertIn('Nitro 5', laptop)

    def test_price(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(2)
        pret = self.driver.find_element(*self.pret).text
        print(pret)
        self.assertIn('Lei', pret)

    def test_descriereLaptop(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(2)
        descriere_produs = self.driver.find_element(*self.descriere_produs).text
        print(descriere_produs)
        self.assertIn('Laptop', descriere_produs)

    def test_clickOnLaptop(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(2)
        clic_produs = self.driver.find_element(*self.deschidereProdus).click()
        self.assertTrue("Laptop", clic_produs)


    def test_verificareStocProdus(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(2)
        self.driver.find_element(*self.deschidereProdus).click()
        time.sleep(2)
        verificare_stoc = self.driver.find_element(*self.verificare_stoc).text
        print(verificare_stoc)
        self.assertIn('stoc', verificare_stoc)

    def test_verificareRidicarePersonala(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(2)
        self.driver.find_element(*self.deschidereProdus).click()
        time.sleep(2)
        ridicare_produs = self.driver.find_element(*self.ridicare_produs).text
        print(ridicare_produs)
        self.assertIn('Ridicare', ridicare_produs)

    def test_adaugareProdusLaFavorite(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(2)
        self.driver.find_element(*self.deschidereProdus).click()
        time.sleep(2)
        adauga = self.driver.find_element(*self.adaugareLaFovorit).click()
        self.assertTrue("Favorite", adauga)


    def test_deschidePaginaDeFavorite(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(2)
        self.driver.find_element(*self.deschidereProdus).click()
        time.sleep(2)
        self.driver.find_element(*self.adaugareLaFovorit).click()
        time.sleep(2)
        favorit = self.driver.find_element(*self.checkFovorit).click()
        self.assertTrue("Favorite", favorit)

    def test_stergereProdusDeLaFavorite(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(2)
        self.driver.find_element(*self.deschidereProdus).click()
        time.sleep(2)
        self.driver.find_element(*self.adaugareLaFovorit).click()
        time.sleep(2)
        self.driver.find_element(*self.checkFovorit).click()
        time.sleep(2)
        sterge = self.driver.find_element(*self.stergereFovorite).click()
        self.assertTrue("Sterge", sterge)


    def test_adaugareProdusLaCos(self):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys('Laptop Nitro 5')
        search_box.submit()
        time.sleep(2)
        self.driver.find_element(*self.deschidereProdus).click()
        time.sleep(2)
        self.driver.find_element(*self.adaugareLaFovorit).click()
        time.sleep(2)
        self.driver.find_element(*self.checkFovorit).click()
        time.sleep(2)
        cos = self.driver.find_element(*self.adaugareCos).click()
        self.assertTrue("Adauga", cos)
