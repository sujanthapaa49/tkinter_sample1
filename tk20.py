
import tkinter as tk
root = tk.Tk()
strvar = tk.StringVar()
print(strvar)
en =tk.Entry(textvariable=strvar)
strvar.set('Hello World')
en.pack()

root.mainloop()