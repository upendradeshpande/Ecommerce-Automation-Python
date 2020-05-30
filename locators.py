import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Locator(object):
    PATH = r"C:\Users\u.satish.deshpande\chromedriver.exe"
    #river=webdriver.chrome(executable_path=PATH)
    #driver= webdriver.chrome(PATH)
    URL="https://amazon.in"
    searchId = "0dRlrTqyZcagU2z4nmKwmg"
    categoryId="nav-hamburger-menu"
    selectCategoryXpath='//a[contains(., "Mobiles, Computers")]'
    selectOptionXpath='//a[contains(., "All Mobile Phones")]'
    sortId="sort"
    confirm='//a[contains(., "Hello, upendra")]'
    #drpdown.select_by_visible_text("Price: High to Low")

    def __init__(self,driver):
        self.driver=driver

    def clickMenu(self):
        self.driver.find_element_by_id(self.categoryId).click()
    
    def selectCategory(self):
        self.driver.find_element_by_xpath(self.selectCategoryXpath).click()
    
    def selectOption(self):
        self.driver.find_element_by_xpath(self.selectOptionXpath).click()
 

    

    

    

