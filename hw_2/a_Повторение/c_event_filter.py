"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""
import time

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        self.prettyLabel = QtWidgets.QLabel(
            '<span style="color: red;">Pretty</span> <span style="color:blue;">button</span>'
        )
        self.prettyLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.prettyLabel.installEventFilter(self)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.prettyLabel)

        self.setLayout(layout)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        # print(watched)
        # print(event)

        if watched == self.prettyLabel and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            print(time.ctime(), "pretty button pressed")

        return super(Window, self).eventFilter(watched, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
