from Views.MenuCreationFilmView import MenuCreationFilm

class MenuCreationFilmController:
    def __init__(self, getBackToMenuPrincipal):
        self.view = MenuCreationFilm()
        self.getBackToMenuPrincipal = getBackToMenuPrincipal

    def init(self):
        self.view.printMenu()
        returnMenuPrincipalUserInput = self.view.getUserInput()
        self.getBackToMenuPrincipal()

