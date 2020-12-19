# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:15:20 2019

@author: Legion
"""

from tkinter import *

phonelist = []

def selected():
    print("At {0}".format(select.curselection()))
    return int(select.curselection()[0])


def add():
    phonelist.append([fnamevar.get(), lnamevar.get(), phonevar.get(), phonevar1.get(),emailvar.get()])
    reset()


def update():
    phonelist[selected()] = [fnamevar.get(),lnamevar.get(),phonevar.get(), phonevar1.get(),emailvar.get()]
    reset()

def delete():
    del phonelist[selected()]
    reset()


def load():
    fname, lname, phone, phone1, email = phonelist[selected()]
    fnamevar.set(fname)
    lnamevar.set(lname)
    phonevar.set(phone)
    phonevar1.set(phone1)
    emailvar.set(email)
    


def make_window():
    global fnamevar, lnamevar, phonevar, phonevar1, emailvar, select
    win = Tk()
    #win.resizable(False,False)

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="First Name").grid(row=0, column=0)
    fnamevar = StringVar()
    fname = Entry(frame1, textvariable=fnamevar)
    fname.grid(row=0, column=1,pady=(6,6))

    Label(frame1, text="Last Name").grid(row=1, column=0)
    lnamevar = StringVar()
    lname = Entry(frame1, textvariable=lnamevar)
    lname.grid(row=1, column=1,pady=(6,6))

    Label(frame1, text="Phone Number").grid(row=2, column=0)
    phonevar = StringVar()
    phone = Entry(frame1, textvariable=phonevar)
    phone.grid(row=2, column=1,pady=(6,6))

    Label(frame1, text="Alternate Number").grid(row=2, column=2)
    phonevar1 = StringVar()
    phone1 = Entry(frame1, textvariable=phonevar1)
    phone1.grid(row=2, column=3,pady=(6,6))

    Label(frame1, text="Email").grid(row=3, column=0)
    emailvar = StringVar()
    email = Entry(frame1, textvariable=emailvar)
    email.grid(row=3, column=1,pady=(6,6))
    
    
    frame2 = Frame(win)       
    frame2.pack()
    b1 = Button(frame2, text=" ADD ", command=add,padx=20)
    b2 = Button(frame2, text="UPDATE", command=update,padx=20)
    b3 = Button(frame2, text="DELETE", command=delete,padx=20)
    b4 = Button(frame2, text="LOAD  ", command=load,padx=20)
    b5 = Button(frame2, text="Refresh", command=reset)
    b1.pack(side=LEFT,pady=10,padx=8)
    b2.pack(side=LEFT,padx=8)
    b3.pack(side=LEFT,padx=8)
    b4.pack(side=LEFT,padx=8)
    b5.pack(side=LEFT,padx=8)
    

    frame3 = Frame(win)       
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, width=70, height=8)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y ,pady=10)
    select.pack(side=LEFT, fill=BOTH, expand=1,pady=10)
    return win


def reset():
    fnamevar.set('')
    lnamevar.set('')
    phonevar.set('')
    phonevar1.set('')
    emailvar.set('')
        
    phonelist.sort(key=lambda record: record[1])
    select.delete(0, END)
    for fname, lname, phone, phone1, email in phonelist:
        select.insert(END, "{0} {1}".format(fname   ,   lname ))


win = make_window()
reset()
win.mainloop()
