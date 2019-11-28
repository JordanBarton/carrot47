import tkinter as tk
import numpy as np
     
    #wpawn = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\bpawn.png")      
    #wknight = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\bpawn.png")
    #wbishop = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\bpawn.png")  
    #wrook = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\bpawn.png")  
    #wqueen = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\bpawn.png")  
    #wking = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\bpawn.png")  
    
    #bpawn = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\brook.png")      
    #bknight = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\brook.png")
    #bbishop = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\brook.png")  
    #brook = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\brook.png")  
    #bqueen = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\brook.png")  
   # bking = tk.PhotoImage(file = r"C:\Users\username\OneDrive\python\brook.png")  

def odd(a,b):
    x=100
    y=200
    if (a % 2 ==0):#a is even
        x=1
    
    if (b % 2 ==0):#b is even
        y=1
        
    if (a % 2 !=0):#a is odd
        x=0
    
    if (b % 2 !=0):#b is odd 
        y=0
        

        
    if x==y:
        
        return 1
    
    if x!=y:
        
        return 0
        

    
   
    
def move(i,j,old_piece):
   
    pieces[i][j]=old_piece
    
def select(i,j):
    
    global old_piece
    old_piece= pieces[i][j]
    
    pieces[i][j]=''
    
   


button=np.zeros((8,8))
pieces=np.array([['r','b','k','K','q','k','b','r'],['p','p','p','p','p','p','p','p'],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['p','p','p','p','p','p','p','p'],['r','b','k','K','q','k','b','r']])
old_piece=4
t=0

master=tk.Tk()
while t!=1:
    
    
    

   
    for i in range(0,8):
        for j in range(0,8):
            
            if odd(i,j)==1:
                
           
                button=tk.Button(master, text=pieces[i][j], command= lambda i=i,j=j: select(i,j),height=5,width=10,bg='brown')
            
            else:
                
                button=tk.Button(master, text=pieces[i][j], command= lambda i=i,j=j: select(i,j),height=5,width=10,bg='beige')
            
            button.grid(row=i,column=j)
            
        
    master.mainloop()
    
    
    
    
    

    
    master=tk.Tk()
    
    for i in range(0,8):
        for j in range(0,8):
            
            
            if odd(i,j)==1:
            
                button=tk.Button(master, text=pieces[i][j], command= lambda i=i,j=j: move(i,j,old_piece),height=5,width=10,bg='brown')
            
            else:
            
                button=tk.Button(master, text=pieces[i][j], command= lambda i=i,j=j: move(i,j,old_piece),height=5,width=10,bg='beige')
            
            
            
            button.grid(row=i,column=j)
    
    master.mainloop()
    
    pieces=np.rot90(pieces)
    pieces=np.rot90(pieces)
    


