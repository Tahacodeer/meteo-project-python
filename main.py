
from meteo_iterator import MeteoDataIterator
from analyzer import MeteoAnalyzer


def main():
    iterator = MeteoDataIterator("meteo_data.csv")
    analyzer = MeteoAnalyzer(iterator)

    print("---- Analyse des données météo-----")
    print("Nombre total de jours analysés :", analyzer.count_days())
    print("Jours de chaleur extrême :", len(analyzer.heat_anomalies()))
    print("Jours de fortes pluies :", len(analyzer.rain_anomalies()))
    print("Température moyenne :", round(analyzer.average_temperature(), 2), "°C")


if __name__ == "__main__":
    main()
