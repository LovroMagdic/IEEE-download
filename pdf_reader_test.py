import os, re, zipfile
from PyPDF2 import PdfReader


output = open("output.txt", "a")
path_zip = "./zip" # path to folder with zipped pdf downloaded, this needs to be defined by user
path_unzip = "./unzip" # path to folder where to unzip downloaded pdfs, this needs to be defined by user
files = os.listdir(path_zip)
for file in files:
    if file != ".DS_Store":
        print(file)
        with zipfile.ZipFile(path_zip + "/" + file, 'r') as zip_ref:
            zip_ref.extractall(path_unzip)

# script used for reading downloaded pdfs and extracting emails
path = path_unzip
files = os.listdir(path)
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
for file in files:
    if file != ".DS_Store": # this is just for MacOS
        output.write(f"In file {file} found:\n")

        reader = PdfReader(path + "/" + file)
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            text = page.extract_text()
            emails = re.findall(email_pattern, text)
            for each in emails:
                output.write(each + "\n")
        output.write("============================\n")

output.write("\n\n\n")