#pip install requests
#pip install bs4
import requests, os, bs4

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}

url = 'https://pokemondb.net/pokedex/national'
res = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#Finn alle elementene "<a class=ent-name"
divs = soup.find_all("a", class_="ent-name")
#print(divs)
for pokemon in divs:
    #Finn teksten mellom <a class...> DENNE TEKSTEN </a>
    navn = pokemon.get_text()

#Skriv ut navnet
    print(navn)
