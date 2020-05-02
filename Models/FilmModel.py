from Classes.DataSource import DataSource


class FilmModel(DataSource):
    def __init__(self):
        self.fichierCSV = "films.csv"
        self.fields = ["nom", "categorie", "annee", "realisateur", "acteurs"]

    def getFilms(self):
        films = self.read(self.fichierCSV)
        return films

    def createFilm(self, newFilmData):
        films = self.getFilms()
        films.append(newFilmData)
        self.write(fileName=self.fichierCSV, fields=self.fields, values=films)
