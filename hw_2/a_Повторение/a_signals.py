"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()

        self.pushButtonMirror = QtWidgets.QPushButton()
        self.pushButtonMirror.setText("Mirror")

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEditInput)
        layoutLineEdit.addWidget(self.lineEditMirror)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addWidget(self.pushButtonMirror)

        self.setLayout(layoutMain)

    def initSignals(self) -> None:
        self.pushButtonMirror.clicked.connect(self.mirrorText)

    def mirrorText(self) -> None:
        source_text = self.lineEditInput.text()
        self.lineEditMirror.setText(source_text[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
