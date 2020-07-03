from tkinter import *
import sqlite3

#Startup
root = Tk()
#root.overrideredirect(True)
#root.iconbitmap(r'C:\Users\Richie.King\Documents\GitHub\LifeLine\images\dark_logo.ico') #Icon
root.title("LifeLine") #Title
root.geometry("350x450") #Menu Size
#root.configure(bg='#23272A') #Background Colour

title = Label(root, text = "Welcome to LifeLine")
f_name = Label(root, text = "First Name")
l_name = Label(root, text = "Last Name")
dob = Label(root, text = "Date of Birth")
height = Label(root, text = "Height")
weight = Label(root, text = "Weight")

f_name_box = Entry(root)
l_name_box = Entry(root)
dob_box = Entry(root)
height_box = Entry(root)
weight_box = Entry(root)

title.grid(row= 2, column= 3)
f_name.grid(row= 3, column= 2)
f_name_box.grid(row= 3, column= 4)
l_name.grid(row= 4, column= 2)
l_name_box.grid(row= 4, column= 4)
dob.grid(row= 5, column= 2)
dob_box.grid(row= 5, column= 4)
height.grid(row= 6, column= 2)
height_box.grid(row= 6, column= 4)
weight.grid(row= 7, column= 2)
weight_box.grid(row= 7, column= 4)

root.mainloop()
