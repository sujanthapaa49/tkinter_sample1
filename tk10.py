# -*- coding: utf-8 -*-
# tk09.pyw
import tkinter as tk
root = tk.Tk()
lb = tk.Label(text="MS ゴシック, サイズ20, 太字でない, 斜体, 下線なし, 取り消し線あり", font=("MS ゴシック", 20, "normal", "italic", "normal", "overstrike"))
lb.pack()
root.mainloop()