import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from last_element import script # TODO ubacit koristenje script iz last_element.py
import time
import sys

# MAIN - creating threads, downloading from every page in results, doesnt work in headless, TODO add script for finding last page of results

def create_threads(target_function, args_list):
    threads = []
    
    for arg in args_list:
        thread = threading.Thread(target=target_function, args=(arg,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def thread_job(arg):
    print(f"Thread started getting downloads from: {arg}")

    chrome_options = Options()
    chrome_options.add_argument("--headless") # --headless mode, no GUI
    chrome_options.add_argument('--log-level=3')
    browser = webdriver.Chrome()
    browser.get(arg)
    time.sleep(5)
    exit = bool(0) # 0 results FALSE, 1 results TRUE

    #handle cookies
    try:
        elem_cookie = browser.find_element(By.CSS_SELECTOR, "[class*='osano-cm-button--type_denyAll ']") #osano-cm-button--type_denyAll
        elem_cookie.click()
    except:
        pass

    # handler for no results
    try:
        elem_cookie = browser.find_element(By.CSS_SELECTOR, "[class*='List-results-none']") #osano-cm-button--type_denyAll
    except:
        exit = 1

    if not exit:
        print(f"No search results for: {input_search}")
        browser.quit()
        
    else:
        elem_select_all = 0 # flag for checking if select all button showedup
        while elem_select_all == 0:
            try:
                elem_select_all = browser.find_element(By.CSS_SELECTOR, "[class*='results-actions-selectall-checkbox']")  # select all
                elem_select_all.click()
            except:
                print("Couldnt locate select all button, trying again.")
        
        try:
                elem = browser.find_element(By.CSS_SELECTOR, "[class*='download-pdf']")
                elem.click()
        except:
            print(f"Couldnt locate Download PDF button. Check institutional sign in.")
            sys.exit(0)

    
        time.sleep(1)

        # find button to start bulk download
        elem = browser.find_element(By.CSS_SELECTOR, "[class*='stats-SearchResults_BulkPDFDownload']") # downloadpdf-predl-proceed-button stats-SearchResults_BulkPDFDownload xpl-btn-primary
        elem.click()

        elem_close = 0 # flag for waiting download to finish
        while elem_close == 0: # while flag is 0 downloading is still ongoing, 1 download is finished (by download we mean on page creating zip file)
            try:
                elem_close = browser.find_element(By.CSS_SELECTOR, "[class*='modal-close']")
                browser.refresh() # this should be better than just refreshing the page :(
            except:
                pass
        
        time.sleep(5)
        browser.quit()
    print(f"Thread finished getting downloads from: {arg}")

input_search = "machine learning" # testing purpose
input_search = "%20".join(input_search.split(" "))
rows_per_page = "&rowsPerPage=10" # makes sure that all PDFs on page are downloaded, since there is a limit of 10 per download req
page_number = "&pageNumber=" # need to concate str with number of page, used to make sure all pdf for search results are downloaded
current_page_number = 1

max = 10
arg_list = []
for i in range(1,20,1):
    arg_list.append("https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=" + input_search + rows_per_page + page_number + str(current_page_number))
    current_page_number +=1

create_threads(thread_job, arg_list)

#TODO prepoznat koliko stranica rezultata postoji