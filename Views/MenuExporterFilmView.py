from os import system
from Classes.SubMenuView import SubMenuView


class MenuExporterFilm(SubMenuView):
    def printMenu(self):
        system("cls")
        system("clear")
        print("Menu Exportation Film \n\n")
