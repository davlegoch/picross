from tkinter import *
from debugHelper import *

class Window:
    '''Classe fenêtre'''

    title = "titre"
    width = 300
    height = 150
    resizable = False

    def __init__(self):
        """initialisation"""
        displayInfoClass(self)
        self.window = Tk()

    def setProperties(self, title = "title", width = 130, height = 300):
        """initialise les propriété de la fenêtre"""
        displayInfoClass(self)

        self.title = title
        self.width = width
        self.height = height

        #Applique les modification à la fenêtre
        self.setWindow()

    def setWindow(self):
        """initialise la fenêtre"""
        displayInfoClass(self)

        self.window.title(self.title)
        self.window.geometry("%dx%d" % (self.width, self.height))

        # fen.geometry("%dx%d%+d%+d" % (L, H, X, Y))