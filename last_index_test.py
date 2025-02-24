from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, re, sys

def ceiling_based_on_last_digit(number):
    if number % 10 == 0:
        return number

    return (number // 10 + 1) * 10

def get_last_index(link):
    chrome_options = Options()
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)

    try:
        elem_cookie = browser.find_element(By.CSS_SELECTOR, "[class*='osano-cm-button--type_denyAll ']") #osano-cm-button--type_denyAll
        elem_cookie.click()
    except:
        pass
    time.sleep(2)
    try:
        elem = browser.find_element(By.CSS_SELECTOR, "[class*='Dashboard-header']") # Dashboard-header col-12
        #elem = browser.find_element(By.CSS_SELECTOR, "[class*='global-margins']") ## col-24-24 Dashboard-section
        elem = elem.get_attribute("innerHTML").splitlines()[0]
        flag = 1
    except:
        print(f"Couldnt locate results div for link > {link}, check if valid link.")
        sys.exit()

    pattern = r'>([^<]+)<'
    matches = re.findall(pattern, elem)
    cleaned_text = ' '.join(match.strip() for match in matches if match.strip())
    cleaned_text = cleaned_text.split(" ")

    if "Showing" in cleaned_text and "for" in cleaned_text:
        num_results = cleaned_text[3]
    elif "Showing" in cleaned_text and "for" not in cleaned_text:
        num_results = cleaned_text[-1]
    elif "No" in cleaned_text and "results" in cleaned_text:
        num_results = None
        print(f"Detected no results for link > {link}")
        flag = 0
    if flag:
        if "," in num_results:
            num_results = int(num_results.replace(",", ""))
        else:
            num_results = int(num_results)

        num_results = int(ceiling_based_on_last_digit(num_results) / 10)

        print(f"For this link > {link}, there are > {num_results} pages of result.")

#script for detecting number of result pages for link

# this was used for testing
links1 = ["https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=mali%20bembo",
         "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=machine%20learning", 
         "https://ieeexplore.ieee.org/xpl/conhome/10723818/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10500516/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10554669/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10662982/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10483273/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10667474/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10663060/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10664657/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10654343/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10735440/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10723818/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10493069/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10542692/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10685652/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10540647/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10605587/proceeding",
         "https://ieeexplore.ieee.org/xpl/conhome/10589922/proceeding"] # 1. search result, 2. conference link, 3. no results

link = "https://ieeexplore.ieee.org/xpl/conhome/10483273/proceeding"

max, fixed_link = get_last_index(link)

print(max)

