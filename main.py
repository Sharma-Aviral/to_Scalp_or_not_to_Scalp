from logging import log
import time
from os import name
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv

browser = webdriver.Firefox()
browser.get('https://www.flipkart.com/noise/p/itm0d83240694f33?pid=9780008309008&lid=LSTBOK9780008309008IEUPVV&marketplace=FLIPKART&store=bks&srno=b_1_1&otracker=browse&fm=organic&iid=265bf789-6744-4485-b098-51ae02ee1b37.9780008309008.SEARCH&ppt=None&ppn=None&ssid=qn0oevfzr40000001622097919257') 
notCLickable = True

loginDetails = {
    "mobile_No" :,
    "password": ""
}


print(loginDetails["mobile_No"])

def login():
   
    loginButton = browser.find_element_by_class_name("_1_3w1N")
    loginButton.click()
    passwordBox = browser.find_element_by_class_name("_2IX_2-._3mctLh.VJZDxU")
    userName  = browser.find_element_by_class_name("_2IX_2-.VJZDxU")
     
    passwordBox.send_keys(loginDetails["password"])
    userName.send_keys(loginDetails["mobile_No"])
    pressLogin = browser.find_element_by_class_name("_2KpZ6l._2HKlqd._3AWRsL")
    pressLogin.click()
    time.sleep(1.24)



def addressing():
  
    time.sleep(0.5)
    contiButtons = browser.find_element_by_class_name("_2KpZ6l._1seccl._3AWRsL")
    # nameBar.send_keys("aviral.sharma.012@gmail.com")
    time.sleep(1)
    contiButtons.click()
    time.sleep(5)
    # upiRadioo = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "_1XFPmK")))
    upiRadioo = browser.find_element_by_id("UPI_COLLECT")
    upiRadioo.click()
    time.sleep(1)
    
while notCLickable :
    
    try:
        login()
        element = browser.find_element_by_class_name("_2KpZ6l._2U9uOA.ihZ75k._3AWRsL")
        element.click()
        notCLickable = False
        print("added _to_cart")
    except:  
       
        print("not in cart")
        browser.refresh()
     
 
addressing()
