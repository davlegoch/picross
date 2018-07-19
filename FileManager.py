from debugHelper import *

class FileManager:
    '''outils de chargement et sauvegarde de jeu'''
    #chargement fichier
    #sauvegarde grille
    #sauvegarde partie
    folderGrid = 'Files\\'

    def loadGrid(self, fileName):
        '''charge une grille'''
        grid = []
        with open(self.folderGrid + fileName, 'r') as file:
            for row in file.read().split("\n"):
                grid.append(list(row))

        for row in range(0, len(grid)):
            for column in range(0, len(grid[row])):
                grid[row][column] = int(grid[row][column])

        return grid

    def saveGrid(self, fileName, content):
        '''sauvegarde une grille'''
        file = open(self.folderGrid + fileName, 'w')
        for row in range(0, len(content)):
            print(content[row])
            for column in range(0, len(content[row])):
                file.write(str(content[row][column]))
            if (len(content)-1 != row):
                file.write('\n')
        file.close()

    def saveGame(self, fileName, content):
        '''sauvegarde une partie en cours'''