# IEEE-download
Python script for automating download from IEEE Xplore page. Reading downloaded PDF files and extracting email addresses.<br>

## This tool requires these packages:

Selenium for navigating IEEE site and downloading:
```
pip install selenium
```
PyPDF2 for reading downloaded PDFs:
```
pip install PyPDF2
```

## Usage:
Clone repository:
```
git clone git@github.com:LovroMagdic/IEEE-download.git
```
To run script:
```
python IEEE_download_script.py "provided_link"
```
or use in IDE.

Downloaded pdf will be downloaded to "./zip" folder. If download was interrupted or failed report_file will be created in "./report_file" folder.<br>
<br>Report file contains text as followed:
```
34,example_link.com
```

After download is finished run this to unzip files and extract emails;

```
python pdf_reader.py
```
all PDFs in "./zip" folder will be unzipped to "./unzip" and results extracted to "output.txt".<br />