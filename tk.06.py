import tkinter as tk

def print_txtval():

    val_en = en.get()
    print(val_en)

root=tk.Tk()
root.title('Get text box')
root.geometry('350x300')
lb=tk.Label(text='label')
en=tk.Entry()
bt=tk.Button(text='Button', command=print_txtval)
#lb.pack()
#en.pack()
#bt.pack()
[widget.pack()for widget in [lb,bt,en]]
root.mainloop()