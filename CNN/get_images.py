from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import os

f = open("/Users/lovro/Desktop/IEEE-download/CNN/query.txt", "r")
for each in f:
    each = each.replace("\n", "")

    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    url = "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=" + each
    driver.get(url)
    
    time.sleep(5)

    screenshot_path = "CNN/" + each + ".png"
    driver.save_screenshot(screenshot_path)

    # Define the pixel coordinates (x1, y1, x2, y2) for the cropped area
    x1, y1 = 60, 650
    x2, y2 = 473, 688

    x1, y1 = 60, 600
    x2, y2 = 510, 650

    image = Image.open(screenshot_path)
    cropped_image = image.crop((x1, y1, x2, y2))

    cropped_screenshot_path = "CNN/dataset/" + each + ".png"
    cropped_image.save(cropped_screenshot_path)

    os.remove(screenshot_path)

    driver.quit()