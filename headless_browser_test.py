from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

#this is just concept to test if driver can run in background(without GUI) and with user using computer (--headless work)



chrome_options = Options()
chrome_options.add_argument("--headless") # --headless mode, no GUI
chrome_options.add_argument('--log-level=3') # should remove log messeges, doesnt work for now

driver = webdriver.Chrome(options=chrome_options) # init driver with options, used for headless
driver.get("https://www.google.com")
driver.maximize_window() # just for testing purposes, will be removed in future

reject_options = ["Odbij", "Reject"]
buttons = driver.find_elements(By.TAG_NAME, 'button') # skip cookies
for button in buttons:
    for option in reject_options:
        if option in button.text:
            button.click()
            break

elem_search = driver.find_element(By.TAG_NAME, "textarea")
elem_search.click()
elem_search.send_keys("What is the main capital of Croatia?", Keys.RETURN)

elem_ans = driver.find_element(By.TAG_NAME, "textarea")
text = elem_ans.text
print(text)

driver.quit()