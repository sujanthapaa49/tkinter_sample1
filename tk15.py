import tkinter as tk
root = tk.Tk()
root.geometry('300x270')
ms_dict ={}

for bw_int in range (1,6):
    bw_str=str(bw_int)
    ms_dict[bw_str] = tk.Message(text='border_width='+bw_str, relief='ridge', bd=bw_int)
    ms_dict[bw_str].pack()
root.mainloop()