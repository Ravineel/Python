import sqlite3
import getpass
import sys
import datetime
from manage import Manage
from login import Login

def log():
    usrname = input("Enter username: ")
    psswd = getpass.getpass(prompt="Enter Password:  ")
    Check =Login()
    check  = Check.connect(usrname,psswd)


    


        









