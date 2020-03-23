from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url='http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)
source=driver.find_element_by_xpath('//*[@id="box3"]')
destination=driver.find_element_by_xpath('//*[@id="box103"]')
actions=ActionChains(driver)
actions.drag_and_drop(source,destination).perform()

time.sleep(2)
driver.close()
