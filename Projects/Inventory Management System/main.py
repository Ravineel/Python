import sqlite3
import getpass
import sys
import datetime
from manage import Manage
from login import Login

import tkinter
from tkinter import *
import tkinter.messagebox





def log(username,psswd):
    Check =Login() 
    check,msg  = Check.connect(username,psswd)
    return check, msg

def login():
    tkWindow = Tk()
    tkWindow.geometry('250x100')
    tkWindow.title('Login Screen')
    # username label and text entry box
    usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)
    # password label and password entry box
    passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
    password = StringVar()

    def reset():
        username.set("")
        password.set("")

    tkWindow.counter = 0

    def Exit():
        tkinter.messagebox.showinfo("Exiting", "Closing the Application..")
        tkWindow.destroy()

    def validateLogin():
        if tkWindow.counter < 2:
            res, msg = log(username.get(),password.get())
            if res:
                tkinter.messagebox.showinfo("SUCCESS",msg)
                print(msg)
                
                #menu()
                tkWindow.destroy()
                from Menu import menu
                menu()
            else:
                tkWindow.counter += 1
                reset()
                tkinter.messagebox.showinfo(msg,
                                            "You have " + str(3 - tkWindow.counter) + " tries left.")
        else:
            tkinter.messagebox.showinfo("Alert! Wrong Credentials.", "Closing the Application..")
            tkWindow.destroy()

    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)
    # login button
    loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)
    # reset button
    ResetButton = Button(tkWindow, text="Reset", command=reset).grid(row=4, column=1)
    tkWindow.mainloop()
    exit_ = Button(tkWindow, text="exit", command=Exit).grid(row=2, column=2)
    


login()

    


        









