from Views.MenuRechercherUnFilmView import MenuRechercherUnFilm
from Models.FilmModel import FilmModel


class MenuRechercherUnFilmController:
    def __init__(self, getBackToMenuPrincipal):
        self.view = MenuRechercherUnFilm()
        self.getBackToMenuPrincipal = getBackToMenuPrincipal

    def getUserSearchInput(self):
        return self.view.askForSearchInput()

    def init(self):
        self.view.printMenu()
        filmToSearch = self.getUserSearchInput()
        filmsFromSearch = FilmModel().getFilmListByName(filmToSearch)
        self.view.printList(filmsFromSearch)
        returnMenuPrincipalUserInput = self.view.getUserInput()
        self.getBackToMenuPrincipal()
