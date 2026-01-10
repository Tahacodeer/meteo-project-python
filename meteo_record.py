<<<<<<< HEAD


    
=======
class Meteo_record:
    def __init__(self,date,temperature,humidity,rainfall):
        self.__date=date
        self.__temperature=temperature
        self.__humidity=humidity
        self.__rainfall=rainfall
    @property
    def date:
        return self.__date
    @property
    def temperature:
        return self.__temperature
    @property
    def rainfall:
        return self.__rainfall
    def __repr__(self):
        return f"la date est : {self.__date!r}  la temperature est : {self.temperature!r}  la humidity est :{self.humidity!r}  la rainfall est : {self.rainfall!r}"
    def __self__(self):
        return f"la date est : {self.__dater} \n la temperature est : {self.temperature} \n la humidity est :{self.humidity} \n la rainfall est : {self.rainfall}"
"
    
>>>>>>> eeb41b4 (created class Meteo_record)
