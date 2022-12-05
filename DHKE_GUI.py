import tkinter as tk

if __name__ == '__main__':

    # Top level window
    frame = tk.Tk()
    frame.title("TextBox Input")


    # Function for getting Input
    # from textbox and printing it
    # at label widget

    def printInput():
        inp = inputTxt.get(1.0, "end-1c")
        # outputtxt.insert(, inp)


    # Input Textbox Creation
    inputTxt = tk.Text(frame, height=5, width=20)
    inputTxt.pack()
    # Output Textbox Creation
    outputTxt = tk.Text(frame, height=5, width=20)
    outputTxt.pack()


    # Button Creation
    printButton = tk.Button(frame,
                            text="Print",
                            command=printInput)
    printButton.pack()

    # Label Creation
    lbl = tk.Label(frame, text="")
    lbl.pack()
    frame.mainloop()

