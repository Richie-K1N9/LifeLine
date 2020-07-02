import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Welcome to Lifeline")
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
label.pack()

window.mainloop()
