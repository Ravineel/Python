import tkinter
from tkinter import *
import tkinter.messagebox
from backend import Backened

def use_stock():
    tk = Tk()
    tk.geometry('400x300')
    tk.title('Use Stock')
    PartNamelabel = Label(tk, text="Part Name*").grid(row=0, column=0)
    PartName = StringVar()
    PartNameEntry = Entry(tk, textvariable=PartName).grid(row=0, column=1)
    PartIDLabel = Label(tk, text="Part ID").grid(row=1, column=0)
    PartID = StringVar()
    PartIDEntry = Entry(tk, textvariable=PartID).grid(row=1, column=1)
    QuantityLabel = Label(tk, text="Quantity*").grid(row=2, column=0)
    Quantity = StringVar()
    QuantityEntry = Entry(tk, textvariable=Quantity).grid(row=2, column=1)
    ReasonLabel = Label(tk, text="Reason*").grid(row=5, column=0)
    Reason = StringVar()
    ReasonEntry = Entry(tk, textvariable=Reason).grid(row=5, column=1)
    TypeLabel = Label(tk, text="Type").grid(row=3, column=0)
    TypeVariable = StringVar()
    TypeVariable.set("general")
    TypeMenu = OptionMenu(tk, TypeVariable, "vehicle", "camp", "general")
    TypeMenu.grid(row=3, column=1)
    VehicleNumberLabel = Label(tk, text="Vehicle Number").grid(row=4, column=0)
    VehicleNumber = StringVar()
    VehicleNumberEntry = Entry(tk, textvariable=VehicleNumber).grid(row=4, column=1)
    LocationLabel = Label(tk, text=" Location").grid(row=6, column=0)
    Location = StringVar()
    LocationEntry = Entry(tk, textvariable=Location).grid(row=6, column=1)


    def reset():
        PartName.set("")
        PartID.set("")
        Quantity.set("")
        Reason.set("")
        VehicleNumber.set("")
        Location.set("")

    def cancel():
        tkinter.messagebox.showinfo("", "Returning to Main Menu..")
        tk.destroy()
        from Menu import menu
        menu()

    def usestock():
        if PartName.get() and Quantity.get() and Reason.get():
            part_name = PartName.get()
            part_id = PartID.get()
            qty = Quantity.get()
            reason= Reason.get()
            type_val = TypeVariable.get()
            vehicle_no = VehicleNumber.get()
            location = Location.get()

            if len(part_id) <1:
                part_id=None
            if len(location)<1:
                location=None
            if len(vehicle_no)<1:
                vehicle_no =None
            Use = Backened()
           
            res,msg = Use.use_Stock(part_name,part_id,qty,type_val,vehicle_no,location,reason)
            if res:
                tkinter.messagebox.showinfo("Sucess", msg)
            else:
                tkinter.messagebox.showinfo("Error",msg)
            Use.conn.close()
            reset()
        else:
            tkinter.messagebox.showinfo("Error", "Mandatory fields have not been filled.")
            reset()

    def print_():
        tkinter.messagebox.showinfo("Status", str(PartName.get())+" "+str(PartID.get())+" "+str(Quantity.get())+" "+str(TypeVariable.get())+" "+str(Reason.get())+" "+str(VehicleNumber.get())+" "+str(Location.get()))

    AddButton = Button(tk, text="use stock", command=usestock).grid(row=7, column=0)
    ResetButton = Button(tk, text="reset", command=reset).grid(row=7, column=1)
    CancelButton = Button(tk, text="cancel", command=cancel).grid(row=7, column=2)
    tk.mainloop()


use_stock()
