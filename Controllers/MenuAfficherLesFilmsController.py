from Views.MenuAfficherLesFilmsView import MenuAfficherFilms

class MenuAfficherLesFilmsController:
    def __init__(self, getBackToMenuPrincipal):
        self.view = MenuAfficherFilms()
        self.getBackToMenuPrincipal = getBackToMenuPrincipal

    def init(self):
        self.view.printMenu()
        returnMenuPrincipalUserInput = self.view.getUserInput()
        self.getBackToMenuPrincipal()




