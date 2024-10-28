# IEEE-download
Python script for automating download from IEEE Xplore page. Reading downloaded PDF files and extracting email addresses.<br>
TODO:
    - testirat limit downloada po danu<br>
    - zavrsit iteriranje po "page number"<br>
    - isprobat multithreading za download pdf sa svake dostupne stranice - thread("download from page_number=1,..")<br>
    - isprobat download na stranici gdje je prikazano 100 rezultata i skripta pronalazi PDF ikonu i manualno skida jedan po jedan<br>
    - regex za pronalazak mailova u PDFu<br>
<br>
28.10, napisana skripta za malazanje zadnje moguce stranice, radi sporo i ne radi u headless modu, treba postavit handle za getting result dok je prisutan to je vjv problem ne nalaska next-btn elementa <br>