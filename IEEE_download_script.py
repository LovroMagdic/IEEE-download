from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, sys, re, os

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

    #this is used to get sufix from original link and change it to get rowsperpage
    #THIS WILL CAUSE PROBLEMS FOR PAGES THAT HAVE RESULTS BUT NOT MULTIPLE PAGES, EXAMPLE: RESULTS OF LESS THAN 10 PDFS
    elem_next_btn = browser.find_element(By.CSS_SELECTOR, "[class*='next-btn']") #next-btn
    elem_next_btn.click()
    second_page_url = browser.current_url
    sufix = second_page_url.split("?")[1]
    sufix = sufix.replace("pageNumber=2", "rowsPerPage=10")
    link_first_page = link + "?" + sufix # this is returned as value to easily iterate pages in the future
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
        return num_results, link_first_page

def download_from_list(testing): # this done without more threads
    # testing -- list of links wo open with browser and get pages, iterates through list

    system_exit = 0
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : '/Users/lovro/Desktop/IEEE-download/zip'} # this needs to be defined by user
    chrome_options.add_experimental_option('prefs', prefs)

    browser = webdriver.Chrome(options=chrome_options)
    for each in testing:
        page_num = each.split("&pageNumber=")
        print(f"Started getting downloads from: {page_num[1]}")

        #browser.minimize_window()
        browser.get(each)
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
            print(f"No search results for: {link}")
            browser.quit()
            
        else:
            elem_select_all = 0 # flag for checking if select all button showedup
            num_try = 0
            while elem_select_all == 0:
                try:
                    elem_select_all = browser.find_element(By.CSS_SELECTOR, "[class*='results-actions-selectall-checkbox']")  # select all
                    elem_select_all.click()
                except:
                    print("Couldnt locate select all button, trying again.")
                    time.sleep(2)
                    num_try += 1

                    if num_try > 10:
                        system_exit = 1
            
            if system_exit == 1:
                sys.exit(0)
            
            try:
                elem = browser.find_element(By.CSS_SELECTOR, "[class*='download-pdf']")
                elem.click()
            except:
                print(f"Couldnt locate Download PDF button. Check institutional sign in.")
                system_exit = 1
            
            if system_exit == 1:
                sys.exit(0)

            time.sleep(1)

            # find button to start bulk download
            elem = browser.find_element(By.CSS_SELECTOR, "[class*='stats-SearchResults_BulkPDFDownload']") # downloadpdf-predl-proceed-button stats-SearchResults_BulkPDFDownload xpl-btn-primary
            elem.click()

            elem_close = 0 # flag for waiting download to finish
            system_exit = 0
            while elem_close == 0: # while flag is 0 downloading is still ongoing, 1 download is finished (by download we mean on page creating zip file)
                try:
                    elem_close = browser.find_element(By.CSS_SELECTOR, "[class*='modal-close']")
                    elem_close_message = browser.find_element(By.CSS_SELECTOR, "[class*='downloadpdf-postdl-msg']") # class="downloadpdf-postdl-msg"
                    elem_close_message = elem_close_message.get_attribute("innerHTML").splitlines()[0]
                    pattern = r'<div[^>]*class="downloadpdf-postdl-msg"[^>]*>(.*?)</div>'

                    result = re.search(pattern, str(elem_close_message))
                    #if result:
                        #print(result.group(1).strip())
                    #print(f"This is message recorded: {elem_close_message}")# this works, needs to check what is returned, for testing this is OK output <div _ngcontent-ng-c4125381912="" class="downloadpdf-postdl-msg"> The items you have selected have been successfully downloaded. </div><!----><!----><!----><!---->
                    result_message = result.group(1).strip()
                    print(f"Message: {result_message}")# this works, needs to check what is returned, for testing this is OK output <div _ngcontent-ng-c4125381912="" class="downloadpdf-postdl-msg"> The items you have selected have been successfully downloaded. </div><!----><!----><!----><!---->
                    if result_message != "The items you have selected have been successfully downloaded.":
                        print("Failed dowloading, exiting process.")
                        report_file = open("report_file.txt", "w")
                        report_link = each.split("?isnumber")[0]
                        report_file.write(f"{page_num},{report_link}")
                        print(f"Download failed for link > {report_link}, last page downloaded > {page_num}") # TODO testing
                        system_exit = 1
                except:
                    pass

                if system_exit:
                    sys.exit(0)
            
            time.sleep(5)
        print(f"Finished getting downloads from: {page_num[1]}")

# MAIN
rows_per_page = "&rowsPerPage=10" # makes sure that all PDFs on page are downloaded, since there is a limit of 10 per download req
page_number = "&pageNumber=" # need to concate str with number of page, used to make sure all pdf for search results are downloaded
initial_page_number = 1
arg_list = []
list_of_urls_to_open = []
start_time = time.time()

link = "https://ieeexplore.ieee.org/xpl/conhome/10723818/proceeding"
print(f"Started script for link > {link}")

#check whether report file exists
file_exists_flag = False
file = "report_file.txt"

if os.path.isfile(file):
    file_exists_flag = True
    f = open(file)
    error_msg = ""
    for line in f:
        error_msg = line.split(",")
    error_code = int(error_msg[0])
    error_link = error_msg[1]

    print(f"Detected report file for link > {error_link}.")

    if link == error_link:
        initial_page_number = error_code
        print(f"Report file and link provided are the same. Do you wish to continue downloading from page > {error_code}?")
        user_response = str(input("(Y/N)?"))

        if user_response.lower() == "y":
            initial_page_number = error_code
        elif user_response.lower() == "n":
            initial_page_number = 1
        else:
            sys.exit(0)

max, fixed_link = get_last_index(link)
print(f"Last page detected {max}, and fixed link > {fixed_link}")

for i in range(initial_page_number,max+1,1):
    full_link = fixed_link + page_number + str(initial_page_number)
    list_of_urls_to_open.append(full_link)
    initial_page_number +=1
download_from_list(list_of_urls_to_open)
print("--- %s seconds ---" % (time.time() - start_time))

# BUG TESTING

# ogromna konferencija https://ieeexplore.ieee.org/xpl/conhome/10723818/proceeding
# bug di ako ima manje od 10 rezultata ne postoji nova stranica ikada pa detektira kao da nema rezultata
# malena konferencija https://ieeexplore.ieee.org/xpl/conhome/10483273/proceeding


#possible message exceptions : Items have not been downloaded because they are either outside of your subscription or not eligible for multiple PDF download.