from os import system
from Classes.SubMenuView import SubMenuView


class MenuGererLesCategories(SubMenuView):
    def printMenu(self):
        system("cls")
        system("clear")
        print("Menu Gerer Les Categories \n\n")
