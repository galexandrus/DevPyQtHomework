"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. DONE Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    DONE * Кол-во экранов
    DONE * Текущее основное окно
    DONE * Разрешение экрана
    DONE * На каком экране окно находится
    DONE * Размеры окна
    DONE * Минимальные размеры окна
    DONE * Текущее положение (координаты) окна
    DONE * Координаты центра приложения
    DONE * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time

from PySide6 import QtWidgets, QtCore
from c_signals_events_form import Ui_Form


# noinspection PyAttributeOutsideInit,PyPep8Naming
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация UI

        :return: None
        """
        pass

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoords)
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetData)
        self.ui.pushButtonLT.clicked.connect(self.onPushButtonLT)
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonLB)

    def onPushButtonMoveCoords(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonMoveCoords

        :return: None
        """
        self.ui.plainTextEdit.setPlainText(f"старая позиция: {self.window().x()}, {self.window().y()}")
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())
        self.ui.plainTextEdit.appendPlainText(f"новая позиция: {self.window().x()}, {self.window().y()}")

    def onPushButtonLT(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLT

        :return: None
        """
        self.ui.plainTextEdit.setPlainText(f"старая позиция: {self.window().x()}, {self.window().y()}")
        self.move(0, 0)
        self.ui.plainTextEdit.appendPlainText(f"новая позиция: {self.window().x()}, {self.window().y()}")

    def onPushButtonLB(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLB

        :return: None
        """
        self.ui.plainTextEdit.setPlainText(f"старая позиция: {self.window().x()}, {self.window().y()}")
        self.move(0, self.screen().geometry().height() - self.window().size().height() - 70)
        self.ui.plainTextEdit.appendPlainText(f"новая позиция: {self.window().x()}, {self.window().y()}")

    def onPushButtonGetData(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonGetData

        :return: None
        """
        window_states = []
        if self.window().isEnabled():
            window_states.append("Enabled")
        if self.window().isHidden():
            window_states.append("Hidden")
        if self.window().isActiveWindow():
            window_states.append("Active")
        if self.window().isVisible():
            window_states.append("Visible")
        if self.window().isFullScreen():
            window_states.append("Full screen")
        window_state = ", ".join(window_states)

        self.ui.plainTextEdit.setPlainText(f"{time.ctime()}\n"
                                           f"количество экранов: "
                                           f"{len(QtWidgets.QApplication.screens())}\n"
                                           f"текущее основное окно: "
                                           f"{self.window().objectName()}\n"
                                           f"разрешение экрана: "
                                           f"{self.screen().geometry().width()}, "
                                           f"{self.screen().geometry().height()}\n"
                                           f"на каком экране находится окно: "
                                           f"{self.window().screen().name()}\n"
                                           f"размеры окна: "
                                           f"{self.window().size().width()}, "
                                           f"{self.window().size().height()}\n"
                                           f"минимальные размеры окна: "
                                           f"{self.window().minimumSize().width()}, "
                                           f"{self.window().minimumSize().height()}\n"
                                           f"текущие координаты окна: "
                                           f"{self.window().x()}, {self.window().y()}\n"
                                           f"координаты центра приложения: "
                                           f"{self.window().x() + self.window().size().width() // 2}, "
                                           f"{self.window().y() + self.window().size().height() // 2}\n"
                                           f"состояние окна: {window_state}\n")
                                           # f"высота панели задач: {self.screen().findChild('bar', )}")

    # def onWindowMove(self, move_func) -> None:
    #     """
    #     Декоратор при перемещении окна
    #
    #     :return: None
    #     """
    #     def wrapper(*args, **kwargs) -> None:
    #         self.ui.plainTextEdit.setPlainText(f"старая позиция: {self.window().x()}, {self.window().y()}")
    #         move_func()
    #         self.ui.plainTextEdit.appendPlainText(f"новая позиция: {self.window().x()}, {self.window().y()}")
    #
    #     return wrapper


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
