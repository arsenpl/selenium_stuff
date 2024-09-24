import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://seleniumplayground.practiceprobs.com/")


driver.fullscreen_window()

search_field = driver.find_element(By.NAME, "query")

search_field.send_keys("Breed")

results = driver.find_elements(By.CLASS_NAME, "md-search-result__item")
html_results = [res.get_attribute("innerHTML") for res in results]

driver.close()

links = []
for res in html_results:
    if "Akita Inu" in res:
        split_res = res.split("href=")
        link_part = split_res[1]
        links.append(link_part.split('"')[1])

print(links)
# ['https://seleniumplayground.practiceprobs.com/dogs/breeds/akita/']

