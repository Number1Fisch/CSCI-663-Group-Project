import DiffieHellman.py
import RSAEncryption.py
from tkinter import *
from tkinter import ttk
# This is the GUI file for the CSCI 663 Group Project

root = Tk()
frm = ttk.Frame(root, padding = 10)
frm.grid()
ttk.Label(frm, text="Crypto Demo").grid(column = 0, row = 0)
ttk.Button(frm, text="Quit", command = root.destroy).grid(column = 1, row = 0)
root.mainloop()
