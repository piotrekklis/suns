import requests
import json

# get token; username and assword are required
request = requests.post('http://localhost:8000/scraper/get_auth_token/', data = {'username' : 'admin', 'password' : 'admin1234'})
token = json.loads(request.text)
token = token['token']
# create token
token = 'Token ' + token

# example of new currency feed
cf = {'name' : 'GBP', 'link' : 'http://www.ecb.europa.eu/rss/fxref-gbp.html'}
cf = json.dumps(cf)

# get filtered currencies; options are stored in 'http://localhost:8000/scraper/currencyfeeds/' endpoint
request = requests.get('http://localhost:8000/scraper/filteredcurrencies/', headers = {'Authorization' : token}, params = {'targetCurrency' : 'GBP'})
# get all feeds
# request = requests.get('http://localhost:8000/scraper/currencyfeeds/', headers = {'Authorization' : token} )
# post new feed; name and link are required
# request = requests.post('http://localhost:8000/scraper/currencyfeeds/', headers = {'Authorization' : token, 'Content-type' : 'application/json'}, data = cf)
r = json.loads(request.text)
print(r)
