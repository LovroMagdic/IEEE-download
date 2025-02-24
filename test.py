import os, hashlib, sys

link2 = "https://ieeexplore.ieee.org/xpl/conhome/10723818/proceeding"
link3 = "lovro.com"
link3 = "neznam123.com"

link = "test.com"


link_hash = hashlib.md5(link.encode()).hexdigest()
folder_path = "./report_file"
report_files = os.listdir(folder_path)

if link_hash + ".txt" in report_files:
    report_file = open("./report_file/" + link_hash + ".txt", "r")
    for line in report_file:
        error_msg = ""
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