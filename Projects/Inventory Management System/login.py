from Database import Connections

class Login:

    def __init__(self):
        self.check =False
        self.conn,self.cur = Connections.login()

    def connect(self,usrname,psswd):

        self.cur.execute('SELECT username,password FROM login WHERE username = ?  and  password = ?', (usrname,psswd,))
        row = self.cur.fetchone()

        if row is None:
            print("Username  or  Password is wrong")

    
        else:
            print("Login Successfull")
            self.check=True
            self.conn.close()
        return self.check
        



