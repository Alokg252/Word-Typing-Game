from os import startfile
from tkinter import *
from time import sleep
from random import choice
import tkinter.messagebox as msg

words = open("words.txt",'r')
words = words.read()
words = words.split(" , ")

colors = ["#00a5e3","#8dd7bf","#ff96c5","#ff5768","#ffbf65","#fc6238","#ffd872","#f2d4cc","#e77577","#ff828b","#e7c582","#00b0ba",
"#00cdac","#ff6f68","#ffdacc","#ff60ab","#cff800","#ff5c77","#4dd091","#ffec59","#ffa23a",]

start = ["STARTING",'3','2','1','GO']

root = Tk()
root.geometry("1920x610+0+0")
root.title("Fast Typig")
root.iconbitmap(r"F:\Programing\python\python_codes\Icons\Elegantthemes-Beautiful-Flat-One-Color-Keyboard.ico")

canvas1 = Canvas(root, width=1920 ,height=610, bg="#000000")
canvas1.create_rectangle(10,10,1348,600,width=10)

stext = canvas1.create_text(680,280,text="Press 'SPACE' to start",fill="#fc6238",font='calibri 50 bold') # starting text

cx = 1330 # chance x coordinate
cy = 540 # chance y coordinate
cf = "calibri 20 bold" # chance font


def drop(event):

    won_flag = 0    
    c_color = "green"
    # chance is chance+1 because its going to decrease by one on starting 
    chance = 5+1
    score = 0
    
    c = canvas1.create_text(cx,cy,text=chance-1,fill=c_color,font=cf)

    canvas1.delete(stext)
    size = 60

    for i in start:
        s = canvas1.create_text(680,280,text=i,fill="#fc6238",font=f'calibri {size} bold')
        canvas1.update()
        sleep(0.8)
        canvas1.delete(s)
        sleep(0.3)
        canvas1.update()
        size = 100
    
    st = 0.35
    
    sleep(0.5)
    while True:

        word = choice(words)
        color = choice(colors)
        x_axis = choice(range(200,1100,10))        

        f1 = open("word.txt",'r')
        f2 = f1.read()
        
        if f2 != "right":

            chance -= 1

            if chance == 4:
                c_color = "cyan"
            elif chance == 3:
                c_color = "yellow"
            elif chance == 2:
                c_color = "orange"
            elif chance == 1:
                c_color = "red"

            canvas1.delete(c)
            c = canvas1.create_text(cx,cy,text=chance,fill=c_color,font=cf)
            if chance <= 0:

                msg.showerror("LOST",f"YOU LOST THE GAME\nSCORE : {score}")
                startfile("part1.py")
                exit()
        else:
            score+=1

        f1.close()
        f1 = open("word.txt","w")
        f1.write(word)
        f1.close()
        
        sent = canvas1.create_text(x_axis,20,text=word.capitalize(),fill=color,font='consolas 30 bold')
        
        x=0
        y=26

        for t in range(23):
            sleep(st)
            canvas1.move(sent,x,y)
            canvas1.update()

        canvas1.delete(sent)
        
        if st>0.09:
            st -= 0.005
        else:
            if won_flag == 0:
                msg.showinfo("WON",f"YOU WON THE GAME\nSCORE : {score}")
                won_flag = 1
            st = 0.09
        sleep(1.5)
        
canvas1.focus_set()
canvas1.bind("<space>",drop)
canvas1.pack(pady=2)

root.mainloop()