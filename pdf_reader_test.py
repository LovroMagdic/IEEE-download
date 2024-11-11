import os
import re
from PyPDF2 import PdfReader
import zipfile
import time

path_zip = "./zip"
path_unzip = "./unzip"
files = os.listdir(path_zip)
for file in files:
    if file != ".DS_Store":
        print(file)
        with zipfile.ZipFile(path_zip + "/" + file, 'r') as zip_ref:
            zip_ref.extractall("./unzip")

# script used for reading downloaded pdfs and extracting emails

path = "./unzip"
files = os.listdir(path)
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
for file in files:
    if file != ".DS_Store":
        print(f"In file {file} found:")

        reader = PdfReader(path + "/" + file)
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            text = page.extract_text()
            emails = re.findall(email_pattern, text)
            for each in emails:
                print(each)
        print("=========================")