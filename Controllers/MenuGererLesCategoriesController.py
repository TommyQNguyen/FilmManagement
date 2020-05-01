from Views.MenuGererLesCategoriesView import MenuGererLesCategories

class MenuGererLesCategoriesController:
    def __init__(self, getBackToMenuPrincipal):
        self.view = MenuGererLesCategories()
        self.getBackToMenuPrincipal = getBackToMenuPrincipal

    def init(self):
        self.view.printMenu()
        returnMenuPrincipalUserInput = self.view.getUserInput()
        self.getBackToMenuPrincipal()
