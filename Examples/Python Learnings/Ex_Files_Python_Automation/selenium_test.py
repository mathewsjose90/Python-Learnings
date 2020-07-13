from selenium import webdriver
import time

driver=webdriver.Chrome()
url='https://www.seleniumeasy.com/test/basic-first-form-demo.html'
driver.get(url)

#Test the show message
message_field=driver.find_element_by_xpath('//*[@id="user-message"]')
message_field.send_keys('Hello Matz')

submit_button=driver.find_element_by_xpath('//*[@id="get-input"]/button')
submit_button.click()

#test sum of 2 values

item1=driver.find_element_by_xpath('//*[@id="sum1"]')
item1.send_keys('100')
item2=driver.find_element_by_xpath('//*[@id="sum2"]')
item2.send_keys('50')
sum_button=driver.find_element_by_xpath('//*[@id="gettotal"]/button')
sum_button.click()


time.sleep(3)
driver.close()