from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
from PyPDF2 import PdfReader

path = "./pdf_examples"
files = os.listdir(path)
for file in files:
    if file != ".DS_Store":
        print(f"In file{file} found:")

        reader = PdfReader(path + "/" + file)
        number_of_pages = len(reader.pages)
        for i in range(number_of_pages):
            page = reader.pages[i]
            text = page.extract_text()
            text = text.replace("\n", " ")
            for each in text.split(" "):
                if "@" in each:
                    print(each)
        print("=========================")


