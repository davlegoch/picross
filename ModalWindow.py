from debugHelper import *
import tkinter as tk
#from tkinter import *

class ModalWindow(tk.Toplevel):
    """création de fenêtre modale"""
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Fenêtre modale")

        tk.Label(self, text="Label").pack()
        self.entry = tk.Entry(self)
        self.entry.pack()

        tk.Button(self, text="boutton", command=self.connect).pack()

    def connect(self):
        mot = self.entry.get().strip()
        print("infos ", mot)
        self.destroy()

