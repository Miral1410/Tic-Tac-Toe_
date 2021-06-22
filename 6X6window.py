import tkinter
from tkinter import Menu, messagebox

self=tkinter.Tk()
self.title("TIC TAC TOE")
self.minsize(750,500)
self.configure(bg='firebrick1')

label = tkinter.Label(self, text="6X6 GRID", bg='firebrick1',fg='orange',font=("broadway", 60))
label.pack(side="top", fill="x", pady=10)

label = tkinter.Label(self, text="", bg='firebrick1',fg='white',font=("broadway", 25))
label.place(relx= 0.25, rely= 0.5, anchor= 'e')

label = tkinter.Label(self, text="", bg='firebrick1',fg='white',font=("broadway", 25))
label.place(relx= 0.75, rely= 0.5, anchor= 'w')


turn = True

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

def clicked17():
    global turn
    global cell
    if turn == True and t17["text"]==" ":
        t17["text"]="X"
        
        turn = False
        check()
    elif turn == False and t17["text"]==" " :
        t17["text"]="O"
        turn = True 
        check()

def clicked18():
    global turn
    global cell
    if turn == True and t18["text"]==" ":
        t18["text"]="X"
        
        turn = False
        check()
    elif turn == False and t18["text"]==" " :
        t18["text"]="O"
        turn = True  
        check()

def clicked19():
    global turn
    global cell
    if turn == True and t19["text"]==" ":
        t19["text"]="X"
        
        turn = False
        check()
    elif turn == False and t19["text"]==" " :
        t19["text"]="O"
        turn = True 
        check()

def clicked20():
    global turn
    global cell
    if turn == True and t20["text"]==" ":
        t20["text"]="X"
        
        turn = False
        check()
    elif turn == False and t20["text"]==" " :
        t20["text"]="O"
        turn = True  
        check()

def clicked21():
    global turn
    global cell
    if turn == True and t21["text"]==" ":
        t21["text"]="X"
        
        turn = False
        check()
    elif turn == False and t21["text"]==" " :
        t21["text"]="O"
        turn = True 
        check()

def clicked22():
    global turn
    global cell
    if turn == True and t22["text"]==" ":
        t22["text"]="X"
        
        turn = False
        check()
    elif turn == False and t22["text"]==" " :
        t22["text"]="O"
        turn = True 
        check()

def clicked23():
    global turn
    global cell
    if turn == True and t23["text"]==" ":
        t23["text"]="X"
        
        turn = False
        check()
    elif turn == False and t23["text"]==" " :
        t23["text"]="O"
        turn = True  
        check()

def clicked24():
    global turn
    global cell
    if turn == True and t24["text"]==" ":
        t24["text"]="X"
        
        turn = False
        check()
    elif turn == False and t24["text"]==" " :
        t24["text"]="O"
        turn = True 
        check()

def clicked25():
    global turn
    global cell
    if turn == True and t25["text"]==" ":
        t25["text"]="X"
        
        turn = False
        check()
    elif turn == False and t25["text"]==" " :
        t25["text"]="O"
        turn = True  
        check()

def clicked26():
    global turn
    global cell
    if turn == True and t26["text"]==" ":
        t26["text"]="X"
        
        turn = False
        check()
    elif turn == False and t26["text"]==" " :
        t26["text"]="O"
        turn = True  
        check()

def clicked27():
    global turn
    global cell
    if turn == True and t27["text"]==" ":
        t27["text"]="X"
        
        turn = False
        check()
    elif turn == False and t27["text"]==" " :
        t27["text"]="O"
        turn = True  
        check()

def clicked28():
    global turn
    global cell
    if turn == True and t28["text"]==" ":
        t28["text"]="X"
        
        turn = False
        check()
    elif turn == False and t28["text"]==" " :
        t28["text"]="O"
        turn = True  
        check()

def clicked29():
    global turn
    global cell
    if turn == True and t29["text"]==" ":
        t29["text"]="X"
        
        turn = False
        check()
    elif turn == False and t29["text"]==" " :
        t29["text"]="O"
        turn = True  
        check()

def clicked30():
    global turn
    global cell
    if turn == True and t30["text"]==" ":
        t30["text"]="X"
        
        turn = False
        check()
    elif turn == False and t30["text"]==" " :
        t30["text"]="O"
        turn = True  
        check()

def clicked31():
    global turn
    global cell
    if turn == True and t31["text"]==" ":
        t31["text"]="X"
        
        turn = False
        check()
    elif turn == False and t31["text"]==" " :
        t31["text"]="O"
        turn = True  
        check()

def clicked32():
    global turn
    global cell
    if turn == True and t32["text"]==" ":
        t32["text"]="X"
        
        turn = False
        check()
    elif turn == False and t32["text"]==" " :
        t32["text"]="O"
        turn = True  
        check()

def clicked33():
    global turn
    global cell
    if turn == True and t33["text"]==" ":
        t33["text"]="X"
        
        turn = False
        check()
    elif turn == False and t33["text"]==" " :
        t33["text"]="O"
        turn = True  
        check()

def clicked34():
    global turn
    global cell
    if turn == True and t34["text"]==" ":
        t34["text"]="X"
        
        turn = False
        check()
    elif turn == False and t34["text"]==" " :
        t34["text"]="O"
        turn = True  
        check()

def clicked35():
    global turn
    global cell
    if turn == True and t35["text"]==" ":
        t35["text"]="X"
        
        turn = False
        check()
    elif turn == False and t35["text"]==" " :
        t35["text"]="O"
        turn = True  
        check()

def clicked36():
    global turn
    global cell
    if turn == True and t36["text"]==" ":
        t36["text"]="X"
        
        turn = False
        check()
    elif turn == False and t36["text"]==" " :
        t36["text"]="O"
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
    b17 = t17["text"]
    b18 = t18["text"]
    b19 = t19["text"]
    b20 = t20["text"]
    b21 = t21["text"]
    b22 = t22["text"]
    b23 = t23["text"]
    b24 = t24["text"]
    b25 = t25["text"]
    b26 = t26["text"]
    b27 = t27["text"]
    b28 = t28["text"]
    b29 = t29["text"]
    b30 = t30["text"]
    b31 = t31["text"]
    b32 = t32["text"]
    b33 = t33["text"]
    b34 = t34["text"]
    b35 = t35["text"]
    b36 = t36["text"]
    count = count+1

    if b1==b2 and b2==b3 and b3==b4 and b4==b5 and b5==b6 and b1=="O" or b1==b2 and b2==b3 and b3==b4 and b4==b5 and b5==b6 and b1=="X":
        win(t1["text"])

    if b7==b8 and b8==b9 and b9==b10 and b10==b11 and b11==b12 and b7=="O" or b7==b8 and b8==b9 and b9==b10 and b10==b11 and b11==b12 and b7=="X":
        win(t7["text"])

    if b13==b14 and b14==b15 and b15==b16 and b16==b17 and b17==b18 and b13=="O" or b13==b14 and b14==b15 and b15==b16 and b16==b17 and b17==b18 and b13=="X":
        win(t13["text"])

    if b19==b20 and b20==b21 and b21==b22 and b22==b23 and b23==b24 and b19=="O" or b19==b20 and b20==b21 and b21==b22 and b22==b23 and b23==b24 and b19=="X":
        win(t19["text"])

    if b25==b26 and b26==b27 and b27==b28 and b28==b29 and b29==b30 and b25=="O" or b25==b26 and b26==b27 and b27==b28 and b28==b29 and b29==b30 and b25=="X": 
        win(t25["text"])
    
    if b31==b32 and b32==b33 and b33==b34 and b34==b35 and b35==b36 and b31=="O" or b31==b32 and b32==b33 and b33==b34 and b34==b35 and b35==b36 and b31=="X":
        win(t31["text"])




    if b1==b7 and b7==b13 and b13==b19 and b19==b25 and b25==b31 and b1=="O" or b1==b7 and b7==b13 and b13==b19 and b19==b25 and b25==b31 and b1=="X":
        win(t1["text"])

    if b2==b8 and b8==b14 and b14==b20 and b20==b26 and b26==b32 and b2=="O" or b2==b8 and b8==b14 and b14==b20 and b20==b26 and b26==b32 and b2=="X":
        win(t2["text"])

    if b3==b9 and b9==b15 and b15==b21 and b21==b27 and b27==b33 and b3=="O" or b3==b9 and b9==b15 and b15==b21 and b21==b27 and b27==b33 and b3=="X":
        win(t3["text"])

    if b4==b10 and b10==b16 and b16==b22 and b22==b28 and b28==b34 and b4=="O" or b4==b10 and b10==b16 and b16==b22 and b22==b28 and b28==b34 and b4=="X":
        win(t4["text"])

    if b5==b11 and b11==b17 and b17==b23 and b23==b29 and b29==b35 and b5=="O" or b5==b11 and b11==b17 and b17==b23 and b23==b29 and b29==b35 and b5=="X": 
        win(t5["text"])
    
    if b6==b12 and b12==b18 and b18==b24 and b24==b30 and b30==b36 and b6=="O" or b6==b12 and b12==b18 and b18==b24 and b24==b30 and b30==b36 and b6=="X":
        win(t6["text"])

    

    if b1==b8 and b8==b15 and b15==b22 and b22==b29 and b29==b36 and b1=="O" or b1==b8 and b8==b15 and b15==b22 and b22==b29 and b29==b36 and b1=="X":
        win(t1["text"])

    if b31==b26 and b26==b21 and b21==b16 and b16==b11 and b11==b6 and b31=="O" or b31==b26 and b26==b21 and b21==b16 and b16==b11 and b11==b6 and b31=="X":
        win(t31["text"])

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
        t17.config(text=" ")
        t18.config(text=" ")
        t19.config(text=" ")
        t20.config(text=" ")
        t21.config(text=" ")
        t22.config(text=" ")
        t23.config(text=" ")
        t24.config(text=" ")
        t25.config(text=" ")
        t26.config(text=" ")
        t27.config(text=" ")
        t28.config(text=" ")
        t29.config(text=" ")
        t30.config(text=" ")
        t31.config(text=" ")
        t32.config(text=" ")
        t33.config(text=" ")
        t34.config(text=" ")
        t35.config(text=" ")
        t36.config(text=" ")

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
    t17.config(text=" ")
    t18.config(text=" ")
    t19.config(text=" ")
    t20.config(text=" ")
    t21.config(text=" ")
    t22.config(text=" ")
    t23.config(text=" ")
    t24.config(text=" ")
    t25.config(text=" ")
    t26.config(text=" ")
    t27.config(text=" ")
    t28.config(text=" ")
    t29.config(text=" ")
    t30.config(text=" ")
    t31.config(text=" ")
    t32.config(text=" ")
    t33.config(text=" ")
    t34.config(text=" ")
    t35.config(text=" ")
    t36.config(text=" ")
    

t1=tkinter.Button(self,text=" ",font=("forte"),bg='orange',fg='firebrick1',height=2, width=5,command=clicked1)
t1.place(relx= 0.35, rely= 0.38, anchor= 'se')

t2=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked2)
t2.place(relx= 0.385, rely= 0.38, anchor= 's')

t3=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked3)
t3.place(relx= 0.45, rely= 0.38, anchor= 's')

t4=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked4)
t4.place(relx= 0.515, rely= 0.38, anchor= 's')

t5=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked5)
t5.place(relx= 0.58, rely= 0.38, anchor= 's')

t6=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked6)
t6.place(relx= 0.675, rely= 0.38, anchor= 'se')

t7=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked7)
t7.place(relx= 0.35, rely= 0.47, anchor= 'se')

t8=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked8)
t8.place(relx= 0.385, rely= 0.47, anchor= 's')

t9=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked9)
t9.place(relx= 0.45, rely= 0.47, anchor= 's')

t10=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked10)
t10.place(relx= 0.515, rely= 0.47, anchor= 's')

t11=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked11)
t11.place(relx= 0.58, rely= 0.47, anchor= 's')

t12=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked12)
t12.place(relx= 0.675, rely= 0.47, anchor= 'se')

t13=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked13)
t13.place(relx= 0.35, rely= 0.51, anchor= 'e')

t14=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked14)
t14.place(relx= 0.385, rely= 0.51, anchor= 'center')

t15=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked15)
t15.place(relx= 0.45, rely= 0.51, anchor= 'center')

t16=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked16)
t16.place(relx= 0.515, rely= 0.51, anchor= 'center')

t17=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked17)
t17.place(relx= 0.58, rely= 0.51, anchor= 'center')

t18=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked18)
t18.place(relx= 0.675, rely= 0.51, anchor= 'e')

t19=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked19)
t19.place(relx= 0.35, rely= 0.6, anchor= 'e')

t20=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked20)
t20.place(relx= 0.385, rely= 0.6, anchor= 'center')

t21=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked21)
t21.place(relx= 0.45, rely= 0.6, anchor= 'center')

t22=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked22)
t22.place(relx= 0.515, rely= 0.6, anchor= 'center')

t23=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked23)
t23.place(relx= 0.58, rely= 0.6, anchor= 'center')

t24=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked24)
t24.place(relx= 0.675, rely= 0.6, anchor= 'e')

t25=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked25)
t25.place(relx= 0.35, rely= 0.64, anchor= 'ne')

t26=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked26)
t26.place(relx= 0.385, rely= 0.64, anchor= 'n')

t27=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked27)
t27.place(relx= 0.45, rely= 0.64, anchor= 'n')

t28=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked28)
t28.place(relx= 0.515, rely= 0.64, anchor= 'n')

t29=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked29)
t29.place(relx= 0.58, rely= 0.64, anchor= 'n')

t30=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked30)
t30.place(relx= 0.675, rely= 0.64, anchor= 'ne')

t31=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked31)
t31.place(relx= 0.35, rely= 0.73, anchor= 'ne')

t32=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked32)
t32.place(relx= 0.385, rely= 0.73, anchor= 'n')

t33=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked33)
t33.place(relx= 0.45, rely= 0.73, anchor= 'n')

t34=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked34)
t34.place(relx= 0.515, rely= 0.73, anchor= 'n')

t35=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked35)
t35.place(relx= 0.58, rely= 0.73, anchor= 'n')

t36=tkinter.Button(self,text=" ",font=("forte", ),bg='orange',fg='firebrick1',height=2, width=5, command=clicked36)
t36.place(relx= 0.675, rely= 0.73, anchor= 'ne')


self.mainloop()