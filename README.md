# IEEE-download
Python script for automating download from IEEE Xplore page. Reading downloaded PDF files and extracting email addresses.<br>
<br>
TODO:
    - testirat limit downloada po danu -- DONE<br>
    - zavrsit iteriranje po "page number" -- DONE<br> 
    - regex za pronalazak mailova u PDFu -- DONE<br>
    - isprobat multithreading za download pdf sa svake dostupne stranice - thread("download from page_number=1,..") -- DONE<br>
    <br>
    <br>
    - isprobat download na stranici gdje je prikazano 100 rezultata i skripta pronalazi PDF ikonu i manualno skida jedan po jedan<br>

<br>
11.11 prva u potpunosti funkcionalna verzija "IEEE_download_script.py", odbacen nacin koristenja vise dretvi, trenutno se koristi iteriranje, za ~ 370 rezultata treba oko ~15min.<br>