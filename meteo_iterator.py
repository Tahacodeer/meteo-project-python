from meteo_record import MeteoRecord
from exceptions import CorruptedDataError


class MeteoDataIterator:

    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        try:
            with open(self.filename, "r") as file:
                next(file)  # ignorer l'en-tête
                for line in file:
                    parts = line.strip().split(",")

                    if len(parts) != 4:
                        raise CorruptedDataError("Ligne incorrecte dans le fichier")

                    date = parts[0]
                    temperature = float(parts[1])
                    humidity = int(parts[2])
                    rainfall = int(parts[3])

                    # petite imperfection volontaire : pas de contrôle avancé ici
                    yield MeteoRecord(date, temperature, humidity, rainfall)

        except FileNotFoundError:
            raise CorruptedDataError("Fichier météo introuvable")
