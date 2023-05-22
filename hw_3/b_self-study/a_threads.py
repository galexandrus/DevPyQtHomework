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
    # TODO Пропишите сигналы, которые считаете нужными
    weatherReceived = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self) -> None:
        # TODO настройте метод для корректной работы

        while True:
            response = requests.get(self.__api_url)
            data_dict = json.loads(response.json())
            self.weatherReceived.emit(data_dict["current_weather"])
            time.sleep(self.__delay)

        # while self.__status:
            # TODO Примерный код ниже
            """
            response = requests.get(self.__api_url)
            data = response.json()
            ваш_сигнал.emit(data)
            sleep(delay)
            """
