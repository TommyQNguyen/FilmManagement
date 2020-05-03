from os import system
from Classes.SubMenuView import SubMenuView


class MenuRechercherUnFilm(SubMenuView):
    def askForSearchInput(self):
        print("Entrer le nom du film a chercher: ")
        filmToSearch = self.getUserInput()
        return filmToSearch

    def printList(self, filmList):
        system("cls")
        system("clear")
        print(
            "{:<15} {:<15} {:<15} {:<15} {:<15}".format(
                "Nom", "Categorie", "Annee", "Realisateur", "Acteurs"
            )
        )
        print(
            "==================================================================================================="
        )
        for film in filmList:
            print(
                "{:<15} {:<15} {:<15} {:<15} {:<15}".format(
                    film["nom"],
                    film["categorie"],
                    film["annee"],
                    film["realisateur"],
                    film["acteurs"],
                )
            )

    def printMenu(self):
        system("cls")
        system("clear")
        print("Menu Rechercher Un Film\n\n")
