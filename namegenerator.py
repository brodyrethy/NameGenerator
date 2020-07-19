import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    @staticmethod
    def genName(input):
        global finishedName
        with open('first-names.txt') as f:
            firstName = f.read().splitlines()
        firstNameDone = random.choice(firstName)
        with open('last-names.txt') as f:
            lastName = f.read().splitlines()
        lastNameDone = random.choice(lastName)
        finishedName = firstNameDone + " " + lastNameDone
        return finishedName

    def regenName(self):
        self.displayText = tk.Text(self.master, height=2, width =32)
        self.displayText.insert(tk.END, self.genName(""))
        self.displayText.pack()

    def create_widgets(self):

        self.genButton = tk.Button(self)
        self.genButton['text'] = "Generate Name"
        self.genButton['command'] = self.regenName
        self.genButton.pack(side='top')

        self.quit = tk.Button(self, text='QUIT', fg='red', command=self.master.destroy)
        self.quit.pack(side='bottom')

root = tk.Tk()
app = Application(master=root)
app.mainloop()