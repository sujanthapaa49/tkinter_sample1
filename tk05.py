import tkinter as tk

def action_btn_press():
    print('Button was pressed!')

root = tk.Tk()
root.title("Widget")
root.geometry('500x500')
lb = tk.Label(text="Label")
bt = tk.Button(text="Button", command=action_btn_press)
lb.pack()
bt.pack()
root.mainloop()