from os import system
from Classes.SubMenuView import SubMenuView

class MenuAfficherFilms(SubMenuView): # class MenuAfficherFilms extends SubMenuView
  def printMenu(self):
    system('cls') 
    system('clear')
    print("Menu Afficher Films \n\n")
