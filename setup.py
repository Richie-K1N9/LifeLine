from tkinter import *
import tkinter as tk
import tkinter.font as font
import time
#import mysql.connector

#Window properties
root = Tk()
#root.overrideredirect(True)
root.iconbitmap(r'C:\Users\Richie.King\Documents\GitHub\LifeLine\images\dark_logo.ico') #Icon
root.title("LifeLine") #Title
root.geometry("475x450") #Menu Size
root.configure(bg='#23272A') #Background Colour

#Database
#db = mysql.connector.connect(
#    host="localhost",
#    user="yourusername",
#    password="yourpassword",
#    database="data"
#)
#
#mycursor = db.cursor()
#
#mycursor.execute("CREATE TABLE data (f_name VARCHAR(255), l_name VARCHAR(255))")

#Bold font var
h_f = font.Font(weight="bold", size=20)

#Variables
_data = StringVar()
_data = StringVar()
_data = StringVar()
_data = StringVar()
_data = StringVar()

#Info
title = Label(root, text = "Welcome to LifeLine")
title['font'] = h_f
f_name = Label(root, text = "First Name")
l_name = Label(root, text = "Last Name")
dob = Label(root, text = "Age")
height = Label(root, text = "Height")
weight = Label(root, text = "Weight")

f_data = tk.StringVar()
l_data = tk.StringVar()
dob_data = tk.StringVar()
height_data = tk.StringVar()
weight_data = tk.StringVar()

#Text Boxes
f_name_box = Entry(root, textvariable=f_data)
l_name_box = Entry(root, textvariable=l_data)
dob_box = Entry(root, textvariable=dob_data)
height_box = Entry(root, textvariable=height_data)
weight_box = Entry(root, textvariable=weight_data)

#Canvas
title.grid(row= 2, column= 3, pady=15)
f_name.grid(row= 3, column= 2, pady=5)
l_name.grid(row= 4, column= 2, pady=5)
dob.grid(row= 5, column= 2, pady=5)
height.grid(row= 6, column= 2, pady=5)
weight.grid(row= 7, column= 2, pady=5)
f_name_box.grid(row= 3, column= 4, pady=5)
l_name_box.grid(row= 4, column= 4, pady=5)
dob_box.grid(row= 5, column= 4, pady=5)
height_box.grid(row= 6, column= 4, pady=5)
weight_box.grid(row= 7, column= 4, pady=5)

#Output Data
well = Label(root, text="Welcome " + f_name_box.get())

#Output Grid
well.grid(row= 8, column=2, pady=10)

root.mainloop()
