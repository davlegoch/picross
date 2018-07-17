from debugHelper import *
from tkinter import *
from Window import *
from GuiGrid import *
from FileManager import *


class GUI:
    """interface utilisateur"""
    '''
    window
    gridGame
    gridNumbers
    buttons
    '''
    previous_x = -1
    previous_y = -1

    def __init__(self):
        """initialisation"""
        displayInfoClass(self)

        self.mainWindow = Window()
        self.mainWindow.setProperties('Python PICROSS', 800, 600)

    def launchGameLoop(self):
        self.mainWindow.window.mainloop()

    def drawGrid(self, nbRow, nbColumn):
        self.grid = GuiGrid(self.mainWindow.window, nbRow, nbColumn)

    def createInterfaceFileManager(self, saveGridEvent, loadGridEvent):
        '''création des éléments d'interface pour la gestion des fichiers'''

        self.saveButton = Button(self.mainWindow.window, text="Save", width=20, command=saveGridEvent)
        self.saveButton.place(x=450, y=10)

        self.saveButton = Button(self.mainWindow.window, text="Load", width=20, command=loadGridEvent)
        self.saveButton.place(x=450, y=50)

