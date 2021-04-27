import sqlite3

class Connections():
    @staticmethod
    def connection(dbname):
        conn = sqlite3.connect('sgccl.sqlite')
        cur = conn.cursor()
        return conn,cur
    
    @staticmethod
    def login():
        conn = sqlite3.connect('login.sqlite')
        cur = conn.cursor()
        return conn,cur


