# IEEE-download
Python script for automating download from IEEE Xplore page. Reading downloaded PDF files and extracting email addresses.<br>
## This script runs on python3 and requires these packages:<br />
<br />

Selenium for navigating IEEE site and downloading:
```
pip install selenium
```
PyPDF2 for reading downloaded PDFs:
```
pip install PyPDF2
```
<br />

Clone repository:
```
git@github.com:LovroMagdic/IEEE-download.git
```

```
python IEEE_download_script.py "provide a link"
```
Downloaded pdf will be downloaded to "./zip" folder.<br />
If download is interrupted report_file will be created in "./report_file" folder containing page where it failed and link provided.<br />

Then run:

```
python pdf_reader_test.py
```
all PDFs in "./zip" folder will be unzipped to "./unzip" and results extracted to "output.txt".<br />