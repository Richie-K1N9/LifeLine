from tkinter import *
import tkinter as tk
import tkinter.font as font
import time
#import mysql.connector

#Window properties
root = Tk()
#root.overrideredirect(True)
#root.iconbitmap(r'C:\Users\Richie.King\Documents\GitHub\LifeLine\images\dark_logo.ico') #Icon
root.title("LifeLine") #Title
root.geometry("460x450") #Menu Size
#root.configure(bg='#23272A') #Background Colour

h_f = font.Font(weight="bold", size=20)

bmi = 0

def retrieve_input():
    input = self.dob_data.get("1.0","end-1c")
    print(input)

#Info
title = Label(root, text = "Welcome to LifeLine")
title['font'] = h_f
dob = Label(root, text = "Age")
height = Label(root, text = "Height")
weight = Label(root, text = "Weight")

dob_data = tk.StringVar()
height_data = tk.StringVar()
weight_data = tk.StringVar()

#Text Boxes
dob_box = Entry(root, textvariable=dob_data)
height_box = Entry(root, textvariable=height_data)
weight_box = Entry(root, textvariable=weight_data)

#Button
update = Button(root, text="Update", command= retrieve_input)

#Canvas
title.grid(row= 2, column= 3, pady=15)
dob.grid(row= 5, column= 2, pady=5)
height.grid(row= 6, column= 2, pady=5)
weight.grid(row= 7, column= 2, pady=5)
dob_box.grid(row= 5, column= 4, pady=5)
height_box.grid(row= 6, column= 4, pady=5)
weight_box.grid(row= 7, column= 4, pady=5)
update.grid(row= 8, column= 3)

bmi = Label(root, text = input)
bmi.grid(row= 9, column= 3)

root.mainloop()