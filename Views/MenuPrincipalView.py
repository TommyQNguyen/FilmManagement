from os import system

# todo inherit from submenuview, rename submenu to menu
class MenuPrincipal:
  def printMenu(self):
    system('cls') 
    print("Menu Principal \n\n")
    print("1) Creer film")
    print("2) Afficher les films")
    print("3) Rechercher un film")
    print("4) Gerer les categories")
    print()                         # Sauter une ligne
    print("Entrez votre choix")

  def getUserInput(self):
    return input()  
