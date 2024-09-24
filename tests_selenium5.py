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

base_dir = "screenshots_full"
create_dir(base_dir)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://seleniumplayground.practiceprobs.com/dogs/")
driver.implicitly_wait(5)
height = driver.execute_script('return document.documentElement.scrollHeight')
width  = driver.execute_script('return document.documentElement.scrollWidth')
driver.set_window_size(width, height)

tab_items = driver.find_elements(By.CSS_SELECTOR, 'ul.md-tabs__list a.md-tabs__link')
pages=[]
for tab_item in tab_items:
    pages.append(tab_item.get_attribute('href'))
    print(pages)
for page in pages:
    driver.get(page)
    time.sleep(3)
    nav_items = driver.find_elements(By.CSS_SELECTOR, 'ul.md-nav__list li.md-nav__item--active a.md-nav__link')
    if(nav_items):
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
            try:
                summary = driver.find_element(By.TAG_NAME, 'summary')
                print(summary.get_attribute('innerHTML'))
                if(summary):
                    summary.click()
            except:
                print('nope')
            filename = f"{base_dir}/{text.replace(' ', '_')}.png"
            
            take_screenshot(filename)
           

driver.close()