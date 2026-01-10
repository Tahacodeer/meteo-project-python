import os
from meteo_record import MeteoRecord
from exceptions import CorruptedDataError


class MeteoDataIterator:

    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        try:
            
            BD = os.path.dirname(__file__)
            file_path = os.path.join(BD, self.filename)

            with open(file_path, "r") as file:
                next(file)  # ignorer l'en-tête
                for line in file:
                    parts = line.strip().split(",")

                    if len(parts) != 4:
                        raise CorruptedDataError("Ligne incorrecte dans le fichier")

                    date = parts[0]
                    temperature = float(parts[1])
                    humidity = int(parts[2])
                    rainfall = int(parts[3])

                    yield MeteoRecord(date, temperature, humidity, rainfall)

        except FileNotFoundError:
            raise CorruptedDataError("Fichier météo introuvable")
