"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        settings = QtCore.QSettings("SaveApp")
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setPlainText(settings.value("text", ""))

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.plainTextEdit)

        self.setLayout(layout)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        settings = QtCore.QSettings("SaveApp")
        settings.setValue("text", self.plainTextEdit.toPlainText())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

