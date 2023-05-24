"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""

from PySide6 import QtWidgets
from a_threads import WeatherHandler
from c_weatherapi_form import Ui_Form


# noinspection PyAttributeOutsideInit,PyPep8Naming
class weatherWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()
        self.initThreads()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """
        self.ui.lineEditLatitude.setText("59.938955")
        self.ui.lineEditLatitude.setEnabled(False)
        self.ui.lineEditLongitude.setText("30.315644")
        self.ui.lineEditLongitude.setEnabled(False)
        self.ui.lineEditDelay.setText("10")
        self.ui.labelDateTimeValue.setText("")
        self.ui.labelTemperatureValue.setText("")
        self.ui.labelWeatherCodeValue.setText("")
        self.ui.labelIsDayValue.setText("")
        self.ui.labelWindDirectionValue.setText("")
        self.ui.labelWindSpeedValue.setText("")

        self.ui.pushButtonStop.setEnabled(False)

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """
        self.weatherThread = WeatherHandler(lat=self.ui.lineEditLatitude.text(), lon=self.ui.lineEditLongitude.text())

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.weatherThread.weatherReceived.connect(self.updateWeather)
        self.ui.pushButtonChangeCoords.clicked.connect(self.onPushButtonChangeCoords)
        self.ui.pushButtonStop.clicked.connect(self.onPushButtonStop)
        self.weatherThread.finished.connect(self.weatherThreadFinished)
        self.ui.pushButtonStart.clicked.connect(self.handleWeatherThread)
        self.ui.lineEditDelay.textChanged.connect(self.onLineEditDelayTextChanged)

    def updateWeather(self, weather: dict) -> None:
        """
        Обновление данных в окне

        :param weather: Полученные данные от WeatherHandler
        :return: None
        """
        self.ui.labelDateTimeValue.setText(weather["time"])
        self.ui.labelTemperatureValue.setText(str(weather["temperature"]))
        self.ui.labelWeatherCodeValue.setText(str(weather["weathercode"]))
        self.ui.labelIsDayValue.setText(str(weather["is_day"]))
        self.ui.labelWindDirectionValue.setText(str(weather["winddirection"]))
        self.ui.labelWindSpeedValue.setText(str(weather["windspeed"]))

    def onPushButtonChangeCoords(self) -> None:
        """
        Обработка сигнала при нажатии на кнопку pushButtonChangeCoords

        :return: None
        """
        if self.ui.pushButtonChangeCoords.text() == "Change coordinates":
            self.ui.pushButtonStart.setEnabled(False)
            self.ui.lineEditLatitude.setEnabled(True)
            self.ui.lineEditLongitude.setEnabled(True)
            self.ui.pushButtonChangeCoords.setText("Save coordinates")
        else:
            self.ui.pushButtonStart.setEnabled(True)
            self.ui.lineEditLatitude.setEnabled(False)
            self.ui.lineEditLongitude.setEnabled(False)
            self.ui.pushButtonChangeCoords.setText("Change coordinates")
        self.weatherThread.lat = float(self.ui.lineEditLatitude.text())
        self.weatherThread.lon = float(self.ui.lineEditLongitude.text())
        self.weatherThread.api_url_update()

    def onPushButtonStop(self) -> None:
        """
        Обработка сигнала при нажатии на кнопку pushButtonStop

        :return: None
        """
        self.weatherThread.finished.emit()

    def onLineEditDelayTextChanged(self) -> None:
        """
        Обработка сигнала при изменении значения в lineEditDelayTextChanged

        :return: None
        """
        try:
            self.weatherThread.delay = int(self.ui.lineEditDelay.text())
        except ValueError:
            self.ui.lineEditDelay.setText(f"{self.weatherThread.delay}")

    def weatherThreadFinished(self) -> None:
        """
        Обработка завершения потока

        :return: None
        """
        self.ui.pushButtonStop.setEnabled(False)
        self.ui.pushButtonStart.setEnabled(True)
        self.ui.pushButtonChangeCoords.setEnabled(True)
        self.ui.lineEditDelay.setEnabled(True)
        # self.weatherThread.delay = 1

    def handleWeatherThread(self) -> None:
        """
        Управление потоком

        :return: None
        """
        self.ui.pushButtonStop.setEnabled(True)
        self.ui.pushButtonStart.setEnabled(False)
        self.ui.pushButtonChangeCoords.setEnabled(False)
        self.weatherThread.start()
        # if self.weatherThread.status or not self.weatherThread.isRunning():
        #     self.weatherThread.start()
        # else:
        #     self.weatherThread.status = False


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = weatherWindow()
    window.show()

    app.exec()
