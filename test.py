from locators import Locator as lc
from loginpage import loginPage
from homepage import homePage
from checkout import checkoutPage
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
import testdata

class test_amazon(unittest.TestCase):
    
    if testdata.browser=="Chrome":
        driver=webdriver.Chrome(testdata.PATH)
    else:
        print("set the browser in testdata")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(testdata.URL)
        cls.driver.maximize_window()
    
    def test_Firstpage(self):
        print("Testing login page")
        self.driver.save_screenshot("beforelogin.png")
        self.assertEqual("Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more",self.driver.title,"webpage is different")
        signin=loginPage(self.driver)
        time.sleep(3)
        signin.login()
        self.driver.implicitly_wait(5)
        self.assertTrue(EC.visibility_of_element_located((By.XPATH,lc.checkUserXpath)))
        self.driver.save_screenshot("afterlogin.png")
       
    def test_Homepage(self):    
        print("Testing home page")
        self.assertEqual("Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more",self.driver.title,"webpage is different")
        home=homePage(self.driver)
        home.clickMenu()
        self.driver.implicitly_wait(2)
        home.selectCategory()
        home.selectOption()
        home.sortbyvalue()
        self.assertTrue(EC.visibility_of_element_located((By.XPATH,lc.result)))
        self.driver.save_screenshot("categoryResultHighToLow.png")
       
        

    def test_Lastpage(self):
        print("Testing Checkoutpage")
        checkout=checkoutPage(self.driver)
        parentGUID = self.driver.current_window_handle
        allresult=checkout.storeResult() 
        allresult[0].send_keys(Keys.CONTROL + Keys.ENTER)
        time.sleep(5)
        self.driver.switch_to_window(self.driver.window_handles[1])
        checkout.addToCart()
        time.sleep(3)
        self.driver.close()
        self.driver.switch_to_window(parentGUID)
        time.sleep(3)
        allresult[1].click()
        checkout.addToCart() 
        CartCount=checkout.goToCart()
        print(CartCount)
        self.assertEqual("2",CartCount, "cart count is not 2")
        self.driver.save_screenshot("cartitems.png")
        time.sleep(15)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
    
    

if __name__ == "__main__":
    unittest.main()
  

