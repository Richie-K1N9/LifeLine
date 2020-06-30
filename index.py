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

#Database connection
data = sqlite3.connect('user.db')

d = data.cursor()

d.exectue("""CREATE TABLE user (
    first_name text,
    last_name text,
    

)
    """)

data.commit()

data.close()

L1 = Label(root, text = "G'Day ")
L2 = Label(root, text = "Second")

L1.grid(row = 1, column = 0)
L1.grid(row = 2, column = 0)


root.mainloop()