import time as t
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Button.html')
driver.implicitly_wait(5)

home=driver.find_element(By.ID, 'home')
home.click()
driver.back()
t.sleep(1)

position = driver.find_element(By.ID, 'position').location
print(f"x:{position['x']}, y:{position['y']}")

color = driver.find_element(By.ID, 'color').value_of_css_property("background-color")
print(color)

size = driver.find_element(By.ID, 'size').size
print(f"w:{size['width']}, h:{size['height']}")




driver.close()