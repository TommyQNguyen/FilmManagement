from os import system
from Classes.SubMenuView import SubMenuView


class MenuRechercherUnFilm(SubMenuView):
    def printMenu(self):
        system("cls")
        system("clear")
        print("Menu Rechercher Un Film\n\n")
