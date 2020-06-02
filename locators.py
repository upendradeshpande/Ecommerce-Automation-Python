import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Locator(object):
    PATH = r"C:\Users\u.satish.deshpande\chromedriver.exe"
    URL="https://amazon.com"
    searchId = "0dRlrTqyZcagU2z4nmKwmg"
    menu='//*[@id="a-popover-3"]/div/div/ul/li[3]'
    seconditemxpath='//*[@id="search"]/div[1]/div[2]/div/span[4]/div[2]/div[2]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span'
    firstMenuId="nav-link-accountList"
    secondMenuId='//*[@id="nav-flyout-ya-signin"]//a'
    emailId="ap_email"
    cont="continue"
    passwordId="ap_password"
    submitId="signInSubmit"
    checkUserXpath='//a[contains(., "Hello, upendra")]'
    categoryId="nav-hamburger-menu"
    selectCategoryXpath='//*[@data-menu-id="20"]//a'
    selectCategoryXpath='//a[contains(., "Computers")]'
    selectOptionXpath='//a[contains(., "Computer Accessories & Peripherals")]'
    sortId="a-autoid-0-announce"
    sortvalue='//*[@id="s-result-sort-select_2"]'
    result='//*[@data-uuid="06f06245-b319-40fe-a8e9-313783c28e70"]'
    addtocartId="add-to-cart-button"
    cartId="nav-cart"
    cartresultId="sc-active-cart"
    firstitemxpath='//*[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]//a'

    def __init__(self,driver):
        self.driver=driver
        

  
       

    

    

    


