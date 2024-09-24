import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://seleniumplayground.practiceprobs.com/dogs/breeds/")
driver.implicitly_wait(5)

label=driver.find_element(By.XPATH, '//label[@for="__tabbed_1_2"]')
label.click()

table = driver.find_element(By.TAG_NAME, 'table')
table_data=[]
rows = driver.find_elements(By.XPATH, './/tbody/tr')
for row in rows:
    row_data=[]
    cells = driver.find_elements(By.XPATH, './/td')
    for cell in cells:
        row_data.append(cell.get_attribute('innerHTML'))
    table_data.append(row_data)
print(table_data)
t.sleep(10)
driver.close()