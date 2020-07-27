#currency converter 
import requests
from bs4 import BeautifulSoup

def convert(unit1,unit2):

    URL = 'https://markets.ft.com/data/currencies/tearsheet/summary?s='+ unit1 + unit2
    page = requests.get(URL)
    soup = BeautifulSoup(page.content , "html.parser")
    
    value = soup.find("span",class_="mod-ui-data-list__value")
    value = value.text
    return value

def create_lookup():

    URL = "https://www.iban.com/currency-codes"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,"html.parser")
    table = soup.find("table",class_ = "table table-bordered downloads tablesorter")
    rows = table.find_all("tr")
    n=0
    lookup_table = []
    for row in rows:
        n+=1
        entries = row.find_all("td")
        try:
            lookup_table.append([entries[0].text,entries[1].text,entries[2].text,entries[3].text])
        except:
                pass
    return lookup_table
lookup_table = create_lookup()



print(convert("EUR","USD"))
print(len(lookup_table))