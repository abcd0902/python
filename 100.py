##def Season(n) :
##    if n>=3 and n<=5 :
##        print("spring")
##    if n>=6 and n<=8 :
##        print("summer")
##    if n>=9 and n<=11 :
##        print("fall")
##    if n==12 or n==1 or n==2:
##        print("winter")
##n = int(input())
##Season(n)
##from tkinter import *
##win = Tk()
##label1 = Label(win,text = "one")
##label2 = Label(win,text = "two")
##label3 = Label(win,text = "three")
##label1.pack()
##label2.pack()
##label3.pack()
##win.mainloop()
##win = Tk()
##lbl1 = Label(win,text = "orange",width = 20,height = 3,relief = "solid")
##lbl2 = Label(win,text = "banana",font = ("궁서",20),bg = "yellow")
##lbl3 = Label(win,text = "apple",fg = "red")
##lbl1.pack()
##lbl2.pack()
##lbl3.pack()
##win.mainloop()
##from tkinter import *

##win = Tk()
##img = PhotoImage(file = 'pizza.png')
##lbl1 = Label(win,image = img)
##lbl2 = Label(win,text = "pizza",fg = "red",bg = "yellow")
##lbl1.pack()
##lbl2.pack()
##win.mainloop()

##win = Tk()
##btn = Button(win,text = "Butten",bg = "black",fg = "white")
##btn.pack()
##win.mainloop()
##from tkinter import *
##
##win = Tk()
##
##def click() :
##    if btn['text'] == "red" :
##        btn['text'] = "blue"
##        btn['bg'] = "blue"
##    else :
##         btn['text'] = "red"
##         btn['bg'] = "red"  
##btn = Button(win,text = "red",fg = "white",bg =  "red",command = click)
##btn.pack()
##win.mainloop()
##from tkinter import *
##
##win = Tk()
##
##def click() :
##    if lbl['text'] == "hello" :
##        lbl['text'] = "python"
##        lbl['bg'] = "green"
##    else :
##         lbl['text'] = "hello"
##         lbl['bg'] = "orange"
##lbl = Label(win,text = "hello",fg = "white",bg =  "orange")
##lbl.pack()
##btn = Button(win,text = "button",command = click)
##btn.pack()
##win.mainloop()
##from tkinter import *
##
##win = Tk()
##win.title("grid")
##
##lade11 = Label(win,width=10,height =5,bg = "red")
##lade12 = Label(win,width=10,height =5,bg = "orange")
##lade13 = Label(win,width=10,height =5,bg = "yellow")
##lade14 = Label(win,width=10,height =5,bg = "green")
##lade15 = Label(win,width=10,height =5,bg = "blue")
##lade16 = Label(win,width=10,height =5,bg = "purple")
##
##lade11.grid(row = 0,column = 0)
##lade12.grid(row = 0,column = 11)
##lade13.grid(row = 0,column = 21)
##lade14.grid(row = 6,column = 0)
##lade15.grid(row = 6,column = 11)
##lade16.grid(row = 6,column = 21)
##win.mainloop()
##from tkinter import*
##win = Tk()
##
##def message(event):
##    lbl['text'] = entry.get()
##
##def clear(event):
##    lbl['text'] = ' '
##entry = Entry(win)
##entry.bind("<Return>",message)
##entry.bind("<Delete>",clear)
##entry.pack()
##lbl = Label(win,text=  "")
##lbl.pack()
##from tkinter import *
##
##win = Tk()
##win.title("grid")
##
##lade11 = Label(win,width=10,height =5,bg = "red")
##lade12 = Label(win,width=10,height =5,bg = "orange")
##lade13 = Label(win,width=10,height =5,bg = "yellow")
##lade14 = Label(win,width=10,height =5,bg = "green")
##lade15 = Label(win,width=10,height =5,bg = "blue")
##lade16 = Label(win,width=10,height =5,bg = "purple")
##
##lade11.grid(row = 0,column = 0)
##lade12.grid(row = 0,column = 1)
##lade13.grid(row = 0,column = 2)
##lade14.grid(row = 1,column = 0)
##lade15.grid(row = 1,column = 1)
##lade16.grid(row = 1,column = 2)
##win.mainloop()
##int c,b
##a = int(input())
##b = int(input())
##add = lambda x, y  : x + y
##print(add(10,100))
##
##aaa = lambda a,b : a%b
##print(aaa(10,2))

##apple = lambda name : print("Hello "+name)
##apple(input())

##from tkinter import*
##
##def Click(shape):
##    if shape == "circle":
##        img = PhotoImage(file = "circle.png")
##    elif shape == "triangle":
##        img = PhotoImage(file = "triangle.png")
##    else:
##        img = PhotoImage(file = "star.png")
##    lbl['image'] = img
##    lbl.image = img
##
##win = Tk()
##
##img = PhotoImage(file = "circle.png")
##lbl = Label(win,image = img)
##btn1 = Button(win,text = "circle",command = lambda : Click("circle"))
##btn2 = Button(win,text = "triangle",command = lambda : Click("triangle"))
##btn3 = Button(win,text = "star",command = lambda : Click("star"))
##
##lbl.grid(row = 0,column = 0,columnspan =3)
##btn1.grid(row = 1,column =0)
##btn2.grid(row = 1,column =1)
##btn3.grid(row = 1,column =2)
from tkinter import*
from random import *

def Click(shape):
    if shape == "rock":
        img = PhotoImage(file = "rock.png")
    elif shape == "scissors":
        img = PhotoImage(file = "scissors.png")
    else:
        img = PhotoImage(file = "paper.png")
    lbl_User['image'] = img
    lbl_User.image = img


def change_img(user):
    List = ["scissors.png","rock.png","paper.png"]
    com = randint(0,2)

    com_img = PhotoImage(file = List[com])
    user_img = PhotoImage(file = List[user])

    lbl_com['image']  = com_img
    lbl_com.image  = com_img

    lbl_User['image']  = user_img
    lbl_User.image  = user_img

    game(com,user)

def game(com,user):
    if com==User:
        lbl_res['text'] = "Draw"
    else:
        if com == 0:
            if user == 1:
                lbl_res['text'] = "User win!"

win = Tk()
win.title("Rock Scissors Paper Game")

basic_img = PhotoImage(file = "ready.png")
lbl_com = Label(win,image = basic_img,relief = "solid")
lbl_User = Label(win,image = basic_img,relief = "solid")
lbl_name1 = Label(win,text = "computer",width = 15,font = ("궁서",20))
lbl_name2 = Label(win,text = "user",width = 15,font = ("궁서",20))
lbl_res = Label(win,text = " ",width =15,bg = "lightyellow",fg="brown",font =("궁서",20,"bold"))
btn1 = Button(win,text = "scissors",width = 15,bg = "sky blue",command = lambda : change_img(0))
btn2 = Button(win,text = "rock",width = 15,bg = "pink",command = lambda : change_img(1))
btn3 = Button(win,text = "paper",width = 15,bg = "light green",command = lambda : change_img(2))


lbl_com.grid(row = 0,column = 0)
lbl_res.grid(row =0,column =1)
lbl_User.grid(row = 0,column = 2)
lbl_name1.grid(row = 1,column =0)
lbl_name2.grid(row = 1,column =2)
btn1.grid(row = 2,column =0)
btn2.grid(row = 2,column =1)
btn3.grid(row = 2,column =2)











































































































































































































































































































































































































































































