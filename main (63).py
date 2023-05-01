import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_most_visited_museums'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable sortable'})

rows = table.find_all('tr')

museums = []

for row in rows[1:]:
    data = row.find_all('td')
    name = data[0].text.strip()
    visitors = int(data[2].text.strip().replace(',', ''))
    museums.append((name, visitors))

sorted_museums = sorted(museums, key=lambda x: x[1], reverse=True)

print("The busiest museums in the world are: ")
for i, museum in enumerate(sorted_museums[:10]):
    print(f"{i+1}. {museum[0]} - {museum[1]:,} visitors")
