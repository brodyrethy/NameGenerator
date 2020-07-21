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

    def displayName(self):
        self.displayText = tk.Text(self.displayFrame, height=2, width =32)
        self.displayText.insert(tk.END, self.genName(""))
        self.displayText.pack()

    def create_widgets(self):
        self.genButton = tk.Button(self, text='Generate Name', command=self.displayName)
        self.genButton.pack(side='top')

        self.quit = tk.Button(self, text='QUIT', fg='red', command=self.master.destroy)
        self.quit.pack(side='bottom')

        self.displayFrame =tk.Frame()
        self.displayFrame.pack()

        self.clear = tk.Button(self, text='Clear', command=self.clearBox)
        self.clear.pack(side='bottom')

    def clearBox(self):
        for widget in self.displayFrame.winfo_children():
            widget.pack_forget()
            widget.destroy()

root = tk.Tk()
root.geometry('{}x{}'.format(250,320))
app = Application(master=root)
app.mainloop()