import tkinter as tk
import string

from numpy import delete
from c3q4 import *
from tkinter.ttk import Style,Treeview
import pickle


model =tk.StringVar()
vehicle_type = tk.StringVar()
mileage =tk.StringVar()
vendor = tk.StringVar()
reg_number = tk.StringVar()
owner_name = tk.StringVar()
engine_number =tk.StringVar()
V = Vehicle_Collection()




class Vehicle_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vehicle Data Entry")

        #Row 0
        self.owner_label = tk.Label(self.root, text="Owner Name ")
        self.owner_label.grid(row =0,column=0)

        self.owner_entry = tk.Entry(self.root,width=25,textvariable=owner_name)
        self.owner_entry.grid(row=0,column=1)

        self.vendor_label = tk.Label(self.root, text="Vendor Name ")
        self.vendor_label.grid(row =0,column=2)

        self.vendor_entry = tk.Entry(self.root,width=25,textvariable=vendor)
        self.vendor_entry.grid(row=0,column=3)

        add_button = tk.Button(self.root, width=10, text="Add", bg='#99CCFF', command=V.add_vehicle)
        add_button.grid(row=0, column=4)

        Create_pickle_button = tk.Button(self.root, width=10, text="Create Pickle", bg='#99CCFF', command=V.save)
        Create_pickle_button.grid(row=0, column=5)
        
        #Row 1
        self.Model_label = tk.Label(self.root, text="Model ")
        self.Model_label.grid(row =1,column=0)

        self.Model_entry = tk.Entry(self.root,width=25,textvariable=model)
        self.Model_entry.grid(row=1,column=1)

        self.type_label = tk.Label(self.root, text="Car Type ")
        self.type_label.grid(row =1,column=2)

        self.type_entry = tk.Entry(self.root,width=25,textvariable=vehicle_type)
        self.type_entry.grid(row=1,column=3)

        Delete_button = tk.Button(self.root, width=10, text="Delete", bg='#99CCFF', command=V.delete_vehicles)
        Delete_button.grid(row=1, column=4)

        sort_button = tk.Button(self.root, width=10, text="Sort Mileage",bg='#99CCFF', command=V.sort_by_mileage)
        sort_button.grid(row=1, column=5)
        

        #Row 2
        self.Reg_label = tk.Label(self.root, text="Registration Number ")
        self.Reg_label.grid(row =2,column=0)

        self.Reg_entry = tk.Entry(self.root,width=25,textvariable=reg_number)
        self.Reg_entry.grid(row=2,column=1)

        self.Engine_label = tk.Label(self.root, text="Engine ")
        self.Engine_label.grid(row =2,column=2)

        self.Engine_entry = tk.Entry(self.root,width=25,textvariable=engine_number)
        self.Engine_entry.grid(row=2,column=3)

        load_button = tk.Button(self.root, width=10, text="Load Pickle", bg='#99CCFF', command=V.load)
        load_button.grid(row=2, column=4)

        filter_button = tk.Button(self.root, width=10, text="Filter",bg='#99CCFF', command=V.filter_by_attribute)
        filter_button.grid(row=2, column=5)


        # Row 3
        self.Mileage_label = tk.Label(self.root, text="Mileage ")
        self.Mileage_label.grid(row =3,column=0)

        self.Mileage_entry = tk.Entry(self.root,width=25,textvariable=mileage)
        self.Mileage_entry.grid(row=3,column=1)

                
        style = Style()
        style.theme_use("alt")
        style.configure("Treeview",
                        background="silver",
                        foreground='green'
                        )
        style.map('Treeview', background=[('selected', 'grey')])
        treeList = Treeview(columns=("Owner", "Vendor", "Model",
                            "Type", "Reg Number", "Engine", "Mileage"), show='headings')

        treeList.heading("Owner", text="Owner")
        treeList.heading("Vendor", text="Vendor")
        treeList.heading("Model", text="Model")
        treeList.heading("Type", text="Type")
        treeList.heading("Reg Number", text="Reg Number")
        treeList.heading("Engine", text="Engine")
        treeList.heading("Mileage", text="Mileage")

        treeList['show'] = 'headings'

        treeList.column("Owner", width=100, anchor="center")
        treeList.column("Vendor", width=100, anchor="center")
        treeList.column("Model", width=100, anchor="center")
        treeList.column("Type", width=100, anchor="center")
        treeList.column("Reg Number", width=100, anchor="center")
        treeList.column("Engine", width=100, anchor="center")
        treeList.column("Mileage", width=100, anchor="center")

        list_label = tk.Label(self.root, text="Vehicle List", font=("Arial", 14, "bold"))
        list_label.grid(row=5, column=0, columnspan=6, pady=10)


        treeList.grid(row=4, column=0, columnspan=6)






        self.root.mainloop()


# Vehicle_GUI()

V.add_vehicle()