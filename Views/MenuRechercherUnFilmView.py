from os import system
from Classes.SubMenuView import SubMenuView

class MenuRechercherUnFilm(SubMenuView):
  def printMenu(self):
    system('cls') 
    print("Menu Rechercher Un Film\n\n")

