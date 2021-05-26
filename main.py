from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.flipkart.com/sony-chu-2208bb01i-1000-gb-spider-man-ratchet-clank-gran-turismo/p/itm8230ffd9a827b?pid=GMCFUAKAMHX6QJ2C&lid=LSTGMCFUAKAMHX6QJ2C1HTDLX&marketplace=FLIPKART&q=ps4&store=4rr&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=ce6379e2-5ac3-4f4a-a336-1d1bce1256fb.GMCFUAKAMHX6QJ2C.SEARCH&ppt=browse&ppn=browse&ssid=toxzlozlu5xmtslc1622043007335&qH=0e740342f31e9aa6') 
notCLickable = True
# passwordBox = browser.find_element_by_class_name("_2IX_2-._3mctLh.VJZDxU")
# userName  = browser.find_element_by_class_name("_2IX_2-.VJZDxU")
while notCLickable :
    browser.refresh()
      
    try:
        element = browser.find_element_by_class_name("_2KpZ6l._2U9uOA.ihZ75k._3AWRsL")
        element.click()
        print("added _to_cart")
        notCLickable = False
    except:
        print("Refreshing")    

    print("dedeya")     