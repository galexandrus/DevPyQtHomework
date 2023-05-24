"""
Модуль в котором содержатся потоки Qt
"""

import time
import psutil
import requests
import json
from PySide6 import QtCore


# noinspection PyAttributeOutsideInit,PyPep8Naming
class SystemInfo(QtCore.QThread):
    # DONE Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения
    #  (в текущем случае list)
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        # DONE создайте атрибут класса self.delay = None, для управления задержкой получения данных
        self.delay = None

    def run(self) -> None:  # DONE переопределить метод run
        if self.delay is None:  # DONE Если задержка не передана в поток перед его запуском
            self.delay = 1  # DONE то устанавливайте значение 1

        while True:  # DONE Запустите бесконечный цикл получения информации о системе
            # DONE с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            cpu_value = psutil.cpu_percent()
            # DONE с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            ram_value = psutil.virtual_memory().percent
            # DONE с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            self.systemInfoReceived.emit([cpu_value, ram_value])
            # DONE с помощью функции .sleep() приостановите выполнение цикла на время self.delay
            time.sleep(self.delay)


# noinspection PyAttributeOutsideInit,PyPep8Naming
class WeatherHandler(QtCore.QThread):
    # DONE Пропишите сигналы, которые считаете нужными
    weatherReceived = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__lat_default = 59.938955  # Saint-Petersburg latitude
        self.__lon_default = 30.315644  # Saint-Petersburg longitude
        self.__lat = lat
        self.__lon = lon
        self.__api_url = None
        self.api_url_update()
        self.__delay = 10
        self.__status = None

    @property
    def lat_default(self) -> float:
        return self.__lat_default

    @property
    def lon_default(self) -> float:
        return self.__lon_default

    @property
    def lat(self) -> float:
        return self.__lat

    @lat.setter
    def lat(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError
        self.__lat = value

    @property
    def lon(self) -> float:
        return self.__lon

    @lon.setter
    def lon(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError
        self.__lon = value

    @property
    def api_url(self) -> str:
        return self.__api_url

    def api_url_update(self) -> None:
        if self.lat is None or self.lon is None or self.lat == "" or self.lon == "":
            self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={self.lat_default}" \
                             f"&longitude={self.lon_default}&current_weather=true"
        else:
            self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={self.lat}" \
                             f"&longitude={self.lon}&current_weather=true"

    @property
    def delay(self) -> int:
        return self.__delay

    @delay.setter
    def delay(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError
        self.__delay = value

    @property
    def status(self) -> None:
        return self.__status

    @status.setter
    def status(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError
        self.__status = value

    def run(self) -> None:
        # DONE настройте метод для корректной работы

        self.status = True

        while self.__status:
            response = requests.get(self.__api_url)

            if response.status_code == 200:
                weather_dict = json.loads(response.text)["current_weather"]
                self.weatherReceived.emit(weather_dict)
                time.sleep(self.delay)
            else:
                self.status = False
                return


# if __name__ == '__main__':
#     lat = "59.938955"
#     lon = "30.315644"
#     url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
#     resp1 = requests.get(url)
#     # resp2 = requests.Request
#     print(resp1)
#     print(resp1.text)
#     print(type(resp1.text))
#
#     data_dict = json.loads(resp1.text)["current_weather"]

    # print(data_dict)
    # print(type(data_dict))
    # data_time = data_dict["time"]
    # print(data_time)
    # print(type(data_time))
    # data_temp = data_dict["temperature"]
    # print(data_temp)
    # print(type(data_temp))
    # data_code = data_dict["weathercode"]
    # print(data_code)
    # print(type(data_code))
    # data_isday = data_dict["is_day"]
    # print(data_isday)
    # print(type(data_isday))
    # data_direct = data_dict["winddirection"]
    # print(data_direct)
    # print(type(data_direct))
    # data_speed = data_dict["windspeed"]
    # print(data_speed)
    # print(type(data_speed))

    # print(json.loads(resp1.text))
    # print(type(json.loads(resp1.text)))
    # print(resp1.json())
    # print(type(resp1.json()))
    # print(resp1.json()["current_weather"])
    # print(json.loads(resp1.json()))

# self.ui.labelDateTimeValue.setText(weather["time"])
# self.ui.labelTemperatureValue.setText(weather["temperature"])
# self.ui.labelWeatherCodeValue.setText(weather["weathercode"])
# self.ui.labelIsDayValue.setText(weather["is_day"])
# self.ui.labelWindDirectionValue.setText(weather["winddirection"])
# self.ui.labelWindSpeedValue.setText(weather["windspeed"])
