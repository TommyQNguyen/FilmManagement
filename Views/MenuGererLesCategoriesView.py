from os import system
from Classes.SubMenuView import SubMenuView


class MenuGererLesCategories(SubMenuView):
    def printMenu(self):
        system("cls")
        system("clear")
        print("Menu Gerer Les Categories \n\n")

    def printCreateCategorie(self):
        system("cls")
        system("clear")
        print("Name:")

    def printSuprimerCategorie(self):
        system("cls")
        system("clear")
        print("Id a supprimer:")

    def printOptions(self):
        print()
        print("options")
        print()
        print("1) Ajouter une categorie")
        print("2) supprimer une categorie")

    def printList(self, categorieList):
        print("{:<15} {:<15}".format("Id", "Nom"))
        print("=======================================")
        for categorie in categorieList:
            print("{:<15} {:<15}".format(categorie["id"], categorie["nom"]))
