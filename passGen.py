import random
from tkinter import messagebox
from tkinter import *

def generate_password():
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
    except:
        messagebox.showerror(message="Please key in the required inputs!")
        return
    #Check if user allows repitition of characters
    if repeat == 1:
        password = random.sample(character_string, length)
    else:
        password = random.choices(character_string, k=length)
    #Convert returned list into string
    password = ''.join(password)
    #Declare a string variable
    password_v = StringVar()
    password = "Created Password: " + str(password)
    #Assign the password to the declared string variables
    password_v.set(password)
    #create a read only entry box to view the output, position using place
    password_label = Entry(password_gen, bd=0, bg="gray85", textvariable= password_v, state="readonly")
    password_label.place(x=10, y=140, height=50, width=320)

#Define a string containing letters, symbols, and numbers
character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`~!@#$%^&*()-_=+"

#Define a user interface
password_gen = Tk()
password_gen.geometry("350x200")
password_gen.title("Totally Original and Not Copied Password Generator") #Actually from pythongeeks.org/python-password-generator

#Mention the title of the app
#Label arguments are (windows of the screen, text to display, optional font styling)
title_label = Label(password_gen, text = "Totally Original and Not Copied Password Generator", font=("Ubuntu Mono",12))
title_label.pack()
#Read Length
length_label = Label(password_gen, text="Enter length of password: ")
length_label.place(x=20, y=30)
length_entry = Entry(password_gen, width=3)
length_entry.place(x=190,y=30)
#Read repitition
repeat_label = Label(password_gen, text="Repitition? 1: no repitition, 2: otherwise: ")
repeat_label.place(x=20,y=60)
repeat_entry = Entry(password_gen, width=3)
repeat_entry.place(x=300,y=60)
#Generate password
password_button = Button(password_gen, text = "Generate Password", command=generate_password)
password_button.place(x=100,y=100)
#Exit and close the App
password_gen.mainloop()
