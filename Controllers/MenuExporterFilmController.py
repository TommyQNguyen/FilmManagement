from Views.MenuExporterFilmView import MenuExporterFilm

class MenuExporterFilmController:
    def __init__(self, getBackToMenuPrincipal):
        self.view = MenuExporterFilm()
        self.getBackToMenuPrincipal = getBackToMenuPrincipal

    def init(self):
        self.view.printMenu()
        returnMenuPrincipalUserInput = self.view.getUserInput()
        self.getBackToMenuPrincipal()