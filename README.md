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
6.11 dovrsen last_element.py, dohavaca zadnju stranicu rezultata pretrazivanje, radi brze, headless nacin testiran i vjerojatno se nece koristit, alternativa je "browser.minimize_window()". <br>