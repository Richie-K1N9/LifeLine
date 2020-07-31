from tkinter import *
import tkinter as tk
import tkinter.font as font
import time
from tkinter import messagebox
from tkinter.messagebox import showinfo

#Window properties
root = Tk()
#root.iconbitmap(r'C:\Users\Richie.King\Documents\GitHub\LifeLine\images\dark_logo.ico') #Icon
root.title("Lifeline") #Title
root.geometry("655x450") #Menu Size
root.configure(bg='#23272A') #Background Colour

h_f = font.Font(weight="bold", size=20)

bmi2 = StringVar()

def bmi_run(): #does calculations
    age_data = dob_box.get("1.0", "end-1c")
    height_data = height_box.get("1.0", "end-1c")
    weight_data = weight_box.get("1.0", "end-1c")
    print("Age: " + age_data)
    print("Height: " + height_data)
    print("Weight: " + weight_data)
    bmi = int(weight_data)/((int(height_data)/100)**2)
    bmi2 = round(bmi,2)
    print(bmi2)
    if bmi2 <= 15.0:
        res = "Your BMI is " + str(bmi2) + "\nRemarks: Very Underweight!!"
        messagebox.showinfo("Result", res)
    elif bmi2 > 15.0 and bmi2 <= 16.0:
        res = "Your BMI is " + str(bmi2) + "\nRemarks: Underweight!"
        messagebox.showinfo("Result", res)
    elif bmi2 > 16.0 and bmi2 < 18.5:
        res = "Your BMI is " + str(bmi2) + "\nRemarks: Slightly Underweight!"
        messagebox.showinfo("Result", res)
    elif bmi2 >= 18.5 and bmi2 <= 25.0:
        res = "Your BMI is " + str(bmi2) + "\nRemarks: Normal."
        messagebox.showinfo("Result", res)
    elif bmi2 > 25.0 and bmi2 <= 30:
        res = "Your BMI is " + str(bmi2) + "\nRemarks: Slightly Overweight."
        messagebox.showinfo("Result", res)
    elif bmi2 > 30.0 and bmi2 <= 35.0:
        res = "Your BMI is " + str(bmi2) + "\nRemarks: Overweight!"
        messagebox.showinfo("Result", res)
    elif bmi2 > 35.0 and bmi2 <= 40.0:
        res = "Your BMI is " + str(bmi2) + "\nRemarks: Obese!"
        messagebox.showinfo("Result", res)
    else:
        res = "Your BMI is " + str(bmi2) + "\nRemarks: Very Obese" + "\n"
        messagebox.showinfo("Result", res)

#Info
title = Label(root, text = "Welcome to Lifeline")
title['font'] = h_f
dob = Label(root, text = "Age", background = '#23272A', fg = 'white')
height = Label(root, text = "Height (In Centermeters)", background='#23272A', fg='white')
weight = Label(root, text = "Weight (In Kgs)", background='#23272A', fg='white')

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

#exercise
ex = Label(root, text = "Recrommended Exercise")
ex['font'] = h_f
ex.grid(row= 9, column= 3)

#pushups
pushup = Label(root, text = "Pushups", background = '#23272A', fg = 'white')
pushup.grid(row=10, column= 2)

instr1 = Label(root, text="1. Get down on all fours, placing your hands slightly wider than your shoulders.", background = '#23272A', fg = 'white')
instr2 = Label(root, text="2. Straighten your arms and legs.", background = '#23272A', fg = 'white')
instr3 = Label(root, text="3. Lower your body until your chest nearly touches the floor.", background = '#23272A', fg = 'white')
instr4 = Label(root, text="4. Pause, then push yourself back up.", background = '#23272A', fg = 'white')
instr5 = Label(root, text="5. Repeat.", background = '#23272A', fg = 'white')

instr1.grid(row=10, column= 3)
instr2.grid(row=11, column= 3)
instr3.grid(row=12, column= 3)
instr4.grid(row=13, column= 3)
instr5.grid(row=14, column= 3)



root.mainloop()