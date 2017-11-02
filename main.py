import logging
import tkinter as tk
from grab import Grab
import re
import json
import login

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.g = Grab()
        logging.basicConfig(level=logging.DEBUG)
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Label(self, text="This is my app to send data to "
                                         "https://nok-nark.ru")
        self.label.pack()
        self.quitButton = tk.Button(self, text="Quit", command = lambda:
        self.quit())
        self.quitButton.pack()
        self.loginButton = tk.Button(self, text="Login to nok-nark", command
        = lambda: self.login())
        self.loginButton.pack()

    def login(self):
        self.g.go('https://nok-nark.ru/')
        self.g.doc.set_input('USER_LOGIN', login.LOGIN)
        self.g.doc.set_input('USER_PASSWORD', login.PASSWORD)
        # self.g.go('https://nok-nark.ru/personal/')
        self.g.go('https://nok-nark.ru/personal/center/exam.php')

if __name__ == '__main__':
    app = Application()
    app.master.title("App nok-nark")
    app.mainloop()