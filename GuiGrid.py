from tkinter import *
from debugHelper import *

class GuiGrid:
    """Gestion de la grille d'affichage"""

    height = 400
    width = 400
    x = 10
    y = 0
    padLeft = 0
    padTop = 0
    color = "white"

    colorCode = ['white', 'black', 'red']

    rectangle_padLeft = 20
    rectangle_padTop = 20
    rectangle_nb_row = 10
    rectangle_nb_column = 10
    rectangle_height = 20
    rectangle_width = 20

    def __init__(self, window, nbRow = 10, nbColumn = 10):
        """initialisation"""
        displayInfoClass(self)

        self.canvas = Canvas(window, width=self.width, height=self.height, bg=self.color)
        #self.canvas.place(x=self.padLeft, y=self.padTop)
        self.canvas.place(x=self.x, y=self.y)

        self.nbRow = nbRow;
        self.nbColumn = nbColumn;
        self.drawEmpty()

    def setProperties(self, title = "title", width = 130, height = 300):
        displayInfoClass(self)
        self.width = pWidth
        self.height = pHeight
        self.window = pWindow

    def drawEmpty(self):
        """dessine la grille"""
        displayInfoClass(self)

        self.rectangleTab = [[1] * self.nbRow for n in range(self.nbColumn)]
        x = self.padLeft
        y = self.padTop
        for row in range(0, self.nbRow):
            for column in range(0, self.nbColumn):
                self.rectangleTab[row][column] = self.canvas.create_rectangle(x, y, x + self.rectangle_width, y + self.rectangle_height)
                x += self.rectangle_width
            y += self.rectangle_height
            x = self.padLeft
        print(self.rectangleTab)

    def fill(self, template):
        """rempli une grille vide avec les éléments de jeu"""
        displayInfoClass(self)

        for row in range(0, len(template)):
            for column in range(0, len(template[row])):
                self.changeColor(row, column, template[row][column])

    def getCoordonate(self, mouseX, mouseY):
        x = (mouseX - self.padLeft) / self.rectangle_width
        y = (mouseY - self.padTop) / self.rectangle_height

        if (x < 0) or (x > self.nbColumn) or (y < 0) or (y > self.nbRow):
            return(None, None)
        else:
            return [int(x), int(y)]

    def changeColor(self, x, y, status):
        """change la couleur d'une cellule"""
        #displayInfoClass(self)

        self.canvas.itemconfigure(self.rectangleTab[y][x], fill=self.colorCode[status])
