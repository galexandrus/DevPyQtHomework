"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль.
При выводе события указывать время, когда произошло событие.
"""
import time

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def event(self, event: QtCore.QEvent) -> bool:
        # print(event)
        if QtCore.QEvent.Type.Move == event.type():
            print(time.ctime(), event.type())
            print(event)

        return super(Window, self).event(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
