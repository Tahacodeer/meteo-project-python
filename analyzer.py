from functools import reduce


class MeteoAnalyzer:

    def __init__(self, records):
        # choix simple pour faciliter l'analyse
        self.records = list(records)

    def count_days(self):
        return len(self.records)

    def heat_anomalies(self):
        # seuil fixé arbitrairement
        return list(filter(lambda r: r.temperature > 35, self.records))

    def rain_anomalies(self):
        return list(filter(lambda r: r.rainfall > 40, self.records))

    def average_temperature(self):
        temperatures = list(map(lambda r: r.temperature, self.records))

        if len(temperatures) == 0:
            return 0  # sécurité basique

        total = reduce(lambda a, b: a + b, temperatures)
        return total / len(temperatures)
