from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time

chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

url = "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=kitchen"
driver.get(url)

time.sleep(5)

screenshot_path = "CNN/full_screenshot.png"
driver.save_screenshot(screenshot_path)

# Define the pixel coordinates (x1, y1, x2, y2) for the cropped area
x1, y1, x2, y2 = 60, 650, 473, 688

image = Image.open(screenshot_path)
cropped_image = image.crop((x1, y1, x2, y2))

cropped_screenshot_path = "CNN/cropped_screenshot.png"
cropped_image.save(cropped_screenshot_path)

print(f"Cropped screenshot saved as {cropped_screenshot_path}")

driver.quit()