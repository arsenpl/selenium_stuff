import time as t
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Edit.html')
driver.implicitly_wait(5)

email = driver.find_element(By.ID, 'email')
email.clear()
email.send_keys('j.doe@exapmle.com')
#t.sleep(5)

append = driver.find_element(By.XPATH, '//input[@type="text" and @value="Append "]')
append.send_keys('some keys' + Keys.TAB)

username = driver.find_element(By.NAME, 'username')
print(username.get_attribute('value'))

driver.find_element(By.XPATH, '//input[@value="Clear me!!"]').clear()

value=driver.find_element(By.XPATH, '//label[@for="disabled"]/following-sibling::input[1]').get_attribute('disabled')
print(value)

t.sleep(3)
driver.close()