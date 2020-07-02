from tkinter import *
import sqlite3

#Startup
root = Tk()
#root.overrideredirect(True)
root.iconbitmap(r'C:\Users\Richie.King\Documents\GitHub\LifeLine\images\dark_logo.ico') #Icon
root.title("LifeLine") #Title
root.geometry("750x450") #Menu Size
#root.configure(bg='#23272A') #Background Colour

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE user")

root.mainloop()