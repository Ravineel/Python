import sqlite3

class Connections():
    @staticmethod
    def connection(dbname):
        conn = sqlite3.connect(dbname+'.sqlite')
        return conn
    
    @staticmethod
    def login():
        conn = sqlite3.connect('login.sqlite')
        return conn


