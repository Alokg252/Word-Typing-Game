from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("1920x80+0+600")
root.title("Entry Box")
root.iconbitmap(r"F:\Programing\python\python_codes\Icons\Elegantthemes-Beautiful-Flat-One-Color-Keyboard.ico")
root.config(bg="#88ff88")

w=1360
h=80
canvas1= Canvas(root, width=w ,height=h, bg="#88ff88")
v1 = StringVar()

def check(event):
    f1 = open("word.txt","r")
    f2 = f1.read()
    f1.close()

    if f2 == v1.get():
        f1 = open("word.txt","w")
        f1.write("right")
        f1.close()
        msg.showinfo()
    
    else:
        msg.showwarning()     
        

    v1.set('')
    entrybox.update()

canvas1.pack()

entrybox = Entry(canvas1, bg="#bbbbbb", fg="black",textvariable=v1, font="calibri 20 bold", bd=2, width=50)
entrybox.pack(pady=(10,0,), ipady=10)
entrybox.bind("<Return>", check)
root.mainloop()