'''
Point d'entrée du jeu
'''
print("\n############################################\n########## Python PICROSS ##################\n############################################\n")

from debugHelper import *
from GUI import *
from Game import *
from ModalWindow import *


def exitEvent(event):
    GUI.quit()

def changeGridEvent(event):
    #detect position
    x, y = gui.grid.getCoordonate(event.x, event.y)

    if (x is None) or (y is None):
        '''do nothnig'''
    else:
        # change statut cell
        game.updateGrid(x, y)

        #change color grid cell
        gui.grid.changeColor(x, y, game.grid[x][y])

    gui.previous_x = x
    gui.previous_y = y

def mouseMoveEvent(event):
    x, y = gui.grid.getCoordonate(event.x, event.y)
    print(x, ' / ', y)
    if (x is None) or (y is None):
        '''do nothnig'''
    else:
        if gui.previous_x == x and gui.previous_y == y:
            '''do nothing'''
        else:
            # change statut cell
            game.updateGrid(x, y)

            #change color grid cell
            gui.grid.changeColor(x, y, game.grid[x][y])

    gui.previous_x = x
    gui.previous_y = y

def saveGridEvent():
    fen_modal = ModalWindow(gui.mainWindow.window)
    fen_modal.transient(gui.mainWindow.window)
    fen_modal.grab_set()
    gui.mainWindow.window.wait_window(fen_modal)

    fileManager = FileManager()
    fileManager.saveGrid('new_file.txt', game.grid)

def loadGridEvent():
    fileManager = FileManager()
    game.grid = fileManager.loadGrid('new_file.txt')
    print(game.grid)
    gui.grid.fill(game.grid)

#gui.createWindows
gui = GUI()

#game.loadGrid
game = Game()
game.loadGrid()

#gui.displayGrid
gui.drawGrid(len(game.grid), len(game.grid[0]))
gui.grid.fill(game.grid)

#gui.createInterfaceFileManager
gui.createInterfaceFileManager(saveGridEvent, loadGridEvent)

#game.generateNumbers

#gui.displayNumbers

#gui.displayInterface


#events
gui.mainWindow.window.bind("<Escape>", exit)
gui.grid.canvas.bind("<Button-1>", changeGridEvent)
gui.grid.canvas.bind("<B1-Motion>", mouseMoveEvent)

#gameLoop
gui.launchGameLoop()

