import tkinter
from tkinter import *
import tkinter.messagebox
from backend import Backened

l =["Too"]

def check_stock():
    tk = Tk()
    tk.geometry('400x100')
    tk.title('Check Stock')
    PartNamelabel = Label(tk, text="Part Name*").grid(row=0, column=0)
    PartName = StringVar()
    PartNameEntry = Entry(tk, textvariable=PartName).grid(row=0, column=1)
    PartIDLabel = Label(tk, text="Part ID").grid(row=1, column=0)
    PartID = StringVar()
    PartIDEntry = Entry(tk, textvariable=PartID).grid(row=1, column=1)

    def reset():
        PartName.set("")
        PartID.set("")

    def cancel():
        tkinter.messagebox.showinfo("", "Returning to Main Menu..")
        tk.destroy()
        from Menu import menu
        menu()

    def check__stock():

        part_name = PartName.get()
        part_id = PartID.get()
        Check = Backened()

        res,val = Check.check_Stock(part_name, part_id)
        if part_name is not None:    
            if res:
                
                tkk = Tk()
                i=0
                head = ('Part_Name', 'Part_Id', 'QTY')
                for x in head:
                    w = Text(tkk, width=20, height=4)
                    
                    w.grid(row=0, column=i)
                    w.insert(END, x)
                    i=i+1
                i=0
                for x in val:
                    w = Text(tkk, width=20, height=4)
                    w.grid(row=1, column=i)
                    w.insert(END, str(x))
                    
                    i=i+1
            else:
                tkinter.messagebox.showinfo("error", val)
            reset()

        
        else:
            tkinter.messagebox.showinfo("Error", "Mandatory fields have not been filled.")
            reset()

    AddButton = Button(tk, text="check stock", command=check__stock).grid(row=4, column=0)
    ResetButton = Button(tk, text="reset", command=reset).grid(row=4, column=1)
    CancelButton = Button(tk, text="cancel", command=cancel).grid(row=4, column=2)
    tk.mainloop()

check_stock()