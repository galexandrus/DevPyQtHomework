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

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """
        self.weatherThread = WeatherHandler()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = weatherWindow()
    window.show()

    app.exec()
