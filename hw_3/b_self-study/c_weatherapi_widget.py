"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. DONE поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. DONE поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. DONE поле для вывода информации о погоде в указанных координатах
4. DONE поток необходимо запускать и останавливать при нажатии на кнопку
"""

from PySide6 import QtWidgets, QtGui
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
        self.ui.lineEditLatitude.setText("")
        self.ui.lineEditLatitude.setEnabled(False)
        self.ui.lineEditLongitude.setText("")
        self.ui.lineEditLongitude.setEnabled(False)
        self.ui.lineEditDelay.setText("10")
        self.ui.labelDateTimeValue.setText("")
        self.ui.labelTemperatureValue.setText("")
        self.ui.labelWeatherCodeValue.setText("")
        self.ui.labelIsDayValue.setText("")
        self.ui.labelWindDirectionValue.setText("")
        self.ui.labelWindSpeedValue.setText("")

        self.ui.pushButtonStop.setEnabled(False)

        self.ui.lineEditLatitude.setPlaceholderText("-90 < lat < 90")
        self.ui.lineEditLongitude.setPlaceholderText("-180 < lon < 180")

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """
        # self.checkLatLon()
        latitude = self.ui.lineEditLatitude.text()
        longitude = self.ui.lineEditLongitude.text()
        self.weatherThread = WeatherHandler(lat=latitude, lon=longitude)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonChangeCoords.clicked.connect(self.onPushButtonChangeCoords)
        self.ui.pushButtonStop.clicked.connect(self.onPushButtonStop)
        self.ui.pushButtonStart.clicked.connect(self.handleWeatherThread)

        self.weatherThread.weatherReceived.connect(self.updateWeather)
        self.weatherThread.finished.connect(self.weatherThreadFinished)

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

            self.trySetLenLon()
            self.weatherThread.api_url_update()

            self.ui.pushButtonChangeCoords.setText("Change coordinates")

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
        self.weatherThread.quit()

    def trySetLenLon(self) -> None:
        try:
            self.weatherThread.lat = float(self.ui.lineEditLatitude.text())
        except ValueError:
            self.weatherThread.lat = self.weatherThread.lat_default
            self.ui.lineEditLatitude.setText(f"{self.weatherThread.lat}")
        try:
            self.weatherThread.lon = float(self.ui.lineEditLongitude.text())
        except ValueError:
            self.weatherThread.lon = self.weatherThread.lon_default
            self.ui.lineEditLongitude.setText(f"{self.weatherThread.lon}")

    def handleWeatherThread(self) -> None:
        """
        Управление потоком

        :return: None
        """
        self.trySetLenLon()
        self.weatherThread.api_url_update()

        self.ui.pushButtonStop.setEnabled(True)
        self.ui.pushButtonStart.setEnabled(False)
        self.ui.pushButtonChangeCoords.setEnabled(False)

        if not self.weatherThread.isRunning():
            self.weatherThread.start()
        if not self.weatherThread.isFinished():
            self.weatherThread.exec()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Обработка события "Закрытие окна"

        :param event: QtGui.QCloseEvent
        :return: None
        """
        self.weatherThread.quit()
        self.weatherThread.terminate()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = weatherWindow()
    window.show()

    app.exec()
