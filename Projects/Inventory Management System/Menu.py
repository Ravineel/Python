import tkinter
from tkinter import *
import tkinter.messagebox


def menu():
    tk = Tk()
    tk.geometry('350x100')
    tk.title('Storage Management Menu')

    def Exit():
        tkinter.messagebox.showinfo("Exiting", "Closing the Application..")
        tk.destroy()
        exit()

    def addstock():
        tk.destroy()
        from Add_Stock import add_stock
        add_stock()


    def addstockinfo():
        tk.destroy()
        from Add_Stock_Info import add_stock_info
        add_stock_info()

    def checkstock():
        tk.destroy()
        from Check_Stock import check_stock
        check_stock()

    def usestock():
        tk.destroy()
        from Use_Stock import use_stock
        use_stock()

    AddStock = Button(tk, text="Add Stock", command=addstock).grid(row=0, column=0)
    AddStockInfo = Button(tk, text="Add Stock Info", command=addstockinfo).grid(row=0, column=5)
    CheckStock = Button(tk, text="Check Stock", command=checkstock).grid(row=5, column=0)
    UseStock = Button(tk, text="Use Stock", command=usestock).grid(row=5, column=5)
    exit_ = Button(tk, text="exit", command=Exit).grid(row=2, column=2)
    tk.mainloop()


#menu()
