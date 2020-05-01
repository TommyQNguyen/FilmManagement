from Views.MenuPrincipalView import MenuPrincipal

# controllers
from Controllers.MenuCreationFilmController import MenuCreationFilmController
from Controllers.MenuAfficherLesFilmsController import MenuAfficherLesFilmsController
from Controllers.MenuRechercherUnFilmControlleur import MenuRechercherUnFilmController
from Controllers.MenuGererLesCategoriesController import MenuGererLesCategoriesController

class MenuPrincipalController:
    def __init__(self):
        # declarer la vue associer au controlleur
        self.view = MenuPrincipal()

    #  initialise la vue et la communication entre cont et vue
    def init(self):
        self.view.printMenu()
        inputChoice = self.view.getUserInput()
        self.navigate(menuChoice=inputChoice)
    

    # etablie la communication a d'autre controlleurs
    def navigate(self, menuChoice):
        if menuChoice == '1' : MenuCreationFilmController(getBackToMenuPrincipal=self.init).init()
        if menuChoice == '2' : MenuAfficherLesFilmsController(getBackToMenuPrincipal=self.init).init()
        if menuChoice == '3' : MenuRechercherUnFilmController(getBackToMenuPrincipal=self.init).init()
        if menuChoice == '4' : MenuGererLesCategoriesController(getBackToMenuPrincipal=self.init).init()
    

    


