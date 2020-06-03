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

    firstMenuId="nav-link-accountList"
    secondMenuId='//*[@id="nav-flyout-ya-signin"]//a'
    emailId="ap_email"
    cont="continue"
    passwordId="ap_password"
    submitId="signInSubmit"
    checkUserXpath='//a[contains(., "Hello, upendra")]'
    categoryId="nav-hamburger-menu"
    selectCategoryXpath='//a[contains(., "Computers")]'
    selectOptionXpath='//a[contains(., "Computer Accessories & Peripherals")]'
    sortId="a-autoid-0-announce"
    sortvalueId="s-result-sort-select_2"
    result='//*[@data-uuid="06f06245-b319-40fe-a8e9-313783c28e70"]'
    addtocartId="add-to-cart-button"
    cartId="nav-cart"
    cartcount="nav-cart-count"
    cartresultId="sc-active-cart"
    firstitemxpath='//*[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]//a'

    def __init__(self,driver):
        self.driver=driver
        

  
       

    

    

    


