from Classes.DataSource import DataSource
from Models.CategorieModel import CategorieModel
import uuid


class FilmModel(DataSource):
    def __init__(self):
        self.fichierCSV = "films.csv"
        self.fields = [
            "nom",
            "categorie",
            "annee",
            "realisateur",
            "acteurs",
            "note",
            "commentaire",
        ]

    def getFilms(self):
        films = self.read(self.fichierCSV)
        # ici on modifie la liste de dictionaire
        # on va chercher la categorie par le model des categories
        # ensuite on utilise la fonction map (modifier un dictionnaire en iterant sur ces proprietes)
        # la fonction de notre map utilise un lambda et spread operator pour modifier le id en nom de categorie
        filmsWithCategories = list(
            map(
                lambda x: {
                    **x,
                    "categorie": CategorieModel().getCategoriebyId(x["categorie"])[
                        "nom"
                    ],
                },
                films,
            )
        )
        return filmsWithCategories

    def getFilmListByName(self, filmName):
        films = self.read(self.fichierCSV)
        # loop a travers les films
        # regarde si il trouve la string filmName dans le nom du film
        # si on trouve la string, on garde le film dans le nouvel array
        filteredFilm = list(
            filter(lambda x: x["nom"].lower().find(filmName.lower()) > -1, films)
        )
        return filteredFilm

    def createFilm(self, newFilmData):
        films = self.getFilms()
        films.append(newFilmData)
        self.write(fileName=self.fichierCSV, fields=self.fields, values=films)

    # chaque argument definie si on veut exporte le champp
    # on creer conditionellement un array de champ pour le header du csv
    # on map ensuite avec un lambda chaque proprieter pour creer un dictionnaire
    # chaque proprieter est seulement ajouter si l'argument d'export est True
    # l'export va sauvegarder le csv avec un nom unique ensuite
    def exportFilmList(
        self,
        nom=False,
        categorie=False,
        annee=False,
        realisateur=False,
        acteurs=False,
        note=False,
        commentaire=False,
    ):
        films = self.getFilms()
        fields = []
        if nom != False:
            fields.append("nom")
        if categorie != False:
            fields.append("categorie")
        if annee != False:
            fields.append("annee")
        if realisateur != False:
            fields.append("realisateur")
        if acteurs != False:
            fields.append("acteurs")
        if note != False:
            fields.append("note")
        if commentaire != False:
            fields.append("commentaire")

        exportedFilms = list(
            map(
                lambda x: {
                    **({"nom": x["nom"]} if nom is not False else {}),
                    **({"categorie": x["categorie"]} if categorie is not False else {}),
                    **({"annee": x["annee"]} if annee is not False else {}),
                    **(
                        {"realisateur": x["realisateur"]}
                        if realisateur is not False
                        else {}
                    ),
                    **({"acteurs": x["acteurs"]} if acteurs is not False else {}),
                    **({"note": x["note"]} if note is not False else {}),
                    **(
                        {"commentaire": x["commentaire"]}
                        if commentaire is not False
                        else {}
                    ),
                },
                films,
            )
        )
        self.write(
            fileName="export-" + str(uuid.uuid1()) + ".csv",
            fields=fields,
            values=exportedFilms,
        )
