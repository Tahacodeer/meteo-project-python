class MeteoRecord:
    def __init__(self, date, temperature, humidity, rainfall):
        self.__date = date
        self.__temperature = temperature
        self.__humidity = humidity
        self.__rainfall = rainfall

    @property
    def date(self):
        return self.__date

    @property
    def temperature(self):
        return self.__temperature

    @property
    def humidity(self):
        return self.__humidity

    @property
    def rainfall(self):
        return self.__rainfall

    def __repr__(self):
        return (
            f"MeteoRecord(date={self.__date!r}, "
            f"temperature={self.__temperature!r}, "
            f"humidity={self.__humidity!r}, "
            f"rainfall={self.__rainfall!r})"
        )

    def __str__(self):
        return (
            f"La date est : {self.__date}\n"
            f"La température est : {self.__temperature}\n"
            f"L'humidité est : {self.__humidity}\n"
            f"La pluie est : {self.__rainfall}"
        )
