from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get('https://wiki.python.org/moin/FrontPage')

search=driver.find_element_by_id('searchinput')
search.clear()
search.send_keys('Beginner')
search.send_keys(Keys.RETURN)
time.sleep(2)

select_option=Select(driver.find_element_by_xpath('//*[@class="actionsmenu"]/div/select'))
select_option.select_by_visible_text('Raw Text')
time.sleep(2)

driver.close()
