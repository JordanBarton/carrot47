from tkinter import *

BoardValue = ["-","-","-","-","-","-","-","-","-"]

window = Tk()
window.title("Noughts And Crosses")
window.geometry("10x200")

v = StringVar()
Label(window, textvariable=v,pady=10).pack()
v.set("Noughts And Crosses")

def DrawBoard():
    for i, b in enumerate(BoardValue):
        global btn
        if i%3 == 0:
            row_frame = Frame(window)
            row_frame.pack(side="top")
        btn = Button(row_frame, text=b, relief=GROOVE, width=2, command = lambda: PlayMove())
        btn.pack(side="left")

def PlayMove():
    BoardValue[0] = "X"
    btn.destroy()
    DrawBoard()

DrawBoard()
window.mainloop()