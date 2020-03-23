from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get('http://python.org')

search=driver.find_element_by_id('id-search-field')
search.clear()
search.send_keys('pycon')
search.send_keys(Keys.RETURN)
time.sleep(5)

driver.close()