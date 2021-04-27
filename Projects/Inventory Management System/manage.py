
from Database import Connections



class Manage:
    
    def __init__(self):
        dbname = 'sgccl'
        self.conn,self.cur = Connections.connection(dbname)


    
    def exit_sys(self):
        self.conn.close()

    
    def add_description(self):
    
        part_name=input("Enter Part Name:")
        part_id=input("Enter Part ID else press entre to skip: ")
        description=input("Enter Part Description: ")   
        if part_name is None:
            print("part name not entred!")
        
        elif description is None:
            print("Description not entered!")
        
        else:
            self.cur.execute('SELECT Part_Name, Part_ID FROM Part WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
            row = self.cur.fetchone()
            if row is not  None:
                print("Part is already added!")
            
            else:
                self.cur.execute(
            '''INSERT INTO Part (Part_Name,Part_ID,Description)
                VALUES (?,?,?)''',(part_name,part_id,description,))
                print("Part Added Succesfully")
                self.conn.commit()
                   
    def Part_Check(self):
        part_name=input("Enter Part Name:")
        part_id=input("Enter Part ID or press entre to skip: ")
        if part_id is None:
            part_id='None'

        if part_name is None:
            print("part name not entred!Try again")
            
        else:
            self.cur.execute('SELECT Part_Name, Part_ID FROM Part WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
            row = self.cur.fetchone()
            if row is not  None:
                print("Part is present!")
                
            else:
                print("Part Not Present")
    
          
    def add_stock(self):
        part_name=input("Enter Part Name:")
        part_id=input("Enter Part ID or press entre to skip: ")
        QTY =int(input("Enter amount: "))

        if part_id is None:
            part_id='None'

        if part_name is None:
            print("part name not entred!Try again")
                
            
        else:    
            self.cur.execute('SELECT Part_Name, Part_ID FROM Part WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
            row = self.cur.fetchone()

            if row is None:
                print("No part by",part_name,"is present")
        
            else:

                self.cur.execute('SELECT Part_Name, Part_ID FROM Stock WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
                row = self.cur.fetchone()

                if row is None:
                    self.cur.execute(
                        '''INSERT INTO STOCK (Part_Name, Part_ID,Stock) 
                        VALUES(?,?,?)''', (part_name,part_id,QTY,) )

                else:
                    self.cur.execute(
                    'UPDATE Stock SET stock = stock + ? where Part_Name = ? ',(QTY,part_name,) )

                self.cur.execute(
                    '''INSERT INTO History (Part_Name,Part_ID,ADD_Remove,Time) 
                    VALUES(?,?,?,datetime('now','localtime'))''', (part_name,part_id,QTY,) )
            
                self.conn.commit()
                

    
    def enquire(self):

        part_name=input("Enter Part Name:")
        part_id=input("Enter Part ID or press entre to skip: ")
        

        if part_id is None:
            part_id='None'
        
        
        if part_name is None:
            print("part name not entred!Try again")
            
        
        self.cur.execute('SELECT Part_Name, Part_ID FROM Part WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
        row = self.cur.fetchone()

        if row is None:
            print("No part by",part_name,"is present")

        else:

            res=self.cur.execute(
                 '''SELECT Part_Name, Part_ID, Stock from Stock where Part_Name = ? or Part_Id = ?''',(part_name,part_id, )

            ).fetchall()

            print('Part Name: '+str(res[0][0])+" Part Id: "+str(res[0][1])+" Stock: "+str(res[0][2]))  
    
    
    
        
    def use_part(self):
        part_name=input("Enter Part Name:")
        part_id=input("Enter Part ID or press entre to skip: ")
        V_NO= input("Enter Vehicle Number(FULL): ")
        V_Type = input("Enter Vehcle Type(Eg- Truck 8 wheeler, JCB): ")
        D_Name = input("Enter Driver Name: ")
        QTY =int(input("Enter amount to be used: "))


        if D_Name is None or V_NO is None or V_Type is None or QTY is None or part_name is None:
            print("Please Fill out all details! Try Again")
            


        if part_id is None:
            part_id='None'
        self.cur.execute('SELECT Part_Name, Part_ID FROM Part WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
        row = self.cur.fetchone()

        if row is None:
            print("No part by",part_name,"is present")

        else:

            res=self.cur.execute(
                 '''SELECT Stock from Stock where Part_Name = ? or Part_Id = ?''',(part_name,part_id, )

            ).fetchall()

            if res[0][0] - QTY < 0:
                print("Required Amount not present in Stock")
                print("Stock: "+str(res[0][0]))

            else:
                self.cur.execute(
                        'UPDATE Stock SET Stock = Stock - ? where Part_Name = ? or Part_ID = ? ', (QTY,part_name,part_id,) )

                

                self.cur.execute(
                    '''INSERT INTO Vehicle(Driver,Vehicle_Number,Vehicle_Type,Part_Name,Part_ID,QTY,Time)
                    VALUES(?,?,?,?,?,?,datetime('now','localtime'))''',(D_Name,V_NO,V_Type,part_name,part_id,QTY,)
                )



                QTY = - QTY

                self.cur.execute(
                    '''INSERT INTO History (Part_Name,Part_ID,ADD_Remove,Time) 
                    VALUES(?,?,?,datetime('now','localtime'))''', (part_name,part_id,QTY,) )
            
                self.conn.commit()
    