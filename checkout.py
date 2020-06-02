from locators import Locator as lc
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

class checkoutPage(object):

    
    def __init__(self,driver):
        self.driver=driver

    def storeResult(self):

        firstitm=self.driver.find_elements_by_xpath(lc.firstitemxpath)
        return firstitm


    def addToCart(self): 
        addcart=self.driver.find_elements_by_id(lc.addtocartId)
        for i in addcart:
            i.click()
            break
        element_present = EC.presence_of_element_located((By.ID, lc.cartId))
        WebDriverWait(self.driver, 10).until(element_present)

    def goToCart(self):
        car=self.driver.find_elements_by_id(lc.cartId)
        car[0].click()
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, lc.cartresultId)))