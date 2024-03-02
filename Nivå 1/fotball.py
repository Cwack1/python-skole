#https://www.fotmob.com/teams/8456/squad/manchester-city

#pip install requests
#pip install bs4
import requests, os, bs4

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}

url = 'https://www.fotmob.com/en-GB/teams/8456/squad/manchester-city'
res = requests.get(url)#, headers=headers)
#bs4 leser og hjelper med å filtrere søk i html kode
soup = bs4.BeautifulSoup(res.text, 'html.parser')

spans = soup.find_all("span", class_="css-10e7ss7-Name e11hu58l0")

for players in spans:
    #Finn teksten mellom <span class...> DENNE TEKSTEN </span>
    navn = players.get_text()

#Skriv ut navnet
    print(navn)
