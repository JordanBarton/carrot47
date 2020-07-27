
import email_notification
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine , func
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship , backref
import re


def remove_duplicates():
    
    distinct = session.query(func.count(JobDetails.title),JobDetails.title, JobDetails.company,JobDetails.url,JobDetails.score,JobDetails.age,JobDetails.indeed_apply)\
    .group_by(JobDetails.title, JobDetails.company,JobDetails.url,JobDetails.score,JobDetails.age,JobDetails.indeed_apply)\
    .all()
    session.query(JobDetails).delete()
   
    for row in distinct:
        
        session.add(JobDetails(row.title,row.age,  row.url,search_page(row.url) , indeed_apply(row.url),row.company))
        session.commit()

def indeed_apply(URL):
         page = requests.get(URL)
         soup = BeautifulSoup(page.content , 'html.parser')
         indeed_apply = False
         try:
                if soup.find(id = "indeedApplyButtonContainer").text:
                    indeed_apply = True
                
         except:
                pass
            
         return str(indeed_apply)

def search_page(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content , 'html.parser')
    description = soup.find(id = "jobDescriptionText")
    try:
        text = description.text.strip()
    except:
        text = 'blank'

    #negative_words = "years"+"|"+"experience"+"|"+"strong"+"|"+"written"
    
    negative_words = ["years","experience","java","javascript","html",
                      "computer science","git","css","aws","node.js","previous","WCF"]
    negative_words = "|".join(negative_words)
   
    positive_words = ["training","python","no experience","no experience",
                      "physics","STEM","covid","coronavirus","passionate",
                      "analytical","opportunities","learn","communication"]
    positive_words = "|".join(positive_words)
    
    negatives = re.findall(negative_words,text)
    positives = re.findall(positive_words,text)
    
    
    
    value = len(positives) - len(negatives)
    
    return value
        

def filter_(title,url,age,company):
    
    title_flag = False
    url_flag = True
    age_flag = False
    repeat_flag = True
    keywords = ["software","junior","developer","java","python","SQL",
                "accountant","analyst","data",'javascript']
    blacklist = ["senior","c#","php","desk","epr","warehouse","principal",
                 "android","lead","wbf","mobile","front","back","head","fix",
                 "owner","lecturer","pension","wpf",".net",'java']
    for word in keywords:
        if word in title.lower():
            title_flag = True
    
    for word in blacklist:
        if word in title.lower():
            title_flag = False
    
    
    
    nums = ''
    for char in age:
        try:
            int(char)
            nums += char
        except:
            pass

    
    try:
        nums = int(nums)
         
        if int(nums) <3:
            age_flag = True
    except:
        pass
    
 
    for job in job_db:
        
        if str(url) == str(job.url):
            url_flag = False
            break
   
        
    for job in job_db:
        
        if str(company) == str(job.company) and str(title) == str(job.title):
            
            repeat_flag = False
           
            break
   
        
    print(company,job.company , title, job.title , repeat_flag)
        
    #add a name&company check to eliminate multiple job postings
    if url_flag == True and age_flag == True and title_flag == True and repeat_flag == True:
        return True
    else:
        return False
       
    
   



def get_jobs(URL):
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content , 'html.parser')
    
    body  = soup.find(id = "resultsCol")
    
    cards = body.find_all('div', class_="jobsearch-SerpJobCard unifiedRow row result")
    
    
    for card in cards:
            
            title_card = card.find("h2",class_ = "title")
            footer_card = card.find("div", class_="jobsearch-SerpJobCard-footer")
            
            url_extension = title_card.find("a")["href"]
            title = title_card.find("a")["title"]
            age = footer_card.find("span",class_="date").text.strip()
            
            #need to fix this
            try:
                company = card.find("span",class_="company").text.strip()
            except:
                company= "unknown"
            
            url = 'https://www.indeed.co.uk' + url_extension
          
       
         
            #need to now check whether to add or not
            flag = filter_(title,url,age,company)
            if flag == True:
                session.add(JobDetails(title,age,  url,search_page(url) , indeed_apply(url),company))
                session.commit()
            else:
                pass



sql_username = "jordan"
sql_password = "password"
login_url ='postgresql://{}:{}@localhost:5432/jobs'.format(sql_username,sql_password)
engine = create_engine(login_url)      
Session = sessionmaker(bind=engine)
Base = declarative_base()



class JobDetails(Base):
    
    __tablename__ = "job_details"
    
    id = Column(Integer , primary_key = True)
    title = Column(String)
    age = Column(String)
    url = Column(String)
    score = Column(Integer)
    indeed_apply = Column(String)
    company = Column(String)
    
    def __init__(self,title,age,url,score,indeed_apply,company):
        self.title = title
        self.age = age
        self.url = url
        self.score = score
        self.indeed_apply = indeed_apply
        self.company = company
    



def searchjobtype(job):
    site = "https://www.indeed.co.uk/jobs?"
    where = "&l=Manchester+M12&radius=15&start="
    URL = site+job+where+'0'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content , 'html.parser')
    body  = soup.find(id = "resultsCol")
    njobs_string = body.find(id="searchCountPages").text.strip()
    
    result = [x.strip() for x in njobs_string.split(' ')]
    numbers = ""
    for value in result:
        value = "{}".format(value)
        for character in value:
            try:
                int(character)
                numbers+= character
            except:
                pass
    number_of_entries = int(numbers[1:])/17
    print(number_of_entries)
    number_of_pages = round(number_of_entries+1)

    for i in range(0,number_of_pages):
   
        URL = site+job+where+"{}".format(10*i)
        get_jobs(URL)











Base.metadata.create_all(engine)
session = Session()
job_db = session.query(JobDetails).all()

jobs = ["q=software",
        'q=analyst',
        'q=developer',
        'q=python',
        'q=data']

#remove_duplicates()
    
    


for job in jobs:
    searchjobtype(job)
    

session.close()
email_notification.main()

#https://www.google.com/maps/dir/Seddon+St,+Levenshulme,+Manchester+M12+4GP/Altrincham