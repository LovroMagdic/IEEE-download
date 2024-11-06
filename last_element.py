from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def script(link):
    # this script finds last page on results page

    chrome_options = Options()
    chrome_options.add_argument("--headless") # --headless mode, no GUI

    browser = webdriver.Chrome()
    browser.get(link) # testing for specific link
    browser.minimize_window()
    time.sleep(5)

    try:
        elem_cookie = browser.find_element(By.CSS_SELECTOR, "[class*='osano-cm-button--type_denyAll ']") #osano-cm-button--type_denyAll
        elem_cookie.click()
    except:
        pass
    #this is used to get sufix from original link and change it to get rowsperpage
    elem_next_btn = browser.find_element(By.CSS_SELECTOR, "[class*='next-btn']") #next-btn
    elem_next_btn.click()
    second_page_url = browser.current_url
    sufix = second_page_url.split("?")[1]
    sufix = sufix.replace("pageNumber=2", "rowsPerPage=10")
    browser.get(link +"?"+ sufix)

    time.sleep(5)
    elem_next_btn = 1
    spinner = 1
    while elem_next_btn != 0:
        try:
            while spinner != 0:
                try:
                    elem_spinner = browser.find_element(By.CSS_SELECTOR, "[class*='fa-spin']")
                    #print("found spinner", elem_spinner)
                except:
                    spinner = 0
                    #print("No spinner im done.")
            elem_next_btn = browser.find_element(By.CSS_SELECTOR, "[class*='next-btn']") #next-btn
            elem_next_btn.click()
            second_page_url = browser.current_url # if need to fix getting page number you have to look here
            second_page_url = second_page_url.split("?")
            second_page_url = second_page_url[1]
            second_page_url = second_page_url.split("pageNumber=")
            last_page = int(second_page_url[1])
            spinner = 1
            #time.sleep(3) # it takes a long time to get results, could be fixed with if getting results present wait
            #last_page += 1
        except:
            print(f"There is no next page, {last_page} is last page.")
            elem_next_btn = 0

    # fas fa-spinner fa-5x fa-spin -- detect spinner
    return last_page

last_page = script("https://ieeexplore.ieee.org/xpl/conhome/10569139/proceeding")