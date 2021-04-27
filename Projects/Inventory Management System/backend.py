from sqlite3.dbapi2 import Error
from Database import Connections

class Backened:

    def __init__(self,dbname='') :
        self.conn, self.cur = Connections.connection(dbname=dbname)

    def exit_app(self):
        self.conn.close()
        return True
    
    def add_New_Stock(self, part_name, part_id='', part_description='', qty=0):
        try:    
            self.cur.execute(
                '''INSERT INTO Stock (Part_Name, Part_Id,Stock) 
                VALUES(?,?,?)''', (part_name,part_id,qty,) 
            )
            self.cur.execute(
            '''INSERT INTO History (Part_Name,Part_ID,ADD_Remove,Time) 
            VALUES(?,?,?,datetime('now','localtime'))''', (part_name,part_id,qty,) 
            )
            self.cur.execute(
            '''INSERT INTO Part (Part_Name,Part_Id,Description)
            VALUES (?,?,?)''',(part_name,part_id,part_description,)
            )
            self.conn.commit()
            self.conn.close()
            return True, "Successfull"
        except Error :
            msg='Error occured, Please try again! '+Error
            return False, msg

   
    def check_Part(self, part_name, part_id=''):

        if part_name is None :
            msg = "Part name not entered"
            return False, msg

        self.cur.execute('SELECT Part_Name, Part_Id FROM Part WHERE Part_Name = ?  or  Part_Id = ?', (part_name,part_id,))
        row = self.cur.fetchone()
        if row is not  None:
            return True, "Part info already Added"
        
        else:
            return False, 'No Part found'



    def add_Stock_Info(self, part_name, part_id = '', part_description='',qty=0):

        if part_name is None :
            msg = "Part name not entered"
            self.conn.close()
            return False, msg
        
        else:
            res, msg = self.check_Part(part_name, part_id)
            if res == True:
                msg = "Part info already Added"
                self.conn.close()
                return False, msg
            else:
                stock=0
                res,msg = self.add_New_Stock(part_name,part_id,part_description,stock,qty)
                if res == True:
                    return res,"Data has been added."

                else: 
                    self.conn.close()
                    return res,msg
    
    def add_Stock(self, part_name, part_id='',qty=0):
        res, _ = self.check_Part(part_name, part_id)

        if res==True:
            try:
                self.cur.execute(
                    'UPDATE Stock SET stock = stock + ? where Part_Name = ? or Part_Id = ?',
                    (qty,part_name,part_id,)
                )
                self.cur.execute(
                '''INSERT INTO History (Part_Name,Part_Id,ADD_Remove,Time) 
                VALUES(?,?,?,datetime('now','localtime'))''', (part_name,part_id,qty,) 
                )
                self.conn.commit()
                self.conn.close()
                return True, 'Success'
            except:
                res=False
                msg = 'Error Occured, Try again'

                return res, msg
        
        else:
            res, msg = self.add_Stock_Info(part_name,part_id,'',qty)
                    
            return res,msg
    
    
    
    def use_Stock(self, part_name, part_id='', qty=0, type = '', vehicle_no='', location='', reason=''):
        
        res, msg = self.check_Part(part_name, part_id)
       
        if res ==True:
            try:
                self.cur.execute(
                    'UPDATE Stock SET Stock = Stock - ? where Part_Name = ? or Part_Id = ? ', 
                    (qty,part_name,part_id,) 
                )
                qty = -qty
                if type=='camp':
                    self.cur.execute(
                    ''' INSERT INTO ? (Part_Name, Part_Id, QTY, Reason, Location,DATETIME)
                    VALUES(?,?,?,?,datetime('now', 'localtime'))''',(type, part_name, part_id, qty,reason,location, )
                    )

                elif type=='vehicle':
                    self.cur.execute(
                    ''' INSERT INTO ? (Part_Name, Part_Id, QTY, Reason, Vehicel_NO,DATETIME)
                    VALUES(?,?,?,?,?,datetime('now', 'localtime'))''',(type, part_name, part_id, qty,reason, vehicle_no,)
                    )

                else:
                    self.cur.execute(
                        ''' INSERT INTO ? (Part_Name, Part_Id, QTY, Reason, DATETIME)
                        VALUES(?,?,?,?,datetime('now', 'localtime'))''',(type, part_name, part_id, qty,reason,)
                    )


                self.cur.execute(
                    '''INSERT INTO History (Part_Name,Part_ID,ADD_Remove,Time) 
                    VALUES(?,?,?,datetime('now','localtime'))''', (part_name,part_id,qty,) 
                )
                self.cur.commit()
                res=True
                msg='Succesfull'
            except:
                res=False
                msg = 'Error Occured, Try again'
            return res, msg
    
    def check_Stock(self, part_name, part_id=''):
        res, msg = self.check_Part(part_name,part_id)
        if res:
            self.cur.execute(
                '''SELECT Part_Name, Part_Id, Stock FROM Stock WHERE Part_Name=? or Part_Id = ?''',
                (part_name,part_id,)
            )

            row  = self.cur.fetchone()
            self.conn.close()

            if row is None:
                return False,'Please Try Again'
            else:
                
                return True, row
        else: 
            self.conn.close()         
            return False, 'No Part'
        

        

