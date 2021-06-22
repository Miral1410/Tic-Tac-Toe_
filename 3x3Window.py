import tkinter
from tkinter import Menu, messagebox

self=tkinter.Tk()
self.title("TIC TAC TOE")
self.minsize(750,500)
self.configure(bg='firebrick1')

#menu start here
menubar=Menu(self)

filemenu=Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="exit", command=self.quit)
menubar.add_cascade(label="file",menu=filemenu)
self.config(menu=menubar)



turn = True

label = tkinter.Label(self, text="3X3 GRID", bg='firebrick1',fg='orange',font=("broadway", 60))
label.pack(side="top", fill="x", pady=10)

label = tkinter.Label(self, text="", bg='firebrick1',fg='white',font=("broadway", 25))
label.place(relx= 0.25, rely= 0.5, anchor= 'e')

label = tkinter.Label(self, text="", bg='firebrick1',fg='white',font=("broadway", 25))
label.place(relx= 0.75, rely= 0.5, anchor= 'w')

def clicked1():
    global turn
    global cell
    if turn == True and t1["text"]==" ":
        t1["text"]="X"
        
        turn = False
        check()
    elif turn == False and t1["text"]==" " :
        t1["text"]="O"
        turn = True
        check()


def clicked2():
    global turn
    global cell
    if turn == True and ["text"]==" ":
        t2["text"]="X"
        
        turn = False
        check()
    elif turn == False and t2["text"]==" " :
        t2["text"]="O"
        turn = True
        check()

def clicked3():
    global turn
    global cell
    if turn == True and t3["text"]==" ":
        t3["text"]="X"
        
        turn = False
        check()
    elif turn == False and t3["text"]==" " :
        t3["text"]="O"
        turn = True 
        check()

def clicked4():
    global turn
    global cell
    if turn == True and t4["text"]==" ":
        t4["text"]="X"
        
        turn = False
        check()
    elif turn == False and t4["text"]==" ":
        t4["text"]="O"
        turn = True 
        check()

def clicked5():
    global turn
    global cell
    if turn == True and t5["text"]==" ":
        t5["text"]="X"
        
        turn = False
        check()
    elif turn == False and t5["text"]==" " :
        t5["text"]="O"
        turn = True  
        check()

def clicked6():
    global turn
    global cell
    if turn == True and t6["text"]==" ":
        t6["text"]="X"
        
        turn = False
        check()
    elif turn == False and t6["text"]==" " :
        t6["text"]="O"
        turn = True 
        check()

def clicked7():
    global turn
    global cell
    if turn == True and t7["text"]==" ":
        t7["text"]="X"
        
        turn = False
        check()
    elif turn == False and t7["text"]==" " :
        t7["text"]="O"
        turn = True 
        check()

def clicked8():
    global turn
    global cell
    if turn == True and t8["text"]==" ":
        t8["text"]="X"
        
        turn = False
        check()
    elif turn == False and t8["text"]==" " :
        t8["text"]="O"
        turn = True  
        check()

def clicked9():
    global turn
    global cell
    if turn == True and t9["text"]==" ":
        t9["text"]="X"
        
        turn = False
        check()
    elif turn == False and t9["text"]==" " :
        t9["text"]="O"
        turn = True 
        check()

count = 1
def check():
    global count
    b1 = t1["text"]
    b2 = t2["text"]
    b3 = t3["text"]
    b4 = t4["text"]
    b5 = t5["text"]
    b6 = t6["text"]
    b7 = t7["text"]
    b8 = t8["text"]
    b9 = t9["text"]
    
    count = count+1

    if b1==b2 and b2==b3 and b1=="O" or b1==b2 and b2==b3 and b1=="X":
        win(t1["text"])

    if b4==b5 and b5==b6 and b6=="O" or b4==b5 and b5==b6 and b4=="X":
        win(t6["text"])

    if b7==b8 and b8==b9 and b7=="O" or b7==b8 and b8==b9 and b7=="X":
        win(t7["text"])

    





    if b1==b4 and b4==b7 and b1=="O" or b1==b4 and b4==b7 and b1=="X":
        win(t1["text"])

    if b2==b5 and b5==b8 and b2=="O" or b2==b5 and b5==b8 and b2=="X":
        win(t2["text"])

    if b3==b6 and b6==b9 and b3=="O" or b3==b6 and b6==b9 and b3=="X":
        win(t3["text"])


    if b1==b5 and b5==b9 and b1=="O" or b1==b5 and b5==b9 and b1=="X":
        win(t1["text"])

    if b7==b5 and b5==b3 and b7=="O" or b7==b5 and b5==b3 and b7=="X":
        win(t7["text"])

    if count == 26:
        ans = "Game Complete Match Tied!!! "
        messagebox.showinfo("Match Tied!!", ans)
        
        t1.config(text=" ")
        t2.config(text=" ")
        t3.config(text=" ")
        t4.config(text=" ")
        t5.config(text=" ")
        t6.config(text=" ")
        t7.config(text=" ")
        t8.config(text=" ")
        t9.config(text=" ")
        

def win(player):
    ans = "Game Complete " +player +"Wins!! "
    messagebox.showinfo("Congratulations!!", ans)
    #self.destroy()
    t1.config(text=" ")
    t2.config(text=" ")
    t3.config(text=" ")
    t4.config(text=" ")
    t5.config(text=" ")
    t6.config(text=" ")
    t7.config(text=" ")
    t8.config(text=" ")
    t9.config(text=" ")
    

t1=tkinter.Button(self,text=" ",font=("forte"),bg='orange',fg='firebrick1',height = 4, width = 8,command=clicked1)
t1.place(relx= 0.45, rely= 0.475, anchor= 'se')
        
t2=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 4, width = 8, command=clicked2)
t2.place(relx= 0.5, rely= 0.475, anchor= 's')
        
t3=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 4, width = 8, command=clicked3)
t3.place(relx= 0.55, rely= 0.475, anchor= 'sw')
    
t4=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 4, width = 8, command=clicked4)
t4.place(relx= 0.45, rely= 0.55, anchor= 'e')
        
t5=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 4, width = 8, command=clicked5)
t5.place(relx= 0.5, rely= 0.55, anchor= 'center')

t6=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 4, width = 8, command=clicked6)  
t6.place(relx= 0.55, rely= 0.55, anchor= 'w')
        
t7=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 4, width = 8, command=clicked7)
t7.place(relx= 0.45, rely= 0.625, anchor= 'ne')
        
t8=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 4, width = 8, command=clicked8)
t8.place(relx= 0.5, rely= 0.625, anchor= 'n')
        
t9=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 4, width = 8, command=clicked9)
t9.place(relx= 0.55, rely= 0.625, anchor= 'nw')


self.mainloop()

