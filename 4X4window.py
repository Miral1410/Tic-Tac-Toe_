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


cell = ''
turn = True

label = tkinter.Label(self, text="4X4 GRID", bg='firebrick1',fg='orange',font=("broadway", 60))
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

def clicked10():
    global turn
    global cell
    if turn == True and t10["text"]==" ":
        t10["text"]="X"
        
        turn = False
        check()
    elif turn == False and t10["text"]==" " :
        t10["text"]="O"
        turn = True 
        check()

def clicked11():
    global turn
    global cell
    if turn == True and t11["text"]==" ":
        t11["text"]="X"
        
        turn = False
        check()
    elif turn == False and t11["text"]==" " :
        t11["text"]="O"
        turn = True  
        check()

def clicked12():
    global turn
    global cell
    if turn == True and t12["text"]==" ":
        t12["text"]="X"
        
        turn = False
        check()
    elif turn == False and t12["text"]==" " :
        t12["text"]="O"
        turn = True 
        check()

def clicked13():
    global turn
    global cell
    if turn == True and t13["text"]==" ":
        t13["text"]="X"
        
        turn = False
        check()
    elif turn == False and t13["text"]==" " :
        t13["text"]="O"
        turn = True
        check()

def clicked14():
    global turn
    global cell
    if turn == True and t14["text"]==" ":
        t14["text"]="X"
        
        turn = False
        check()
    elif turn == False and t14["text"]==" " :
        t14["text"]="O"
        turn = True
        check()

def clicked15():
    global turn
    global cell
    if turn == True and t15["text"]==" ":
        t15["text"]="X"
        
        turn = False
        check()
    elif turn == False and t15["text"]==" " :
        t15["text"]="O"
        turn = True 
        check()

def clicked16():
    global turn
    global cell
    if turn == True and t16["text"]==" ":
        t16["text"]="X"
        
        turn = False
        check()
    elif turn == False and t16["text"]==" " :
        t16["text"]="O"
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
    b10 = t10["text"]
    b11 = t11["text"]
    b12 = t12["text"]
    b13 = t13["text"]
    b14 = t14["text"]
    b15 = t15["text"]
    b16 = t16["text"]
    
    count = count+1

    if b1==b2 and b2==b3 and b3==b4 and b1=="O" or b1==b2 and b2==b3 and b3==b4 and b1=="X":
        win(t1["text"])

    if b5==b6 and b6==b7 and b7==b8 and b5=="O" or b5==b6 and b6==b7 and b7==b8 and b5=="X":
        win(t5["text"])

    if b9==b10 and b10==b11 and b11==b12 and b9=="O" or b9==b10 and b10==b11 and b11==b12 and b9=="X":
        win(t9["text"])

    if b13==b14 and b14==b15 and b15==b16 and b13=="O" or b13==b14 and b14==b15 and b15==b16 and b13=="X":
        win(t13["text"])

    





    if b1==b5 and b5==b9 and b9==b13 and b1=="O" or b1==b5 and b5==b9 and b9==b13 and b1=="X":
        win(t1["text"])

    if b2==b6 and b6==b10 and b10==b14 and b2=="O" or b2==b6 and b6==b10 and b10==b14 and b2=="X":
        win(t2["text"])

    if b3==b7 and b7==b11 and b11==b15 and b3=="O" or b3==b7 and b7==b11 and b11==b15 and b3=="X":
        win(t3["text"])

    if b4==b8 and b8==b12 and b12==b16 and b4=="O" or b4==b8 and b8==b12 and b12==b16 and b4=="X":
        win(t4["text"])

    





    if b1==b6 and b6==b11 and b11==b16 and b1=="O" or b1==b6 and b6==b11 and b11==b16 and b1=="X":
        win(t1["text"])

    if b13==b10 and b10==b7 and b7==b4 and b13=="O" or b13==b10 and b10==b7 and b7==b4 and b13=="X":
        win(t13["text"])


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
        t10.config(text=" ")
        t11.config(text=" ")
        t12.config(text=" ")
        t13.config(text=" ")
        t14.config(text=" ")
        t15.config(text=" ")
        t16.config(text=" ")
        

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
    t10.config(text=" ")
    t11.config(text=" ")
    t12.config(text=" ")
    t13.config(text=" ")
    t14.config(text=" ")
    t15.config(text=" ")
    t16.config(text=" ")
    

t1=tkinter.Button(self,text=" ",font=("forte"),bg='orange',fg='firebrick1',height = 3, width = 6,command=clicked1)
t1.place(relx= 0.436, rely= 0.415, anchor= 'se')

t2=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked2)
t2.place(relx= 0.476, rely= 0.415, anchor= 's')

t3=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked3)
t3.place(relx= 0.559, rely= 0.415, anchor= 's')

t4=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked4)
t4.place(relx= 0.599, rely= 0.415, anchor= 'sw')

t5=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked5)
t5.place(relx= 0.436, rely= 0.475, anchor= 'e')

t6=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked6)
t6.place(relx= 0.476, rely= 0.475, anchor= 'center')

t7=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked7)
t7.place(relx= 0.559, rely= 0.475, anchor= 'center')

t8=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked8)
t8.place(relx= 0.599, rely= 0.475, anchor= 'w')

t9=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked9)
t9.place(relx= 0.436, rely= 0.535, anchor= 'ne')

t10=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked10)
t10.place(relx= 0.476, rely= 0.535, anchor= 'n')

t11=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked11)
t11.place(relx= 0.559, rely= 0.535, anchor= 'n')

t12=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked12)
t12.place(relx= 0.599, rely= 0.535, anchor= 'nw')

t13=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked13)
t13.place(relx= 0.436, rely= 0.77, anchor= 'se')

t14=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked14)
t14.place(relx= 0.476, rely= 0.77, anchor= 's')

t15=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked15)
t15.place(relx= 0.559, rely= 0.77, anchor= 's')

t16=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height = 3, width = 6, command=clicked16)
t16.place(relx= 0.599, rely= 0.77, anchor= 'sw')




self.mainloop()