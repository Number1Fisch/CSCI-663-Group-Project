# import tkinter module
import tkinter
from tkinter import *
from tkinter.ttk import *

# creates window
encrypt = Tk()
encrypt.geometry("200x100")
encrypt.grid(2, 2, 1, 1)
# variables for encryption values
pubKey = (0, 0)
plainText = tkinter.StringVar()
cipherText = ""

# labels
PubKeyLabel = Label(encrypt, text="Public Key:")
PlainTextLabel = Label(encrypt, text="Plain Text:")
CipherTextLabel = Label(encrypt, text="Cipher Text:")

# text boxes
PubKeyBox = Entry(encrypt, textvariable=pubKey, width=4)
PubKeyBox.insert(INSERT, "(n, e)")
PlainTextBox = Text(encrypt, width=40, height=10)
CipherTextBox = Text(encrypt, width=40, height=10)

# buttons
EncryptButton = Button(encrypt, text="Encrypt")

# construct grid for elements

PlainTextLabel.grid(row=0, column=0, sticky=N)
PlainTextBox.grid(row=1, column=0, rowspan=2, sticky=NSEW)

PubKeyLabel.grid(row=0, column=1, ipadx=5, sticky=N)
PubKeyBox.grid(row=1, column=1, ipadx=5, sticky=N)

EncryptButton.grid(row=2, column=1, sticky=N)

CipherTextLabel.grid(row=0, column=2, sticky=N)
CipherTextBox.grid(row=1, column=2, rowspan=2, sticky=NSEW)
CipherTextBox.insert(END, cipherText)

# add weight so application fills window size
encrypt.rowconfigure(0, weight=1)
encrypt.rowconfigure(1, weight=1)
encrypt.rowconfigure(2, weight=8)

encrypt.columnconfigure(0, weight=5)
encrypt.columnconfigure(1, weight=1)
encrypt.columnconfigure(2, weight=5)