import csv
import json

class Importation:
    """Importe une table csv"""
    def __init__(self, folder: str, filename: str):
        self.folder = folder
        self.filename = filename

    def import_csv(self, folder: str, filename: str) -> None:
        data =[]
        with open(folder + filename, encoding='ISO-8859-1') as csvfile :
            covidreader = csv.reader(csvfile, delimiter=';') 
            for row in covidreader :
                data.append(row)

    def import_json(self, folder: str, filename: str) -> None:
        with open(folder + filename) as json_file:
            data = json.load(json_file)