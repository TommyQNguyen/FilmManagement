from os import system
from Classes.SubMenuView import SubMenuView


class MenuExporterFilm(SubMenuView):
    def printMenu(self):
        system("cls")
        system("clear")
        print("Menu Exportation Film \n\n")

    def printExportName(self):
        system("cls")
        system("clear")
        print("exporter nom? (y/n)")

    def printExportCategorie(self):
        system("cls")
        system("clear")
        print("exporter Categorie? (y/n)")

    def printExportAnnee(self):
        system("cls")
        system("clear")
        print("export Annee? (y/n)")

    def printExportRealisateur(self):
        system("cls")
        system("clear")
        print("export Realisateur? (y/n)")

    def printExportActeurs(self):
        system("cls")
        system("clear")
        print("export Acteurs? (y/n)")
