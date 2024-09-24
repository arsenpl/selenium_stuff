import time as t
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/table.html')
driver.implicitly_wait(5)

table = driver.find_element(By.ID, 'table_id')

rows = table.find_elements(By.TAG_NAME, 'tr')
rc = len(rows)
print(rc)

columns = rows[0].find_elements(By.TAG_NAME, 'th')
cc = len(columns)
print(cc)
for row in rows:
    tds=row.find_elements(By.TAG_NAME, 'td')
    if(tds[0].get_attribute('innerHTML')=="Learn interact with Elements"):
        print(tds[1].get_attribute('innerHTML'))

    


driver.close()