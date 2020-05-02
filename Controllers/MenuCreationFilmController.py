from Views.MenuCreationFilmView import MenuCreationFilm
from Models.FilmModel import FilmModel


class MenuCreationFilmController:
    def __init__(self, getBackToMenuPrincipal):
        self.view = MenuCreationFilm()
        self.getBackToMenuPrincipal = getBackToMenuPrincipal

    def getFilmInput(self):
        return self.view.printAndSendForm()

    def init(self):
        self.view.printMenu()
        nouveauFilm = self.getFilmInput()
        FilmModel().createFilm(nouveauFilm)
        returnMenuPrincipalUserInput = self.view.getUserInput()
        self.getBackToMenuPrincipal()
