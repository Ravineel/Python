import tkinter
from tkinter import *
import tkinter.messagebox
from backend import Backened

def add_stock():
    tk = Tk()
    tk.geometry('350x100')
    tk.title('Add Stock')
    PartNamelabel = Label(tk, text="Part Name*").grid(row=0, column=0)
    PartName = StringVar()
    PartNameEntry = Entry(tk, textvariable=PartName).grid(row=0, column=1)
    PartIDLabel = Label(tk, text="Part ID").grid(row=1, column=0)
    PartID = StringVar()
    PartIDEntry = Entry(tk, textvariable=PartID).grid(row=1, column=1)
    QuantityLabel = Label(tk, text="Quantity*").grid(row=2, column=0)
    Quantity = StringVar()
    QuantityEntry = Entry(tk, textvariable=Quantity).grid(row=2, column=1)

    def reset():
        PartName.set("")
        PartID.set("")
        Quantity.set("")

    def cancel():
        tkinter.messagebox.showinfo("", "Returning to Main Menu..")
        tk.destroy()
        from Menu import menu
        menu()

    def add():
        if PartName.get() and Quantity.get():
            Stock = Backened()

            part_name = PartName.get()
            part_id = PartID.get()
            qty = Quantity.get()
            if len(part_id)<1:
                part_id=None
            res, msg = Stock.add_Stock(part_name,part_id,qty)
            if res:
                tkinter.messagebox.showinfo("Success", msg)
            else:
                tkinter.messagebox.showinfo("Error", msg)
            reset()
        else:
            tkinter.messagebox.showinfo("Error", "Mandatory fields have not been filled.")
            reset()

    AddButton = Button(tk, text="add", command=add).grid(row=4, column=0)
    ResetButton = Button(tk, text="reset", command=reset).grid(row=4, column=1)
    CancelButton = Button(tk, text="cancel", command=cancel).grid(row=4, column=2)
    tk.mainloop()


add_stock()
