from PySide6 import QtWidgets, QtCore


class MyFirstWindow(QtWidgets.QWidget):
    """
    My first window class
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui
        :return:
        """

        self.setWindowTitle("My first window")

        # self.resize(800, 600)
        size = QtCore.QSize(400, 300)
        self.resize(size)

        current_size = self.size()
        print(current_size)

    def initSignals(self) -> None:
        pass

    def initChilds(self) -> None:
        pass

    def initDB(self) -> None:  # Инициализация базы данных, либо в теле функции, либо как результат выполнения функции
        # self.db
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win1 = MyFirstWindow()
    # win2 = MyFirstWindow()
    win1.show()
    # win2.show()

    app.exec()
