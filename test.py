import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest
from locators import Locator


class amazonTest(unittest.TestCase):
    #lp=Locator()
    
    driver=webdriver.Chrome(Locator.PATH)

    @classmethod
    def setUpClass(cls):
        cls.driver.get(Locator.URL)
        cls.driver.maximize_window()

   # def setUpClass(self):
    #    self.driver.get(Locator.URL)
     #   self.driver.maximize_window()
    
    
    def test_homepage(self):
        lc=Locator(self.driver)
        lc.clickMenu()
        lc.selectCategory()
        lc.selectOption()

        #self.assertEqual(,self.driver.,"webpage title not matching")
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
    
    #def tearDownClass(self):
     #   self.driver.close()

if __name__ == "__main__":
    unittest.main()
  
    


#driver= webdriver.Chrome(PATH)
#driver= webdriver.Chrome(executable_path="C:\Users\u.satish.deshpande\chromedriver.exe")
#driver.get("https://www.amazon.in")
#print(driver.title)
#search = driver.find_element_by_id("0dRlrTqyZcagU2z4nmKwmg")
#search.send_keys("0dRlrTqyZcagU2z4nmKwmg")
#search.click()
#category=driver.find_element_by_id("nav-hamburger-menu")
#category.click()
#selectCategory= driver.find_element_by_xpath('//a[contains(., "Mobiles, Computers")]')
#selectCategory.click()
#selectCategoryMobile=driver.find_element_by_xpath('//a[contains(., "All Mobile Phones")]')
#selectCategoryMobile.click()
#Expensive=driver.find_element_by_xpath('//a[contains(., "25kAbove")]')
#Expensive.click()
#sort=driver.find_elements_by_id("sort")
#drpdown = Select(sort)
#drpdown.select_by_visible_text("Price: High to Low")
#drpdown.select_by_value("price-asc-rank")
