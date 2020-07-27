
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

api_login = "rttapi_XXXXXXXXXXXX"
api_password = "XXXXXXXXXXXXXXXXXXXXX"
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

       

    


        
      
    
