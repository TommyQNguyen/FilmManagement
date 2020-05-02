from Views.MenuAfficherLesFilmsView import MenuAfficherFilms
from Models.FilmModel import FilmModel


class MenuAfficherLesFilmsController:
    def __init__(self, getBackToMenuPrincipal):
        self.view = MenuAfficherFilms()
        self.getBackToMenuPrincipal = getBackToMenuPrincipal

    def init(self):
        self.view.printMenu()
        films = FilmModel().getFilms()
        self.view.printList(filmList=films)
        returnMenuPrincipalUserInput = self.view.getUserInput()
        self.getBackToMenuPrincipal()
