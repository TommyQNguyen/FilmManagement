from os import system
from Classes.SubMenuView import SubMenuView


class MenuAfficherFilms(SubMenuView):  # class MenuAfficherFilms extends SubMenuView
    def printList(self, filmList):
        print(
            "{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
                "Nom",
                "Categorie",
                "Annee",
                "Realisateur",
                "Acteurs",
                "Note",
                "Commentaire",
            )
        )
        print(
            "==================================================================================================="
        )
        for film in filmList:
            print(
                "{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
                    film["nom"],
                    film["categorie"],
                    film["annee"],
                    film["realisateur"],
                    film["acteurs"],
                    film["note"],
                    film["commentaire"],
                )
            )

    def printMenu(self):
        system("cls")
        system("clear")
        print("Menu Afficher Films \n\n")
        # self.printList()
