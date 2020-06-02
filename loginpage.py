from locators import Locator as lc
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import credentials

class loginPage(object):

    def __init__(self,driver):
        self.driver=driver

    def login(self):

        firstMenu= self.driver.find_element_by_id(lc.firstMenuId)
        ActionChains(self.driver).move_to_element(firstMenu).perform()
        secondMenu= self.driver.find_element_by_xpath(lc.secondMenuId)
        secondMenu.click()
        email=self.driver.find_elements_by_id(lc.emailId)
        for i in email:
            i.clear()
            i.send_keys(credentials.username)
            break

        continueButton=self.driver.find_elements_by_id(lc.cont)
        for i in continueButton:
            i.click()
            break
        
        password=self.driver.find_elements_by_id(lc.passwordId)
        for i in password :    
            i.clear()
            i.send_keys(credentials.pas)

        submitButton=self.driver.find_elements_by_id(lc.submitId)
        for i in submitButton:
            i.click()
            break
        
   


