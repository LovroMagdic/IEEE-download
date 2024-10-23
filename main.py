# https://ukarim.github.io/

from bs4 import BeautifulSoup
from urllib.request import urlopen


from PyPDF2 import PdfReader

reader = PdfReader("pdf_1.pdf")
number_of_pages = len(reader.pages)
for i in range(number_of_pages):
    page = reader.pages[i]
    text = page.extract_text()
    text = text.replace("\n", " ")
    print(text)
    for each in text.split(" "):
        if "@" in each:
            print(each)
    print("======================")



'''

url = "https://ukarim.github.io/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all("a")

for each in tags:
    print(each)
'''

