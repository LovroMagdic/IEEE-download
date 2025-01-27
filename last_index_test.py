from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, re
from PIL import Image

def ceiling_based_on_last_digit(number):
    if number % 10 == 0:
        return number

    return (number // 10 + 1) * 10

links = ["https://ieeexplore.ieee.org/xpl/conhome/10500516/proceeding",
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
"https://ieeexplore.ieee.org/xpl/conhome/10589922/proceeding"]

link = "https://ieeexplore.ieee.org/xpl/conhome/10723818/proceeding"

for link in links:
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

    elem = browser.find_element(By.CSS_SELECTOR, "[class*='global-margins']") ## col-24-24 Dashboard-section
    elem = elem.get_attribute("innerHTML").splitlines()[0]

    pattern = r'>([^<]+)<'
    matches = re.findall(pattern, elem)
    cleaned_text = ' '.join(match.strip() for match in matches if match.strip())
    cleaned_text = cleaned_text.split(" ")
    num_results = cleaned_text[-1]
    if "," in num_results:
        num_results = int(num_results.replace(",", ""))
    else:
        num_results = int(num_results)

    num_results = int(ceiling_based_on_last_digit(num_results) / 10)

    print(f"For this link > {link}, there are > {num_results} pages of result.")