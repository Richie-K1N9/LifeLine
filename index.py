from tkinter import *
import tkinter as tk
import tkinter.font as font
import time
#import mysql.connector

#Window properties
root = Tk()
#root.overrideredirect(True)
#root.iconbitmap(r'C:\Users\Richie.King\Documents\GitHub\LifeLine\images\dark_logo.ico') #Icon
root.title("Lifeline") #Title
root.geometry("460x450") #Menu Size
#root.configure(bg='#23272A') #Background Colour

h_f = font.Font(weight="bold", size=20)

bmi2 = StringVar()

def bmi_run():
    age_data = dob_box.get("1.0", "end-1c")
    height_data = height_box.get("1.0", "end-1c")
    weight_data = weight_box.get("1.0", "end-1c")
    print("Age: " + age_data)
    print("Height: " + height_data)
    print("Weight: " + weight_data)
    bmi = int(weight_data)/((int(height_data)/100)**2)
    bmi2 = round(bmi,2)
    print(bmi2)
    self.label['bmi2'] = bmi2

#Info
title = Label(root, text = "Welcome to Lifeline")
title['font'] = h_f
dob = Label(root, text = "Age")
height = Label(root, text = "Height (In Meters)")
weight = Label(root, text = "Weight (In Kgs)")

#Text Boxes
dob_box = Text(root, height= 1, width= 10)
height_box =Text(root, height= 1, width= 10)
weight_box = Text(root, height= 1, width= 10)

#Button
update = Button(root, text="Update", command= bmi_run)

#Canvas
title.grid(row= 2, column= 3, pady=15)
dob.grid(row= 5, column= 2, pady=5)
height.grid(row= 6, column= 2, pady=5)
weight.grid(row= 7, column= 2, pady=5)
dob_box.grid(row= 5, column= 4, pady=5)
height_box.grid(row= 6, column= 4, pady=5)
weight_box.grid(row= 7, column= 4, pady=5)
update.grid(row= 8, column= 3)

bmi_text = Label(root, text = bmi2)
bmi_text.grid(row= 9, column= 3)

root.mainloop()