from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import sys

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')

# Initialize the browser in headless mode
driver = webdriver.Chrome(options=chrome_options) # options=chrome_options
driver.get("https://www.google.com")
driver.maximize_window()

buttons = driver.find_elements(By.TAG_NAME, 'button')

# Iterate through the buttons to find the one with the text "test"
for button in buttons:
    if "Odbij" in button.text:
        button.click()  # Click the button
        break  # Stop once we've clicked the button

elem_search = driver.find_element(By.TAG_NAME, "textarea")
elem_search.click()
elem_search.send_keys("What is the main capital of Croatia?", Keys.RETURN)

elem_ans = driver.find_element(By.TAG_NAME, "textarea")
text = elem_ans.text
print(text)

driver.quit()