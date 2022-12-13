# import tkinter module
import tkinter
from tkinter import *
from tkinter.ttk import *

if __name__ == '__main__':

    # creates window
    root = Tk()
    root.title("RSA Encryption")
    root.geometry("200x100")
    root.grid(5, 2, 1, 1)
    # variables for encryption values
    pubKey = (0, 0)
    privateKey = 0
    plainText = ""
    cipherText = ""

    # labels
    PubKeyLabel = Label(root, text="Public Key")
    PrivateKeyLabel = Label(root, text="Private Key")
    PlainTextLabel = Label(root, text="Plain Text")
    CipherTextLabel = Label(root, text="Cipher Text")

    # text boxes
    PubKeyBox = Entry(root, textvariable=pubKey, width=4)
    PubKeyBox.insert(INSERT, "(n, e)")
    PrivateKeyBox = Entry(root, textvariable=privateKey, width=4)
    PrivateKeyBox.insert(INSERT, "d")
    PlainTextBox = Text(root, width=40, height=10)
    CipherTextBox = Text(root, width=40, height=10)

    # buttons
    EncryptButton = Button(root, text="Encrypt")
    DecryptButton = Button(root, text="Decrypt")

    # construct grid for elements

    CipherTextLabel.grid(row=0, column=0, sticky=N)
    CipherTextBox.grid(row=1, column=0, rowspan=5, sticky=NSEW)
    CipherTextBox.insert(INSERT, cipherText)

    PubKeyLabel.grid(row=0, column=1, ipadx=5, sticky=N)
    PubKeyBox.grid(row=1, column=1, ipadx=5, sticky=N)
    EncryptButton.grid(row=2, column=1, sticky=N)

    PrivateKeyLabel.grid(row=3, column=1)
    PrivateKeyBox.grid(row=4, column=1)
    DecryptButton.grid(row=5, column=1)

    PlainTextLabel.grid(row=0, column=2, sticky=N)
    PlainTextBox.grid(row=1, column=2, rowspan=5, sticky=NSEW)
    PlainTextBox.insert(INSERT, plainText)

    # add weight so application fills window size
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=2)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=2)

    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=2)
    root.columnconfigure(2, weight=4)
    root.mainloop()