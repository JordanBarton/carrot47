#chess 3
import tkinter as tk

def change():
     
    button.config(text='b')

window=tk.Tk()
    
for i in range(0,8):
    for j in range(0,8):
     
        button = tk.Button(window,text='a')
        button.grid(row=i,column=j)
        
button = tk.Button(window,text='a',command=change)
button.grid(row=i,column=j)


window.mainloop()