from sqlite3.dbapi2 import Error
from Database import Connections

class Manage:

    def __init__(self,dbname) :
        self.conn, self.cur = Connections.connection(dbname=dbname)

    def exit_app(self):
        self.conn.close()
        return True
    
    def add_New_Stock(self, part_name, part_id='', part_description='', qty=0):
        try:    
            self.cur.execute(
                '''INSERT INTO STOCK (Part_Name, Part_ID,Stock) 
                VALUES(?,?,?)''', (part_name,part_id,qty,) 
            )
            self.cur.execute(
            '''INSERT INTO History (Part_Name,Part_ID,Add_Remove,Time) 
            VALUES(?,?,?,datetime('now','localtime'))''', (part_name,part_id,qty,) 
            )
            self.cur.execute(
            '''INSERT INTO Part (Part_Name,Part_ID,Description)
            VALUES (?,?,?)''',(part_name,part_id,part_description,)
            )
            self.cur.commit()
            return True, None
        except:
            msg='Error occured, Please try again!'
            return False, msg


    def check_Part(self, part_name, part_id=''):

        self.cur.execute('SELECT Part_Name, Part_ID FROM PART WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
        row = self.cur.fetchone()
        if row is not  None:
            return True
        else:
            return False



    def add_Stock_Info(self, part_name, part_id = '', part_description=''):

        if part_name is None :
            msg = "Part name not entered"
            return False, msg
        
        else:
            if check_Part(part_name,part_id) == True:
                msg = "Part info already Added"
                return False, msg
            else:
                stock=0
                res,msg = add_New_Stock(part_name,part_id,part_description,stock)
                if res == True:
                    return res
                else: return res,msg


