from os import system
from Classes.SubMenuView import SubMenuView


class MenuCreationFilm(SubMenuView):
    def printAndSendForm(self):
        print("Nom:")
        nom = self.getUserInput()
        print("\n Categorie:")
        categorie = self.getUserInput()
        print("\n Annee:")
        annee = self.getUserInput()
        print("\n Realisateur:")
        realisateur = self.getUserInput()
        print("\n Acteurs(separer par trait d'union)")
        acteurs = self.getUserInput()
        print("\n Note (1-10))")
        note = self.getUserInput()
        print("\n Commentaire (sans virgule)")
        commentaire = self.getUserInput()
        return {
            "nom": nom,
            "categorie": categorie,
            "annee": annee,
            "realisateur": realisateur,
            "acteurs": acteurs,
            "note": note,
            "commentaire": commentaire,
        }

    def printMenu(self):
        system("cls")
        system("clear")
        print("Menu Creation Film \n\n")
