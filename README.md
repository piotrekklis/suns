# suns

<b>SETUP:</b>

Python 3.6.4

Django              2.0.5

django-filter       2.0.0

djangorestframework 3.9.0

xmltodict           0.11.0

python-dateutil     2.7.2

requests            2.18.4

<br>
<b>FUNKCJONALNOŚCI:</b>

  1. Parsowanie feedów
  2. Dodawanie kolejnych feedów
  3. REST API z endpointami:
  
      a) http://localhost:8000/scraper/filteredcurrencies/ - do pobierania kursów walut (jeden endpoint z opcją filtrowania po 'targetCurrency')
      
      b) http://localhost:8000/scraper/currencyfeeds/ - do pobierania listy feedów z aplikacji oraz do dodawania nowych feedów
      
  4. Uwierzytelnianie z użyciem tokena


<br>
<b>TESTOWANIE:</b>

<br>
1. Autoryzacja:

POST: http://localhost:8000/scraper/get_auth_token/

z 'username' i 'password';

jeżeli użytkownik o podanej nazwie z pasującym do użytkownika hasłe istnieje, to zostanie zwrócony token

<br>
2. Nowy feed:

POST: http://localhost:8000/scraper/currencyfeeds/

header powinien zawierać:

'Authorization' z tokenem w postaci 'Token vhhc9u2kyec8qurt6vmws7grf2p28zr55swpcve2';

'Content-type' : 'application/json';


oraz koniecznie 'name' i 'link', czyli nazwę waluty oraz link skąd pobrać dane o walucie

<br>
3. Informacja o walutach jakie są dostępne:

GET: http://localhost:8000/scraper/currencyfeeds/

header powinien zawierać:

'Authorization' z tokenem w postaci 'Token vhhc9u2kyec8qurt6vmws7grf2p28zr55swpcve2';

<br>
4. Dane o wybranej walucie:

GET: http://localhost:8000/scraper/filteredcurrencies/

header powinien zawierać:

'Authorization' z tokenem w postaci 'Token vhhc9u2kyec8qurt6vmws7grf2p28zr55swpcve2';

oraz w parametrach ?targetCurrency=PLN (lub inną wybraną, dostępną walutę)

<br>
5. Parsowanie feedów:

Uruhomienie parsera poprzez wejście na adres: http://localhost:8000/scraper/


