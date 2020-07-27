from sqlalchemy import create_engine , func
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship , backref

from datetime import date
from random import shuffle

import tkinter as tk

def login():
    login.url ='postgresql://{}:{}@localhost:5432/password_management'.format(sql_username.get(),sql_password.get())
    verify.destroy()
 
    
    
def view():  
    app = entry.get() 
    username = username_entry.get()
    view_entries = session.query(UserDetails)\
           .filter( UserDetails.application == app )\
           .filter( UserDetails.username == username)\
           .all()
    n = 0
    for entries in view_entries:
        tk.Label( window , text = entries.password, bg = "white" , fg = "red" , font = "none 12 bold")\
        .grid(row = 7+n , column = 0 , sticky = 'W')
        n+=1
        print(entries.password)
       
    
    
def generate():
    n_upper = 4
    n_number = 3
    n_symbols = 3
    length = 14
    name = username_entry.get()
    app = entry.get() 
    session.add(UserDetails(app,
                            name,
                            generate_password(int(n_upper),
                                              int(n_number),
                                              int(n_symbols),
                                              int(length))))
    
    
    
    
def close():
    window.destroy()
    exit()
    







def shuffle_and_take(characters):
    shuffle(characters)
    return characters[0]


def generate_password(n_upper , n_number , n_symbol , length ):
    
    numbers= ['1,' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '0']
    upper=[]
    lower=[]
    for i in range(1,27):
        upper.append(chr(ord('@')+i))
        lower.append(chr(ord('`')+i))
        
    symbols= ['!' , '"' , '£' , '$' , '%' , '^' , '&' , '*' , '(' , ')' , '-' , '_' ,
              '+' , '=' ,'{' , '}' , '[' , ']' , ':' , ';' , '@' , "'" , '~' , '#',
              '<' , '>' , ',' , '.' , '/' , '?' , '|' , '\\' , '' , '' , '' , '']
    
    
    shuffle(upper)
    shuffle(lower)
    shuffle(numbers)
    shuffle(symbols)
    
    

    
    password_array = []
    for i in range( 0 , length ): 
        if 0 <= i < n_upper:
            password_array.append(shuffle_and_take(upper))
        if n_upper <= i <( n_upper + n_number):
            password_array.append(shuffle_and_take(numbers))
        if (n_upper + n_number) <= i < (n_upper + n_number + n_symbol):
            password_array.append(shuffle_and_take(symbols))
        if i >= n_upper + n_number + n_symbol:
            password_array.append(shuffle_and_take(lower))
        shuffle(password_array)
        
    
    password = ''
    for letter in password_array:
        password += str(letter)
        
    return password




#'sqlite:///:memory:'

verify = tk.Tk()
sql_username= tk.Entry(verify, width=20, bg="white")#must do it this way or weird things happen
sql_username.grid(row=1, column = 0, sticky = "W")

sql_password = tk.Entry(verify, width = 20 ,bg = "white" , show = "*")
sql_password.grid(row=3, column = 0 , sticky = "W")

user_input = tk.Button(verify, text = "Submit", width = 6 , command = login).grid(column = 0, row = 4, sticky = "E")


verify.mainloop()
 

engine = create_engine(login.url)      
Session = sessionmaker(bind=engine)
Base = declarative_base()



class UserDetails(Base):
    
    __tablename__ = "user_details"
    
    id = Column(Integer , primary_key = True)
    application = Column(String)
    username = Column(String)
    password = Column(String)
    
    def __init__(self,application,username,password):
        self.application = application
        self.username    = username
        self.password    = password
    

Base.metadata.create_all(engine)
session = Session()




window = tk.Tk()
window.title("password manager")
window.configure(background = "black")

#photo1 = tk.PhotoImage(file = "C:/Users/username/Desktop/giphy.gif")
                                                #to the east
#tk.Label( window , image = photo1 , bg = "black").grid(row=0,column=0,sticky='E')


#provide text 
tk.Label( window , text = "enter application", bg = "green" , fg = "white" , font = "none 12 bold").grid(row = 0 , column = 0 , sticky = 'W')

#ask for input
entry = tk.Entry(window, width=20, bg="white")#must do it this way or weird things happen
entry.grid(row=1, column = 0, sticky = "W")

tk.Label( window , text = "", bg = "black" , fg = "black" ).grid(row = 2 , column = 0 , sticky = 'W')

tk.Label( window , text = "enter username", bg = "green" , fg = "white" , font = "none 12 bold").grid(row = 3 , column = 0 , sticky = 'W')


username_entry = tk.Entry(window , width = 20 , bg = "white")
username_entry.grid(row = 4 , column = 0 , sticky = "W")
#submit input , must define a click first
#user_input = tk.Button(window, text = "Submit", width = 6 , command = choose_app).grid(column = 2, row = 1, sticky = "E")


tk.Button(window, text = "view" , width = 6 , command = view).grid(column = 0 , row = 5 , sticky = "E")
tk.Button(window, text = "generate" , width = 6 , command = generate).grid(column = 0 , row = 5 , sticky = "W")

#output =tk.Text(window , width = 20 , height = 1 , background = "white")
#output.grid(row = 2, column = 1, columnspan = 2, sticky = "W")




tk.Button(window, text = "quit" , width = 6 , command = close).grid(column = 0 , row = 6, sticky = "W")

window.mainloop()



session.commit()
session.close()




