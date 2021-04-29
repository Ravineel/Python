from Database import Connections

class Login:

    def __init__(self):
        self.check =False
        self.conn,self.cur = Connections.login()

    def connect(self,usrname,psswd):
        try:
           
            self.cur.execute('SELECT username,password FROM login WHERE username = ?  and  password = ?', (usrname,psswd,))
            row = self.cur.fetchone()

            if row is None:
                return False,"Wrong Credentials"    
            else:
                msg = "Login Successfull"
                self.check=True
                self.conn.close()
                print(msg)
        except:
            self.check=False
            msg = "Failed"
        return self.check, msg
        



