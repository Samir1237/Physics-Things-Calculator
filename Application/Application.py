from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text = "Simple figure calculator")
        self.msg.pack()

        self.exit = Button(self.widget1)
        self.exit["text"] = "Exit"
        self.exit["width"] = 10
        self.exit.bind("<Button-1>", self.changeText)
        self.exit.pack()

    def changeText(self, event):
        if self.msg["text"] == "Simple figure widget":
            self.msg["text"] = "Pressed"
        else:
            self.msg["text"] = "Main widget"
root = Tk()
Application(root)
root.mainloop()

#nothing is working yet