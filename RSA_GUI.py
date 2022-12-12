import tkinter as tk
from tkinter import ttk

import RSA_Decrypt_Tab
import RSA_Encrypt_Tab

root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Encrypt')
tabControl.add(tab2, text='Decrypt')
tabControl.pack(expand=1, fill="both")

root.mainloop()