import requests, csv

### dane z API NBP
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data[0]
data = data[0]
data['rates']
## dane do csv
rates = data['rates']
f = open('currency.csv', 'w')
w = csv.writer(f)
w.writerows([r.values() for r in rates])
f.close()