import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://seleniumplayground.practiceprobs.com/contact/")
driver.implicitly_wait(5)

options = driver.find_elements(By.CSS_SELECTOR, 'select[name = "role[]"] > option')
option_values=[]
for option in options:
    driver.implicitly_wait(5)
    opt=option.get_attribute("value")
    option_values.append(opt)
for opt in option_values:
    name_field = driver.find_element(By.NAME, "name")  
    name_field.clear()  
    name_field.send_keys("John Doe")

    email_field = driver.find_element(By.NAME, "email")  
    email_field.clear()  
    email_field.send_keys("j.doe@example.com")

    driver.find_element(By.CSS_SELECTOR, 'option[value = "'+ opt+'"]').click()

    file_input = driver.find_element(By.NAME, "file")
    file_name = "dogs_2.jpg"
    file_path = os.path.abspath(file_name)
    file_input.send_keys(file_path)

    msg_field = driver.find_element(By.NAME, "message")  
    msg_field.clear()  
    msg_field.send_keys("All dogs deserve to be loved!")

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Change to your submit button's locator
    submit_button.click()

    driver.find_element(By.ID, "back-link").click()
#print(option_values)




driver.close()