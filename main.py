from logging import log
from os import name
from selenium import webdriver
from dotenv import load_dotenv

browser = webdriver.Firefox()
browser.get('https://www.flipkart.com/sony-chu-2208bb01i-1000-gb-spider-man-ratchet-clank-gran-turismo/p/itm8230ffd9a827b?pid=GMCFUAKAMHX6QJ2C&lid=LSTGMCFUAKAMHX6QJ2C1HTDLX&marketplace=FLIPKART&q=ps4&store=4rr&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=ce6379e2-5ac3-4f4a-a336-1d1bce1256fb.GMCFUAKAMHX6QJ2C.SEARCH&ppt=browse&ppn=browse&ssid=toxzlozlu5xmtslc1622043007335&qH=0e740342f31e9aa6') 
notCLickable = True

loginDetails = {
    "mobile_No" : ,
    "password": ""
}

address = {
      


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

login()

def addressing():
    radioButton = browser.find_element_by_class_name("_3DAmyP")
    radioButton.click()
    nameBar = browser.find_element_by_name("name")
    phoneNumber = browser.find_element_by_name("phone")
    address = browser.find_element_by_class_name("_1sQQBU._1w3ZZo._1TO48q")
    pincode = browser.find_element_by_name("pincode")
    locality = browser.find_element_by_name("addressLine2")
    saveAddbutton = browser.find_element_by_class_name("_2KpZ6l._1JDhFS._3AWRsL")
    nameBar.send_keys()
    phoneNumber.send_keys()
    address.send_keys("")
    pincode.send_keys("226016")    


while notCLickable :
    
      
    try:
        element = browser.find_element_by_class_name("_2KpZ6l._2U9uOA.ihZ75k._3AWRsL")
        element.click()
        print("added _to_cart")
       
    except:
        print("Refreshing")    
     
 

