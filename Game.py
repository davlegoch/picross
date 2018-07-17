from debugHelper import *
from FileManager import *

class Game:
    '''Classe de gestion du fonctionnement du jeu'''

    def __init__(self):
        '''initialisation'''
        displayInfoClass(self)

    def loadGrid(self):
        '''chargement d'une nouvelle grille de jeu'''
        displayInfoClass(self)

        self.grid = [[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,1]]

    def updateGrid(self, row, column, status = None):
        '''modifie l'état d'une case'''
        if(status is None):
            if self.grid[row][column] == 1:
                status = 0
            else:
                status = 1

        self.grid[row][column] = status
