from tkinter import *
import random
import os

def restartProgram():
    os.execl(sys.executable, sys.executable, *sys.argv)

def genFirstAndLast():
    global firstNameDone, lastNameDone
    with open('first-names.txt') as f:
        firstName = f.read().splitlines()
    firstNameDone = random.choice(firstName)
    with open('last-names.txt') as f:
        lastName = f.read().splitlines()
    lastNameDone = random.choice(lastName)

def buildWindow():
    window = Tk()
    window.title("Name Generator")
    window.geometry("300x50")
    #Labels
    lblFirstName = Label(window, text=firstNameDone)
    lblFirstName.grid(column=0, row=1)
    lblLastName = Label(window, text=lastNameDone)
    lblLastName.grid(column=1, row=1)
    #Buttons
    btnNewName = Button(window, text="New Name", command=restartProgram)
    btnNewName.grid(column=0, row=100)
    window.mainloop()

def main():
    genFirstAndLast()
    buildWindow()

main()
