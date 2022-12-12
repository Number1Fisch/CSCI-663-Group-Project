# import tkinter module
import tkinter
from tkinter import *
from tkinter.ttk import *

# creates window
decrypt = Tk()
decrypt.geometry("200x100")
decrypt.grid(2, 2, 1, 1)
# variables for encryption values
pubKey = (0, 0)
plainText = tkinter.StringVar()
cipherText = ""

# labels
PubKeyLabel = Label(decrypt, text="Public Key:")
PlainTextLabel = Label(decrypt, text="Plain Text:")
CipherTextLabel = Label(decrypt, text="Cipher Text:")

# text boxes
PubKeyBox = Entry(decrypt, textvariable=pubKey, width=4)
PubKeyBox.insert(INSERT, "(n, e)")
PlainTextBox = Text(decrypt, width=40, height=10)
CipherTextBox = Text(decrypt, width=40, height=10)

# buttons
EncryptButton = Button(decrypt, text="Decrypt")

# construct grid for elements

CipherTextLabel.grid(row=0, column=0, sticky=N)
CipherTextBox.grid(row=1, column=0, rowspan=2, sticky=NSEW)

PubKeyLabel.grid(row=0, column=1, ipadx=5, sticky=N)
PubKeyBox.grid(row=1, column=1, ipadx=5, sticky=N)

EncryptButton.grid(row=2, column=1, sticky=N)

PlainTextLabel.grid(row=0, column=2, sticky=N)
PlainTextBox.grid(row=1, column=2, rowspan=2, sticky=NSEW)
PlainTextBox.insert(END, cipherText)

# add weight so application fills window size
decrypt.rowconfigure(0, weight=1)
decrypt.rowconfigure(1, weight=1)
decrypt.rowconfigure(2, weight=8)

decrypt.columnconfigure(0, weight=5)
decrypt.columnconfigure(1, weight=1)
decrypt.columnconfigure(2, weight=5)