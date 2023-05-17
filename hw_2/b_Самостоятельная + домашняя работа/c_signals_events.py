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
    DONE * При перемещении окна выводить его старую и новую позицию
    DONE * При изменении размера окна выводить его новый размер
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

        self.task_bar_height = 70

    def initUi(self) -> None:
        """
        Доинициализация UI

        :return: None
        """
        self.ui.pushButtonMoveCoords.installEventFilter(self)
        self.ui.pushButtonLT.installEventFilter(self)
        self.ui.pushButtonLB.installEventFilter(self)
        self.ui.pushButtonRT.installEventFilter(self)
        self.ui.pushButtonRB.installEventFilter(self)
        self.ui.pushButtonCenter.installEventFilter(self)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoords)
        self.ui.pushButtonLT.clicked.connect(self.onPushButtonLT)
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonLB)
        self.ui.pushButtonRT.clicked.connect(self.onPushButtonRT)
        self.ui.pushButtonRB.clicked.connect(self.onPushButtonRB)
        self.ui.pushButtonCenter.clicked.connect(self.onPushButtonCenter)
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetData)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """
        Фильтр для обработки событий MouseButtonPress.

        :param watched: Объект, за которым ведётся наблюдение.
        :param event: Текущее событие.
        :return: bool
        """

        buttons = (self.ui.pushButtonMoveCoords,
                   self.ui.pushButtonLT,
                   self.ui.pushButtonLB,
                   self.ui.pushButtonRT,
                   self.ui.pushButtonRB,
                   self.ui.pushButtonCenter)

        if watched in buttons and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.setPlainText(f"{time.strftime('%H:%M:%S', time.localtime())} "
                                               f"старая позиция: {self.window().x()}, {self.window().y()}")

        return super(Window, self).eventFilter(watched, event)

    def event(self, event: QtCore.QEvent) -> bool:
        """
        Обработка событий QtCore.QEvent.Type.Move

        :param event: Текущее событие.
        :return: bool
        """
        if event.type() == QtCore.QEvent.Type.Move:
            self.ui.plainTextEdit.appendPlainText(f"{time.strftime('%H:%M:%S', time.localtime())} "
                                                  f"новая позиция: {self.window().x()}, {self.window().y()}")

        return super(Window, self).event(event)

    def onPushButtonMoveCoords(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonMoveCoords

        :return: None
        """
        self.window().move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

    def onPushButtonLT(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLT

        :return: None
        """
        self.window().move(0, 0)

    def onPushButtonLB(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLB

        :return: None
        """
        self.window().move(0, self.screen().geometry().height() - self.window().size().height() - self.task_bar_height)

    def onPushButtonRT(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonRT

        :return: None
        """
        self.window().move(self.window().screen().geometry().width() - self.window().geometry().width(), 0)

    def onPushButtonRB(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonRB

        :return: None
        """
        self.window().move(self.window().screen().geometry().width() - self.window().geometry().width(),
                           self.window().screen().geometry().height() - self.window().geometry().height() -
                           self.task_bar_height)

    def onPushButtonCenter(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonCenter

        :return: None
        """
        self.window().move((self.window().screen().geometry().width() - self.window().geometry().width()) // 2,
                           (self.window().screen().geometry().height() - self.window().geometry().height() -
                            self.task_bar_height) // 2)

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
                                           f"{self.window().screen().geometry().width()}, "
                                           f"{self.window().screen().geometry().height()}\n"
                                           f"на каком экране находится окно: "
                                           f"{self.window().screen().name()}\n"
                                           f"размеры окна: "
                                           f"{self.window().geometry().width()}, "
                                           f"{self.window().geometry().height()}\n"
                                           f"минимальные размеры окна: "
                                           f"{self.window().minimumSize().width()}, "
                                           f"{self.window().minimumSize().height()}\n"
                                           f"текущие координаты окна: "
                                           f"{self.window().x()}, {self.window().y()}\n"
                                           f"координаты центра приложения: "
                                           f"{self.window().x() + self.window().geometry().width() // 2}, "
                                           f"{self.window().y() + self.window().geometry().height() // 2}\n"
                                           f"состояние окна: {window_state}\n")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
