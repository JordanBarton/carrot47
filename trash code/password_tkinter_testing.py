import tkinter as tk

def choose_app():
    x = entry.get() 
    print(x)
    
  
    
    
def view():  
    print("view")
    
def generate():
    print("generate")
    
def close():
    window.destroy()
    exit()
    
window = tk.Tk()
window.title("password manager")
window.configure(background = "black")

#photo1 = tk.PhotoImage(file = "C:/Users/username/Desktop/giphy.gif")
                                                #to the east
#tk.Label( window , image = photo1 , bg = "black").grid(row=0,column=0,sticky='E')


#provide text 
tk.Label( window , text = "enter application", bg = "green" , fg = "white" , font = "none 12 bold").grid(row = 1 , column = 0 , sticky = 'W')

#ask for input
entry = tk.Entry(window, width=20, bg="white")#must do it this way or weird things happen
entry.grid(row=1, column = 1, sticky = "W")

#submit input , must define a click first
user_input = tk.Button(window, text = "Submit", width = 6 , command = choose_app).grid(column = 2, row = 1, sticky = "E")


tk.Button(window, text = "view" , width = 6 , command = view).grid(column = 0 , row = 2 , sticky = "W")
tk.Button(window, text = "generate" , width = 6 , command = generate).grid(column = 0 , row = 3 , sticky = "WW")

output =tk.Text(window , width = 20 , height = 1 , background = "white")
output.grid(row = 2, column = 1, columnspan = 2, sticky = "E")




tk.Button(window, text = "quit" , width = 6 , command = close).grid(column = 0 , row = 6, sticky = "W")

window.mainloop()

