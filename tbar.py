# -*- coding: UTF-8 -*-

from Tkinter import *

def resize(ev=None):
    print scale.get()
    label.config(font='Helvetica -%d bold' % scale.get())

top = Tk()
top.geometry()

label = Label(top, text = 'hello world!', font = 'Helvetica -12 bold')
label.pack(fill=Y,expand=1)

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)


quit = Button(top, text="QUIT", command=top.quit, activeforeground='white', activebackground='red')
quit.pack()

mainloop()