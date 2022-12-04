import DHKE_GUI as DHKE
import RSA_GUI as RSA
from tkinter import *
from tkinter import ttk
# This is the GUI file for the CSCI 663 Group Project

root = Tk()
frm = ttk.Frame(root, padding = 10)
frm.grid()
ttk.Label(frm, text="Crypto Demo").grid(column = 3, row = 0)
ttk.Button(frm, text="RSA Encryption", command = RSA.run).grid(column = 2, row = 1)
ttk.Button(frm, text="Diffie Hellman Key Exchange", command = DHKE.run).grid(column = 4, row = 1)
ttk.Button(frm, text="Quit", command = root.destroy).grid(column = 3, row = 3)
root.mainloop()
