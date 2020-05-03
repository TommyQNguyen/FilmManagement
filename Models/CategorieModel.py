from Classes.DataSource import DataSource


class CategorieModel(DataSource):
    def __init__(self):
        self.fichierCSV = "categories.csv"
        self.fields = ["id", "nom"]

    def getCategories(self):
        categories = self.read(self.fichierCSV)
        return categories

    def getCategoriebyId(self, categorieId):
        categories = self.getCategories()
        categorieById = list(filter(lambda x: x["id"] == categorieId, categories))[0]
        return categorieById

    def deleteCategorie(self, categorieId):
        categories = self.getCategories()
        categoriesAfterDelete = list(
            filter(lambda x: x["id"] != categorieId, categories)
        )
        print(categoriesAfterDelete)
        self.write(
            fileName=self.fichierCSV, fields=self.fields, values=categoriesAfterDelete
        )

    def createCategorie(self, newCategorieData):
        categories = self.getCategories()
        categories.append(
            {"id": str(int(categories[-1]["id"]) + 1), "nom": newCategorieData}
        )
        self.write(fileName=self.fichierCSV, fields=self.fields, values=categories)
