#API_testing
import requests
import csv
import email_notification
#%%%

URL = "http://api.open-notify.org" 
end_point1 = "/iss-now.json"
end_point2 = "/iss-pass.json" #needs latlong to be specified
end_point3 = "/astros.json"

request = requests.get(URL + end_point3)
print(request.status_code)
print(request.text)
request_json = request.json()
print(request_json)
number = request_json["number"]
print(number)
for person in request_json["people"]:
    print(person["name"])






#words is end point by using ?
#according to documentation rel rhy = x finds words that rhyme with x
#URL = "https://api.datamus.com/words?rel rhy=jingle"
#json = -> : 
parameter = {"rel_rhy":"jingle"}
request = requests.get("https://api.datamuse.com/words" , parameter)
print(request.text)
rhyme = []
request_json = request.json()
for entry in request_json:
    rhyme.append(entry["word"])
print(rhyme)




#from twilio.rest import Client

#account_sid = 'AC61c01b3475f3ee650e9f6873e4368fe4'
#auth_token = '5ef76f1eb6f1807a9c0fcceb37f6333d'
#client = Client(account_sid , auth_token)

#msg = "your code has finished"
    
#message = client.messages.create(to = '+447825915787',
                                 #from_ = '+447401273046',
                                 #body = msg)

#%%
import requests
import csv
import email_notification
import datetime
def format_date(date):
    temp = ''
    date_string = str(date)
    for letter in date_string:
        if letter != '-':
            temp+=letter
        else:
            temp+="/"
        
    return temp
format_date(datetime.date(2020,10,10))
#print(message.sid)
print("\n\n\n\n\n")
URL = "http://api.rtt.io/api/v1/json/search/"

api_login = "rttapi_spudsinhell"
api_password = "2fc2475a7ec34500600ec03a8dc34447d0163522"
#data_get = {str(api_login) : str(api_password)}
zero_stations = []
codes = []
with open("C:/Users/username/Desktop/station_codes.csv") as file:
    rows = csv.reader(file)
    for row in rows:
        codes.append(row[1])

n = -1
zero_stations = []
for code in codes:
    n+=1
    if n == 0:
        pass
    if n !=0:
        print(code , n)
        date = datetime.date(2020,7,18)
        flag = False
        while flag == False:
            try:
                request = requests.get(URL + str(code) +"/"+ format_date(date) , auth = (api_login,api_password))
                request_json = request.json()
                services = request_json["services"]
                name = request_json["location"]["name"]
                
                platforms = []
                for entry in services:
                      try:
                          platform = int(entry["locationDetail"]["platform"])
                      except:
                          platform = 467
                          
                      if platform not in platforms:
                          platforms.append(platform)
                         
                flag = True
                
            except:
                date += datetime.timedelta(1)
                if date == datetime.date(2020,7,31):
                    flag = True
             
        
       
        
        try:
            
            if (0 in platforms) or ('0' in platforms):
                print(name)
                zero_stations.append(name)
        except:
            print("error")
                
        
    

print(zero_stations)          
email_notification.main()

#%%

       

    


        
      
    
