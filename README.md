# suns

SETUP:

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
