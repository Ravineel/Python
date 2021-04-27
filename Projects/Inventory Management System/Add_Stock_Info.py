import tkinter
from tkinter import *
import tkinter.messagebox
from backend import Backened

def add_stock_info():
    tk = Tk()
    tk.geometry('400x100')
    tk.title('Add Stock info')
    PartNamelabel = Label(tk, text="Part Name*").grid(row=0, column=0)
    PartName = StringVar()
    PartNameEntry = Entry(tk, textvariable=PartName).grid(row=0, column=1)
    PartIDLabel = Label(tk, text="Part ID").grid(row=1, column=0)
    PartID = StringVar()
    PartIDEntry = Entry(tk, textvariable=PartID).grid(row=1, column=1)
    DescriptionLabel = Label(tk, text="Description*").grid(row=2, column=0)
    Description = StringVar()
    DescriptionEntry = Entry(tk, textvariable=Description).grid(row=2, column=1)

    def reset():
        PartName.set("")
        PartID.set("")
        Description.set("")

    def cancel():
        tkinter.messagebox.showinfo("", "Returning to Main Menu..")
        tk.destroy()
        from Menu import menu
        menu()

    def add():
        if PartName.get():

            Info = Backened()

            part_name = PartName.get()
            part_id = PartID.get()
            desc = Description.get()
            if len(part_id)<1:
                part_id=None
            res,msg  = Info.add_Stock_Info(part_name,part_id,desc,0)
            if res:
                tkinter.messagebox.showinfo("", msg)
            else:
                tkinter.messagebox.showinfo("Error", msg)
            reset()
        else:
            tkinter.messagebox.showinfo("Error", "Mandatory fields have not been filled.")
            reset()

    AddButton = Button(tk, text="add info", command=add).grid(row=4, column=0)
    ResetButton = Button(tk, text="reset", command=reset).grid(row=4, column=1)
    CancelButton = Button(tk, text="cancel", command=cancel).grid(row=4, column=2)
    tk.mainloop()

add_stock_info()
