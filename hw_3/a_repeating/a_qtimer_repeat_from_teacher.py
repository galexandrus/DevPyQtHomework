"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""
import time
import psutil

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

        self.initTimer()

        self.initSignals()

    def initUi(self) -> None:
        """

        :return:
        """

        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)
        self.checkBoxLogEnable = QtWidgets.QCheckBox("Записывать в файл")
        self.progressBar = QtWidgets.QProgressBar()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.plainTextEdit)
        layout.addWidget(self.progressBar)
        layout.addWidget(self.checkBoxLogEnable)

        self.setLayout(layout)

    def initTimer(self) -> None:
        """

        :return:
        """

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.start()

    def initSignals(self) -> None:
        """

        :return:
        """

        self.timer.timeout.connect(self.get_CPU_percent)

    def get_CPU_percent(self) -> None:
        """

        :return:
        """

        percent = psutil.cpu_percent()
        self.plainTextEdit.appendPlainText(f"{time.ctime()} >>> Загрузка CPU: {percent} %")
        self.progressBar.setValue(int(percent))

        if self.checkBoxLogEnable.isChecked():
            with open("cpu.log", "a") as f:
                f.write(f"{time.ctime()} >>> Загрузка CPU: {percent} %\n")




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
