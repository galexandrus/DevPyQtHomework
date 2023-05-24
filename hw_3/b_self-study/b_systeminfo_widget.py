"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. DONE поле для ввода времени задержки
2. DONE поле для вывода информации о загрузке CPU
3. DONE поле для вывода информации о загрузке RAM
4. DONE поток необходимо запускать сразу при старте приложения
5. DONE установку времени задержки сделать "горячей", т.е. поток должен сразу реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets, QtGui
from a_threads import SystemInfo
from b_systemInfo_form import Ui_Form


# noinspection PyAttributeOutsideInit,PyPep8Naming
class systemInfoWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()
        self.initThreads()
        self.initSignals()

        self.systemInfoThread.start()  # запуск отдельного потока при старте приложения

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """
        self.ui.lineEditTimeDelay.setText("1")
        self.ui.labelCpuUsageValue.setText("")
        self.ui.labelRamUsageValue.setText("")

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """
        self.systemInfoThread = SystemInfo()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.systemInfoThread.systemInfoReceived.connect(self.systemInfoShow)
        self.ui.lineEditTimeDelay.textChanged.connect(self.onLineEditTimeDelayTextChanged)

    def systemInfoShow(self, values: list) -> None:
        """
        Приём данных из отдельного потока и обработка этих данных в основном потоке приложения.

        :return: None
        """
        self.ui.labelCpuUsageValue.setText(f"{values[0]}")
        self.ui.labelRamUsageValue.setText(f"{values[1]}")

    def onLineEditTimeDelayTextChanged(self) -> None:
        """
        Обработка сигнала textChanged для объекта lineEditTimeDelay

        :return: None
        """
        try:
            new_delay = int(self.ui.lineEditTimeDelay.text())
            if new_delay > 0:
                self.systemInfoThread.delay = new_delay
            else:
                self.ui.lineEditTimeDelay.setText("1")
        except ValueError:
            self.ui.lineEditTimeDelay.setText("1")

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Обработка события "Закрытие окна"

        :param event: QtGui.QCloseEvent
        :return: None
        """
        self.systemInfoThread.quit()
        self.systemInfoThread.terminate()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = systemInfoWindow()
    window.show()

    app.exec()

