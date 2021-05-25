from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.flipkart.com/sony-playstation-5-cfi-1008a01r-825-gb-astro-s-playroom/p/itma0201bdea62fa')
element = browser.find_element_by_class_name("_1INA6Y _1MBTtW")
print(element)