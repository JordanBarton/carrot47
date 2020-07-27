from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def create_template():
    with open('C:/Users/username/Desktop/message.txt' , mode = 'r', encoding = 'utf-8') as template_file:
        content = template_file.read()
        return content
    
# use https://myaccount.google.com/lesssecureapps to authorise emails
    # 465 , 587
    
def send_email(*args):
    sender = 'jordansender.py@gmail.com'
    password = "pythonpython"
    reciever = 'jordan_barton97@hotmail.co.uk' 
    
    bcc = ''
    end = len(args)
    n=0
    for recipient in args:
        n+=1
        bcc += str(recipient) 
        
        if n!=end:
            bcc += ', '
        s

   
        
        
    server = smtplib.SMTP_SSL(host = 'smtp.gmail.com'   )
    
    
    
    server.login(sender , password)
    
    
    
    msg = MIMEMultipart()
    
    message = create_template()
    
    msg['from'] = sender
    msg['to'] = reciever
    #msg['bcc'] = "callum@duncan.pro" # need a nice way of changing who to bbc with a message
    msg['Subject'] = "sent from python"
    
    msg.attach(MIMEText( message, 'plain' ))
    
    server.send_message(msg)
    
    del msg
    
    
send_email("1","2","3")