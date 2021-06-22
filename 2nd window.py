import tkinter
from tkinter import Menu

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

label =tkinter.Label(self, text="selet your grid", bg='firebrick1',fg='orange',font=("broadway", 60))
label.pack(side="top", fill="x", pady=10)


button =tkinter.Button(self, text='3X3',font=("broadway", 25),bg='orange',fg='firebrick1',width=13)
button.place(relx= 0.45, rely= 0.6, anchor= 'se')

button=tkinter.Button(self,text='4X4',font=("broadway", 25),bg='orange',fg='firebrick1',width=13)
button.place(relx= 0.55, rely= 0.6, anchor= 'sw')

button=tkinter.Button(self,text='5X5',font=("broadway", 25),bg='orange',fg='firebrick1',width=13)
button.place(relx= 0.45, rely= 0.7, anchor= 'ne')

button=tkinter.Button(self,text='6X6',font=("broadway", 25),bg='orange',fg='firebrick1',width=13)
button.place(relx= 0.55, rely= 0.7, anchor= 'nw')

self.mainloop()