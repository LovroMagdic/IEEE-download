from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

link = "https://ieeexplore.ieee.org/xpl/conhome/10723818/proceeding"

chrome_options = Options()
browser = webdriver.Chrome()
browser.get(link) # testing for specific link

elem = browser.find_element(By.CSS_SELECTOR, "[class*='Dashboard-section-gray']") ## Dashboard-section Dashboard-section-gray text-base-md-lh

location = elem.location
size = elem.size
w, h = size['width'], size['height']

print(location)
print(size)
print(w, h)