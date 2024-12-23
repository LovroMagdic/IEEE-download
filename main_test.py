from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

# MOCK script for downloading pdfs - not used anymore

#input_search = str(input("What are you searching for:"))
input_search = "machine learning" # testing purpose
input_search = "%20".join(input_search.split(" "))
rows_per_page = "&rowsPerPage=10" # makes sure that all PDFs on page are downloaded, since there is a limit of 10 per download req
page_number = "&pageNumber=" # need to concate str with number of page, used to make sure all pdf for search results are downloaded
current_page_number = str(1)

browser = webdriver.Chrome()
browser.get('https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=' + input_search + rows_per_page + page_number + current_page_number)
#browser.get("https://ieeexplore.ieee.org/xpl/conhome/10569139/proceeding") # testing for specific link
browser.maximize_window()
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
  elem = browser.find_element(By.CSS_SELECTOR, "[class*='results-actions-selectall-checkbox']")  # select all
  elem.click()
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
  
  time.sleep(100000)
  browser.quit()