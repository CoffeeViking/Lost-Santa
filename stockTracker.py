from tkinter import messagebox
from tkinter import *
import pickle
import os.path

# Starts dictionary to store information
currentStock = {1234567890: {"stock": 0, "name": "ScottyPoop", "size": "12 oz", "msrp": "$3.99"}                
                }

# Function to print selection to window
def print_selection():
    if rad == '':
        l.config(text='Make a selection!')
    else:
        l.config(text = 'You have selected to ' + rad.get())

# Function to check bcode for invalid characters, routes to proper function
def go():
    if rad.get() == '':
        messagebox.showerror(message="Please select an option!")
    try:
        global bcode
        bcode = int(bcode_entry.get())
    except:
        messagebox.showerror(message="Numerals only, sorry!")
        return
    if rad.get() == 'add':
        add()
    elif rad.get() == 'check':
        check()
    elif rad.get() == 'remove':
        remove()

# Function to Add Item to Inv
def add():
    if bcode not in currentStock:
        print(bcode)
        # Prints labels and entries to window
        nFound_label.place(x=50, y=120)
        name_label.place(x=50, y=140)
        name_entry.place(x=50, y=160)
        size_label.place(x=50, y=180)
        size_entry.place(x=50, y=200)
        msrp_label.place(x=50, y=220)
        msrp_entry.place(x=50, y=240)
        updateButt.place(x=50, y= 260)
    else:
        currentStock[bcode]["stock"] += 1
        l.config(text='Product Added!', message='You have ' + str(currentStock[bcode]["stock"]) + ' ' + str(currentStock[bcode]["name"]))

# Function to add new Item to Dictionary
def updateD(bcode, name, size, msrp):
    currentStock.update({bcode: {"stock": 1, "name": name, "size": size, "msrp": msrp}})
    print(currentStock)
    messagebox.showinfo(message="You have added " + name + " to the DB! You have 1!")
    nFound_label.place_forget()
    name_label.place_forget()
    name_entry.place_forget()
    name_entry.delete(0, 'end')
    size_label.place_forget()
    size_entry.place_forget()
    size_entry.delete(0, 'end')
    msrp_label.place_forget()
    msrp_entry.place_forget()
    msrp_entry.delete(0, 'end')
    updateButt.place_forget()
    bcode_entry.delete(0, 'end')
# Function to Check Item in Inv
def check():
    if bcode not in currentStock:
        messagebox.showinfo(title='Not found!', message='Sorry, I couldnt find this item!')
        bcode_entry.delete(0, 'end')
    else:
        l.config(text='You have ' + str(currentStock[bcode]["stock"]) + ' ' + str(currentStock[bcode]["name"]) + '!')
        bcode_entry.delete(0, 'end')
# Function to Remove Item from Inv
def remove():
    if bcode not in currentStock:
        messagebox.showerror(message="Sorry, this isn't in my system!")
        bcode_entry.delete(0, 'end')
    if currentStock[bcode]["stock"] == 0:
        messagebox.showerror(title='None Found!', message='Sorry, you already dont have any ' + currentStock[bcode]["name"] + '!')
        bcode_entry.delete(0, 'end')
    else:
        currentStock[bcode]["stock"] -= 1
        l.config(text='You now have ' + str(currentStock[bcode]["stock"]) + ' ' + str(currentStock[bcode]["name"]))
        bcode_entry.delete(0, 'end')

# Function to Load Dictionary
def load():
    if os.path.exists('stock.yeet'):
        myFile = open('stock.yeet', 'rb')
        global currentStock
        currentStock = pickle.load(myFile)
        myFile.close()
        l.config(text="Load Successful!")
        stockTracker.after(2000, print_selection)
    else:
        messagebox.showinfo(title='No Saved Database', message='Sorry, there is no existing database!')

#Function to Save Dictionary
def save():
    if os.path.exists('stock.yeet'):
        myFile = open('stock.yeet', 'wb')
        pickle.dump(currentStock, myFile)
        myFile.close()
        l.config(text='Saved Successfully!')
        stockTracker.after(2000, print_selection)
    else:
        answer = messagebox.askokcancel(title='File Not Found', message='No stock.yeet found, Create a new one?')
        if answer:
            myFile = open('stock.yeet', 'wb')
            pickle.dump(currentStock, myFile)
            myFile.close()
            l.config(text="Saved Successfully!")
            stockTracker.after(2000, print_selection)


# Define a User Interface
stockTracker = Tk()
stockTracker.geometry("700x400")
stockTracker.title("Earl's Stock Tracker")
# StringVar is a tkinter thing, helps manage values
rad = StringVar()

# Declare Labels So All Functions Have Access
bcode = None
nFound_label = Label(stockTracker, text="Product Not Found!")
name_label = Label(stockTracker, text="Name of Product")
name_entry = Entry(stockTracker, width=12)
size_label = Label(stockTracker, text="Size of Product")
size_entry = Entry(stockTracker, width=12)
msrp_label = Label(stockTracker, text="What is MSRP?")
msrp_entry = Entry(stockTracker, width=12)
updateButt = Button(stockTracker, text="Update!", command= lambda: updateD(bcode, name_entry.get(), size_entry.get(),msrp_entry.get()))

# Centering Title of App
title_label = Label(stockTracker, text = "Earl's Stock Tracker!")
title_label.pack()

#Create Display for Information
l = Label(stockTracker, bg='white', width=22, text='Make a selection!')
l.pack()

#Radio Buttons
label = Label(text="Add, Check, or Remove?")
r1 = Radiobutton(stockTracker, text='Add', variable=rad, value='add', indicator=0, command=print_selection)
r1.place(x=286, y=45)
r2 = Radiobutton(stockTracker, text='Check', variable=rad, value='check', indicator=0, command=print_selection)
r2.place(x=318, y=45)
r3 = Radiobutton(stockTracker,text='Remove', variable=rad, value='remove', indicator=0, command=print_selection)
r3.place(x=361, y=45)
rDummy = Radiobutton(stockTracker, text='None', variable=rad, value='', indicator=0, command = print_selection)
rDummy.place(x= -100, y=-100)

# Radio Buttons For Load/Save
r4 = Button(stockTracker, text='Load', command=load)
r4.place(x=50, y=45)
r5 = Button(stockTracker, text='Save', command=save)
r5.place(x=87, y=45)

#Get Barcode From User
bcode_label = Label(stockTracker, text='Please enter a barcode number!')
bcode_label.place(x=50, y=75)
bcode_entry = Entry(stockTracker, width=12)
bcode_entry.place(x=50, y=95)
go = Button(stockTracker, text='Go!', command=go)
go.place(x=140, y=95)

#Exit and Close the App
stockTracker.mainloop()
