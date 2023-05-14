from tkinter import *
from tkinter import ttk

from numpy import delete
from c3q4 import *
from tkinter import filedialog
import pickle


# screen = Tk()
# screen.geometry("900x500")
# screen.configure(bg = "grey")
# screen.title("Vehicle Sale Data")
# text= Label(screen, font=('Ariel',15,'bold'),text="VEHICLE DATA",bg="grey")
# text.pack()
# DataFrame = LabelFrame(screen,text="Data",bg = "grey")
# DataFrame.pack(expand="yes",side=RIGHT)
# CarDisplay = ttk.Treeview(DataFrame)
# carData = Vehicle_Collection()


window = Tk()
window.geometry("705x400")
window.title("Vehicle Database")

# row-0
label1 = Label(window, text="Owner ")
label1.grid(row=0, column=0)

entry1 = Entry(window, width=25, textvariable=owner_name)
entry1.grid(row=0, column=1)

label2 = Label(window, text="Vendor ")
label2.grid(row=0, column=2)

entry2 = Entry(window, width=25, textvariable=vendor)
entry2.grid(row=0, column=3)

# row-1
label3 = Label(window, text="Model ")
label3.grid(row=1, column=0)

entry3 = Entry(window, width=25, textvariable=model)
entry3.grid(row=1, column=1)

label4 = Label(window, text="car Type  ")
label4.grid(row=1, column=2)

entry4 = Entry(window, width=25, textvariable=typeClass)
entry4.grid(row=1, column=3)

# row-2
label5 = Label(window, text="Registration Number  ")
label5.grid(row=2, column=0)

entry5 = Entry(window, width=25, textvariable=regNumber)
entry5.grid(row=2, column=1)

label6 = Label(window, text="Engine  ")
label6.grid(row=2, column=2)

entry6 = Entry(window, width=25, textvariable=engNumber)
entry6.grid(row=2, column=3)

# row - 3
label7 = Label(window, text="Mileage")
label7.grid(row=3, column=0)

entry7 = Entry(window, width=25, textvariable=mileage)
entry7.grid(row=3, column=1)

button1 = Button(window, width=10, text="Load Pickle",
                 bg='#fad8b1', command=loadFile)
button1.grid(row=2, column=4)

button8 = Button(window, width=10, text="Filter",
                 bg='#fad8b1', command=filterList)
button8.grid(row=2, column=5)

# second section
# row - 0
button2 = Button(window, width=10, text="Add", bg='#fad8b1', command=addList)
button2.grid(row=0, column=4)

# row - 1
button4 = Button(window, width=10, text="Delete", bg='#fad8b1', command=delete)
button4.grid(row=1, column=4)

button5 = Button(window, width=10, text="Sort Mileage",
                 bg='#fad8b1', command=sortMileage)
button5.grid(row=1, column=5)

button7 = Button(window, width=10, text="Create Pickle",
                 bg='#fad8b1', command=createPickle)
button7.grid(row=0, column=5)


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

list_label = Label(window, text="Vehicle List", font=("Arial", 14, "bold"))
list_label.grid(row=5, column=0, columnspan=6, pady=10)


treeList.grid(row=4, column=0, columnspan=6)
window.mainloop()
