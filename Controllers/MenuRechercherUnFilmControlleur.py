from Views.MenuRechercherUnFilmView import MenuRechercherUnFilm

class MenuRechercherUnFilmController:
    def __init__(self, getBackToMenuPrincipal):
        self.view = MenuRechercherUnFilm()
        self.getBackToMenuPrincipal = getBackToMenuPrincipal

    def init(self):
        self.view.printMenu()
        returnMenuPrincipalUserInput = self.view.getUserInput()
        self.getBackToMenuPrincipal()
