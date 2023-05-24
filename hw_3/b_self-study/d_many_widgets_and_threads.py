"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""

from PySide6 import QtWidgets, QtGui
from b_systeminfo_widget import systemInfoWindow
from c_weatherapi_widget import weatherWindow


# noinspection PyAttributeOutsideInit,PyPep8Naming
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.systemInfo = systemInfoWindow()
        self.weather = weatherWindow()

        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """
        layoutUnited = QtWidgets.QVBoxLayout()
        layoutUnited.addWidget(self.systemInfo)
        layoutUnited.addWidget(self.weather)

        self.setLayout(layoutUnited)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Обработка события "Закрытие окна"

        :param event: QtGui.QCloseEvent
        :return: None
        """
        self.systemInfo.systemInfoThread.quit()
        self.systemInfo.systemInfoThread.terminate()

        self.weather.weatherThread.quit()
        self.weather.weatherThread.terminate()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
