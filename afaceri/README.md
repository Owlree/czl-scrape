# Ministerul pentru Mediul de Afaceri, Comerț și Antreprenoriat

Surse documente:

* afaceri (NodeJS) - http://www.antreprenoriat.gov.ro/categorie/transparenta-decizionala/proiecte-in-dezbatere-publica/
* aippimm (PHP) - http://www.aippimm.ro/categorie/transparenta-decizionala---modificare-hg-96-2011/

Exista doua scrapere in acest folder, vor fi tratate individual.
### 1. afaceri (NodeJS)
#### Tehnologie
*NodeJS* - serverul se conecteaza la URL-ul setat in fisierul din config, descarca fisierele PDF, parseaza continutul lor, trimite obiectele generate la API si sterge fisierele PDF de pe disc.

#### Instructiuni
Token-ul de autentificare la API trebuie setat in fisierul *config.json*.

Continutul PDF-urilor se proceseaza in paragrafe. Serverul obtine datele necesare din paragraful relevant. Paragraful relevant reprezinta primul paragraf cu un numar total mai mare de 8 cuvinte si 50 de litere (configurabil in *config.json*)
```
npm install
node server/server.js
```

#### Exceptii
Datele documentelor nu exista intr-un format standardizat. Date interpretabile exista in URL-urile fisierelor si in numele acestora.

La fiecare rulare a server-ului, sunt (re)procesate fisierele din URL-ul principal.

### 2. aippimm_plugin (PHP)

#### Tehnologie
*PHP* - Script simplu old-school
#### Instructiuni
Nu necesita instructiuni speciale.

Tokenul va fi transmis ca argument:

```bash
$ php aippimm_plugin.php TOKEN
```
#### Exceptii
Scriptul s-ar putea sa nu functioneze daca se schimba linkul de
'Transparenta decizionala' de pe linkul principal http://www.aippimm.ro/categorie/propuneri_lg/.
Linkul sursa actual (http://www.aippimm.ro/categorie/transparenta-decizionala---modificare-hg-96-2011/)
nu este unul standardizat. Cel mai probabil, nu se va intampla nimic :)

In afara de acest lucru, nu exista situatii speciale.