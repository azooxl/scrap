import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://fr.tradingview.com/markets/stocks-france/market-movers-gainers/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.findAll('tr', class_="row-EdyDtqqh listRow")

with open("fichier.csv", 'w', encoding='utf8', newline='') as f:
    awriter = writer(f)
    header=['Nom de société','Variation en %', 'Prix action', 'Variation','Capitalisation Boursière','Secteur']
    awriter.writerow(header)
    for list in lists:
        title = list.find('a', class_="apply-common-tooltip tickerNameBox-hMpTPJiS tickerName-hMpTPJiS").text
        variationenpct = list.find('span', class_="positive-C2C2Vilj").text
        prix = list.find('span', class_="currency-uW0GcYqJ").text
        variationeneuro = list.find('span', class_="positive-avn2kVRm").text
        capitalisation = list.find('td', class_="cell-TKkxf89L right-TKkxf89L").text
        secteur = list.find('a', class_="link-j5JxgHa0 apply-common-tooltip").text
        info = [title,variationenpct,prix,variationeneuro,capitalisation,secteur]
        awriter.writerow(info)
        
    
    