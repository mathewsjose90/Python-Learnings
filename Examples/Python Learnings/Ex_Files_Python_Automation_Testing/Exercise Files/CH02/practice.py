from selenium import webdriver

driver=webdriver.Chrome()
driver.get('file:///Users/mjose/Documents/Team/Python%20Learnings/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html')
#using id
login_form=driver.find_element_by_id('loginForm')
print("My login form element is ",login_form)
#using name
username=driver.find_element_by_name('username')
print('username element is ',username)
#using xpath
login_form_xpath_absoulute=driver.find_element_by_xpath('/html/body/form[1]')
login_form_xpath_relative=driver.find_element_by_xpath('//form[1]')
login_form_xpath_id=driver.find_element_by_xpath("//form[@id='loginForm']")
print('Login Form is :')
print(login_form_xpath_absoulute)
print(login_form_xpath_relative)
print(login_form_xpath_id)
#using class
content=driver.find_element_by_class_name('content')
print('Class element is :',content)


driver.close()