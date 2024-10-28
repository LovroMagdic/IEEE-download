from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#input_search = str(input("What are you searching for:"))
input_search = "machine learning" # testing purpose
input_search = "%20".join(input_search.split(" "))
rows_per_page = "&rowsPerPage=10" # makes sure that all PDFs on page are downloaded, since there is a limit of 10 per download req
page_number = "&pageNumber=" # need to concate str with number of page, used to make sure all pdf for search results are downloaded
current_page_number = int(1)

chrome_options = Options()
chrome_options.add_argument("--headless") # --headless mode, no GUI

browser = webdriver.Chrome()
browser.get("https://ieeexplore.ieee.org/xpl/conhome/10569139/proceeding") # testing for specific link
time.sleep(5)

try:
    elem_cookie = browser.find_element(By.CSS_SELECTOR, "[class*='osano-cm-button--type_denyAll ']") #osano-cm-button--type_denyAll
    elem_cookie.click()
except:
    pass

time.sleep(3)
elem_next_btn = 1
while elem_next_btn != 0:
    try:
        elem_next_btn = browser.find_element(By.CSS_SELECTOR, "[class*='next-btn']") #next-btn
        elem_next_btn.click()
        second_page_url = browser.current_url # if need to fix getting page number you have to look here
        second_page_url = second_page_url.split("?")
        second_page_url = second_page_url[1]
        second_page_url = second_page_url.split("pageNumber=")
        last_page = int(second_page_url[1])
        time.sleep(10) # it takes a long time to get results, coul be fixed with if getting results present wait
        last_page += 1
    except:
        print(f"There is no next page, {last_page} is last page.")
        elem_next_btn = 0

last_page -= 1 # since it always gets one page more, so we have to -1 to get real result