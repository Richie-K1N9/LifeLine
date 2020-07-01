from tkinter import *
from PIL import ImageTk, Image
import sqlite3

#Startup
root = Tk()
#root.overrideredirect(True)
root.iconbitmap(r'C:\Users\Richie.King\Documents\GitHub\LifeLine\images\dark_logo.ico') #Icon
root.title("LifeLine") #Title
root.geometry("750x450") #Menu Size
#root.configure(bg='#23272A') #Background Colour

data = sqlite3.connect('user.db')
	
d = data.cursor()

d.execute('''CREATE TABLE user (first_name text, last_name text, date_of_birth text, height text, weight text)''')

#Submit Function for Database
def submit():

	#Create Database or connect
	data = sqlite3.connect('user.db')
	
	#Create cursor
	d = data.cursor()
	
	#Insert into Table
	
	#Commit Changes
	data.commit()
	
	#Close Connection
	data.close()
	
	#Clear Boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	d_o_b.delete(0, END)
	height.delete(0, END)
	weight.delete(0, END)
	
#Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
d_o_b = Entry(root, width=30)
d_o_b.grid(row=2, column=1)
height = Entry(root, width=30)
height.grid(row=3, column=1)
weight = Entry(root, width=30)
weight.grid(row=4, column=1)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
d_o_b_label = Label(root, text="Date of Birth")
d_o_b_label.grid(row=2, column=0)
height_label = Label(root, text="Height")
height_label.grid(row=3, column=0)
weight_label = Label(root, text="Weight")
weight_label.grid(row=4, column=0)

submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=5, column=0)

root.mainloop()