from Views.MenuGererLesCategoriesView import MenuGererLesCategories
from Models.CategorieModel import CategorieModel


class MenuGererLesCategoriesController:
    def __init__(self, getBackToMenuPrincipal):
        self.view = MenuGererLesCategories()
        self.getBackToMenuPrincipal = getBackToMenuPrincipal

    def getAndCreateCategorie(self):
        self.view.printCreateCategorie()
        nomCategorie = self.view.getUserInput()
        CategorieModel().createCategorie(newCategorieData=nomCategorie)

    def getAndDeleteCategorie(self):
        self.view.printSuprimerCategorie()
        idCategorie = self.view.getUserInput()
        CategorieModel().deleteCategorie(categorieId=idCategorie)

    def init(self):
        self.view.printMenu()
        categories = CategorieModel().getCategories()
        self.view.printList(categorieList=categories)
        self.view.printOptions()
        option = self.view.getUserInput()
        if option == "1":
            self.getAndCreateCategorie()
        if option == "2":
            self.getAndDeleteCategorie()
        returnMenuPrincipalUserInput = self.view.getUserInput()
        self.getBackToMenuPrincipal()
