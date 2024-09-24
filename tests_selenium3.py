import time 
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--start-maximized')
#chrome_options.add_argument("--window-size=1920,1080")

# Function to create directories for screenshots
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to take a screenshot of the current page
def take_screenshot(filename):
    driver.save_screenshot(filename)
    print(f"Screenshot saved to {filename}")

base_dir = "screenshots"
create_dir(base_dir)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://seleniumplayground.practiceprobs.com/dogs/")
driver.implicitly_wait(5)
height = driver.execute_script('return document.documentElement.scrollHeight')
width  = driver.execute_script('return document.documentElement.scrollWidth')
driver.set_window_size(width, height)


nav_items = driver.find_elements(By.CSS_SELECTOR, 'ul.md-nav__list li.md-nav__item--active a.md-nav__link')
links=[]
texts=[]
for nav_item in nav_items:
    #print(nav_item.get_attribute('innerHTML'))
    links.append(nav_item.get_attribute('href'))
    texts.append(nav_item.find_element(By.CSS_SELECTOR, 'span.md-ellipsis').text)
    #print(text)
for link, text in zip(links, texts):
    driver.get(link)
    time.sleep(2)  

    filename = f"{base_dir}/{text.replace(' ', '_')}.png"
    
    take_screenshot(filename)
        

driver.close()