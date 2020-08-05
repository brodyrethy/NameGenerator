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
        self.displayText = tk.Text(self.textFrame, height=2, width =32)
        self.displayText.insert(tk.END, self.genName(""))
        self.displayText.pack()

    def create_widgets(self):
        self.buttonFrame=tk.Frame()
        self.buttonFrame.pack(padx=5,pady=10)

        self.textFrame =tk.Frame()
        self.textFrame.pack()

        self.genButton = tk.Button(self.buttonFrame, text='Generate Name', command=self.displayName)
        self.genButton.pack(side='left', padx=5)

        self.quit = tk.Button(self.buttonFrame, text='QUIT', fg='red', command=self.master.destroy)
        self.quit.pack(side='right', padx=5)

        self.clear = tk.Button(self.buttonFrame, text='Clear', command=self.clearBox)
        self.clear.pack(padx=5)

    def clearBox(self):
        for widget in self.textFrame.winfo_children():
            widget.pack_forget()
            widget.destroy()

root = tk.Tk()
root.geometry('{}x{}'.format(250,320))
app = Application(master=root)
app.mainloop()
