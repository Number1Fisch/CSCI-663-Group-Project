from tkinter import *
from tkinter.ttk import *

if __name__ == '__main__':
    # create window
    frame = Tk()
    frame.title("DHKE")
    frame.geometry('100x100')
    frame.grid(6, 2, 1, 1)

    # variables for key values
    p = 0
    a = 0
    B = 0
    commonKey = 0

    # labels
    PrimeLabel = Label(frame, text="Prime Number: ")
    AlphaLabel = Label(frame, text="Alpha: ")
    BLabel = Label(frame, text="Receiver/Sender value (A/B): ")
    CommonKeyLabel = Label(frame, text="Common Key: ")

    # text boxes
    PrimeBox = Entry(frame, textvariable=p)
    AlphaBox = Entry(frame, textvariable=a)
    BBox = Entry(frame, textvariable=B)
    CommonKeyBox = Entry(frame)
    # buttons
    BButton = Button(frame, text="Calculate B")
    CommonButton = Button(frame, text="Calculate Common Key")

    # construct grid for elements
    PrimeLabel.grid(row=0, column=0, sticky=E)
    PrimeBox.grid(row=0, column=1, sticky=W)

    AlphaLabel.grid(row=1, column=0, sticky=E)
    AlphaBox.grid(row=1, column=1, sticky=W)

    BButton.grid(row=2, column=0, columnspan=2, sticky=N,)

    BLabel.grid(row=3, column=0, sticky=E)
    BBox.grid(row=3, column=1, sticky=W)

    CommonButton.grid(row=4, column=0, columnspan=2, sticky=N)

    CommonKeyLabel.grid(row=5, column=0, sticky=E)
    CommonKeyBox.grid(row=5, column=1, sticky=W)

    # add weight so application fills window size
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=2)
    frame.rowconfigure(3, weight=1)
    frame.rowconfigure(4, weight=2)
    frame.rowconfigure(5, weight=2)
    frame.rowconfigure(5, weight=2)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.mainloop()
