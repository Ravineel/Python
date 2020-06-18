import sqlite3
import getpass
import sys
import datetime
from  Database import Connections

conn = Connections.login()
cur =conn.cursor()
usrname = input("Enter username: ")
psswd = getpass.getpass(prompt="Enter Password:  ")


cur.execute('SELECT username,password FROM login WHERE username = ?  and  password = ?', (usrname,psswd,))
row = cur.fetchone()

if row is None:
    print("Email or  Password is wrong \n you have last chance to proceed ")

    usrname = input("Enter username: ")
    psswd = getpass.getpass(prompt="Enter Password:  ")

    cur.execute('SELECT username,password FROM login WHERE username = ?  and  password = ?', (usrname,psswd,))
    row = cur.fetchone()

    if row is None:
        print("Email and Password entered is wrong. BYE!")
        conn.commit()
        conn.close()

        sys.exit()
    
else:
    print("Login Successfull")
conn.commit()
conn.close()
dbname = 'sgccl'
conn = Connections.connection(dbname)
cur =conn.cursor()



while(True):
    print()
    print()
    print("Press A to add Part Description")
    print("Press W to add stock")
    print("Press I to enquire about specific part and Stock")
    print("Press C to check  Part is in database")
    print("Press S to use Part")    
    print("Press E to Exit")



    choice  = input().lower()


    if choice =='e':
        break
    elif choice == 'a':
        part_name=input("Enter Part Name:")
        part_id=input("Enter Part ID else press entre to skip: ")
        description=input("Enter Part Description: ")   
        if part_name is None:
            print("part name not entred!")
            continue
        elif description is None:
            print("Description not entered!")
            continue
        else:
            cur.execute('SELECT Part_Name, Part_ID FROM Part WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
            row = cur.fetchone()
            if row is not  None:
                print("Part is already added!")
                continue
            else:
                cur.execute(
                '''INSERT INTO Part (Part_Name,Part_ID,Description)
                VALUES (?,?,?)''',(part_name,part_id,description,))
                print("Part Added Succesfully")
                conn.commit()
                continue
    elif choice == 'c':
        part_name=input("Enter Part Name:")
        part_id=input("Enter Part ID or press entre to skip: ")
        if part_id is None:
            part_id='None'

        if part_name is None:
            print("part name not entred!Try again")
            continue
        else:
            cur.execute('SELECT Part_Name, Part_ID FROM Part WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
            row = cur.fetchone()
            if row is not  None:
                print("Part is present!")
                continue
            else:
                print("Part Not Present")
    
    
    elif choice =='w':
        part_name=input("Enter Part Name:")
        part_id=input("Enter Part ID or press entre to skip: ")
        QTY =int(input("Enter amount: "))

        if part_id is None:
            part_id='None'

        if part_name =='':
            print("part name not entred!Try again")
            continue    
            
        else:    
            cur.execute('SELECT Part_Name, Part_ID FROM Part WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
            row = cur.fetchone()

            if row is None:
                print("No part by",part_name,"is present")
        
            else:

                cur.execute('SELECT Part_Name, Part_ID FROM Stock WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
                row = cur.fetchone()

                if row is None:
                    cur.execute(
                        '''INSERT INTO STOCK (Part_Name, Part_ID,Stock) 
                        VALUES(?,?,?)''', (part_name,part_id,QTY,) )

                else:
                    cur.execute(
                    'UPDATE Stock SET stock = stock + ? where Part_Name = ? ',(QTY,part_name,) )

                cur.execute(
                    '''INSERT INTO History (Part_Name,Part_ID,ADD_Remove,Time) 
                        VALUES(?,?,?,datetime('now','localtime'))''', (part_name,part_id,QTY,) )
            
                conn.commit()
                continue


    elif choice =='i':

        part_name=input("Enter Part Name:")
        part_id=input("Enter Part ID or press entre to skip: ")
        

        if part_id is None:
            part_id='None'
        
        
        if part_name is None:
            print("part name not entred!Try again")
            continue
        
        cur.execute('SELECT Part_Name, Part_ID FROM Part WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
        row = cur.fetchone()

        if row is None:
            print("No part by",part_name,"is present")

        else:

            res=cur.execute(
                '''SELECT Part_Name, Part_ID, Stock from Stock where Part_Name = ? or Part_Id = ?''',(part_name,part_id, )

            ).fetchall()

            print('Part Name: '+str(res[0][0])+" Part Id: "+str(res[0][1])+" Stock: "+str(res[0][2]))  
    
    
    
    
    else:
        part_name=input("Enter Part Name:")
        part_id=input("Enter Part ID or press entre to skip: ")
        V_NO= input("Enter Vehicle Number(FULL): ")
        V_Type = input("Enter Vehcle Type(Eg- Truck 8 wheeler, JCB): ")
        D_Name = input("Enter Driver Name: ")
        QTY =int(input("Enter amount to be used: "))


        if D_Name is None or V_NO is None or V_Type is None or QTY is None or part_name is None:
            print("Please Fill out all details! Try Again")
            continue


        if part_id is None:
            part_id='None'
        cur.execute('SELECT Part_Name, Part_ID FROM Part WHERE Part_Name = ?  or  Part_ID = ?', (part_name,part_id,))
        row = cur.fetchone()

        if row is None:
            print("No part by",part_name,"is present")

        else:

            res=cur.execute(
                '''SELECT Stock from Stock where Part_Name = ? or Part_Id = ?''',(part_name,part_id, )

            ).fetchall()

            if res[0][0] - QTY < 0:
                print("Required Amount not present in Stock")
                print("Stock: "+str(res[0][0]))

            else:
                cur.execute(
                    'UPDATE Stock SET Stock = Stock - ? where Part_Name = ? or Part_ID = ? ', (QTY,part_name,part_id,) )

                

                cur.execute(
                    '''INSERT INTO Vehicle(Driver,Vehicle_Number,Vehicle_Type,Part_Name,Part_ID,QTY,Time)
                    VALUES(?,?,?,?,?,?,datetime('now','localtime'))''',(D_Name,V_NO,V_Type,part_name,part_id,QTY,)
                )



                QTY = - QTY

                cur.execute(
                '''INSERT INTO History (Part_Name,Part_ID,ADD_Remove,Time) 
                    VALUES(?,?,?,datetime('now','localtime'))''', (part_name,part_id,QTY,) )
            
            conn.commit()

      
conn.commit()
conn.close()
sys.exit()
        









