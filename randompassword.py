from tkinter import *
from random import randint

root = Tk()
root.title('Random Password Generator')
root.geometry("500x300")


# Functions
def new_rand():
    # Clearing Entry Box
    pwEntry.delete(0, END)

    # Getting Length of the Password
    pwLength = int(myEntry.get())

    # Holding PAssword
    myPassword = ''

    # Loop
    for x in range(pwLength):
        myPassword += chr(randint(33, 126))

    #output 
    pwEntry.insert(0, myPassword)

def clipper():
    # Clearing the Clipboard
    root.clipboard_clear()
    # Copying to Clipboard
    root.clipboard_append(pwEntry.get())


# Label Frame
lf = LabelFrame(root, text="How many characters?")
lf.pack(pady=20)

# Entry Box for numbers of characters
myEntry = Entry(lf, font=("Helvectica", 24))
myEntry.pack(pady=2, padx=20)

# Entry Box for returned password
pwEntry = Entry(root, text='', font=("Helvectica", 24), bd=0, bg="systembuttonface")
pwEntry.pack(pady=20)

# Frame for buttons
myFrame = Frame(root)
myFrame.pack(pady=20)

# Generate Password Button
btnPrimary = Button(myFrame, text="Generate Password", command=new_rand)
btnPrimary.grid(row=0, column=0, padx=10)

# Copy to Clipboard Button
btnClip = Button(myFrame, text="Copy to Clipboard", command=clipper)
btnClip.grid(row=0, column=1, padx=10)

root.mainloop()