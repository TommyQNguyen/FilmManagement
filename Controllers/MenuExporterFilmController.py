from Views.MenuExporterFilmView import MenuExporterFilm
from Models.FilmModel import FilmModel


class MenuExporterFilmController:
    def __init__(self, getBackToMenuPrincipal):
        self.view = MenuExporterFilm()
        self.getBackToMenuPrincipal = getBackToMenuPrincipal

    def init(self):
        self.view.printMenu()

        # demander si exporter le nom
        self.view.printExportName()
        nom = True if self.view.getUserInput() == "y" else False

        #  demander si exporter categorie
        self.view.printExportCategorie()
        categorie = True if self.view.getUserInput() == "y" else False

        # demander si exporter annee
        self.view.printExportAnnee()
        annee = True if self.view.getUserInput() == "y" else False

        # demander si exporter realisateur
        self.view.printExportRealisateur()
        realisateur = True if self.view.getUserInput() == "y" else False

        # demander si exporter acteurs
        self.view.printExportActeurs()
        acteurs = True if self.view.getUserInput() == "y" else False

        # envoyer commande d'export au model
        FilmModel().exportFilmList(
            nom=nom,
            categorie=categorie,
            annee=annee,
            realisateur=realisateur,
            acteurs=acteurs,
        )

        returnMenuPrincipalUserInput = self.view.getUserInput()
        self.getBackToMenuPrincipal()
