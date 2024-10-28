import os
import re
from PyPDF2 import PdfReader

path = "./pdf_examples"
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
            '''text = text.replace("\n", " ")
            for each in text.split(" "):
                if "@" in each:
                    print(each)'''
            for each in emails:
                print(each)
        print("=========================")