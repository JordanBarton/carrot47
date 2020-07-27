import requests
from bs4 import BeautifulSoup
import re



       
   

    
    
    
    
    
    
    
    
URL = "https://www.indeed.co.uk/jobs?q=&l=Manchester+M12"


page = requests.get(URL)

soup = BeautifulSoup(page.content , 'html.parser')

body  = soup.find(id = "resultsCol")

cards = body.find_all('div', class_="jobsearch-SerpJobCard unifiedRow row result")
    
    
for card in cards:
        print(card.find("span",class_="company").text.strip())