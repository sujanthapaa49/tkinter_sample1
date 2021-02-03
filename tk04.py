import tkinter as tk
root = tk.Tk()
root.title("Widget")
root.geometry('500x500')
lb = tk.Label(text="Label")
bt = tk.Button(text="Button1")
lb.pack()
bt.pack()
root.mainloop()