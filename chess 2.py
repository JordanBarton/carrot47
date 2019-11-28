import tkinter as tk
import numpy as np

def move(i,j,old_piece):
   
    pieces[i][j]=old_piece
    
    board(pieces)
    
    
    
def select(i,j):
    
    
    old_piece= pieces[i][j]
    
    return old_piece
    
    pieces[i][j]=''
    
    board(pieces)
    
    
    
    
button=np.zeros((8,8))
pieces=np.array([['r','b','k','K','q','k','b','r'],['p','p','p','p','p','p','p','p'],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['p','p','p','p','p','p','p','p'],['r','b','k','K','q','k','b','r']])
old_piece=4
    

master=tk.Tk()
def board(pieces):

    
    
   
    for i in range(0,8):
        for j in range(0,8):
            
            
            button=tk.Button(master, text=pieces[i][j], command= lambda i=i,j=j: select(i,j),height=5,width=10)
            button.grid(row=i,column=j)
            
            
            
            button=tk.Button(master, text=pieces[i][j], command= lambda i=i,j=j: move(i,j,old_piece),height=5,width=10)
            button.grid(row=i,column=j)
            
            
            
            
            

    
    master.mainloop()
    
    pieces=np.rot90(pieces)
    pieces=np.rot90(pieces)
    






board(pieces)




