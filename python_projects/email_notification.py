from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def create_template():
    with open('C:/Users/username/Desktop/message.txt' , mode = 'r', encoding = 'utf-8') as template_file:
        content = template_file.read()
        return content
    
# use https://myaccount.google.com/lesssecureapps to authorise emails
    # 465 , 587
    
def main(*args):
    
    
 
    
    
    from twilio.rest import Client

    account_sid = 'XXXXXXXXXXXXXX'
    auth_token = 'XXXXXXXXXXXXXXXX'
    client = Client(account_sid , auth_token)
    
 
    message = client.messages.create(to = '+44XXXXXXXXX',
                                     from_ = '44+XXXXXXXXX',
                                     body = "code finished")
    
    

    
    
#----------------------------------------------
    sender = 'XXXXXXXX@gmail.com'
    password = "XXXXX"
    reciever = 'XXXXX@hotmail.co.uk' 
    
    bcc = ''
    end = len(args)
    n=0
    for recipient in args:
        n+=1
        bcc += str(recipient) 
        
        if n!=end:
            bcc += ', '
        

   
        
        
    server = smtplib.SMTP_SSL(host = 'smtp.gmail.com'   )
    
    
    
    server.login(sender , password)
    
    
    
    msg = MIMEMultipart()
    
    message = create_template()
    
    msg['from'] = sender
    msg['to'] = reciever
    msg['bcc'] = bcc # need a nice way of changing who to bbc with a message
    msg['Subject'] = "sent from python"
    
    msg.attach(MIMEText( message, 'plain' ))
    
    server.send_message(msg)
    
    del msg
    

