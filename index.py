from tkinter import *

root = Tk()
#root.overrideredirect(True)
root.iconbitmap(r'C:\Users\Richie.King\Documents\GitHub\LifeLine\images\dark_logo.ico')
root.title("LifeLine")
root.geometry("750x450") #Menu Size
root.configure(bg='#23272A')

L1 = Label(root, text = "First")
L2 = Label(root, text = "Second")

L1.grid(row = 0, column = 0)
L1.grid(row = 1, column = 0)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row = 0, column= 3)
e2.grid(row = 1, column= 2)

root.mainloop()