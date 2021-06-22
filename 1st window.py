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



label = tkinter.Label(self,text="TIC TAC TOE", bg='firebrick1',fg='orange',font=("broadway", 70))
label.pack(side="top", fill="x", pady=12)

button1 = tkinter.Button(self, text='Start',font=("broadway", 50),bg='orange',fg='firebrick1',width=15 )
button1.place(relx= 0.5, rely= 0.7, anchor= 'center')


self.mainloop()

