from locators import Locator as lc
from selenium.webdriver import ActionChains
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class homePage(object): 

    def __init__(self,driver):
        self.driver=driver

    def clickMenu(self):
        self.driver.find_element_by_id(lc.categoryId).click()
    
    def selectCategory(self):
        self.driver.find_element_by_xpath(lc.selectCategoryXpath).click()
    
    def selectOption(self):
        self.driver.find_element_by_xpath(lc.selectOptionXpath).click()
    
    def sortbyvalue(self):
        self.driver.find_element_by_id(lc.sortId).click()
        self.driver.find_element_by_xpath(lc.sortvalue).click()
