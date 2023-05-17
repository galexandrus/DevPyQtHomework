"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore, QtGui
from d_eventfilter_settings_form import Ui_Form


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

        self.min_value = -10
        self.max_value = 10

        self.ui.horizontalSlider.setMinimum(self.min_value)
        self.ui.horizontalSlider.setMaximum(self.max_value)

        self.ui.dial.setMinimum(self.min_value)
        self.ui.dial.setMaximum(self.max_value)

        self.ui.comboBox.addItems(["dec", "oct", "hex", "bin"])

        # self.ui.dial.installEventFilter(self)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.ui.horizontalSlider.sliderMoved.connect(self.onHorizontalSliderMoved)
        self.ui.dial.sliderMoved.connect(self.onDialMoved)
        self.ui.comboBox.currentTextChanged.connect(self.onComboBoxCurrentTextChanged)

    # def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
    #     """
    #
    #     :param watched:
    #     :param event:
    #     :return:
    #     """
    #     # widgets = (self.ui.lcdNumber, self.ui.horizontalSlider, self.ui.dial)
    #
    #     # if watched in widgets and self.ui.lcdNumber
    #     pass

    # def event(self, event: QtCore.QEvent) -> bool:
    #     """
    #
    #     :param event:
    #     :return:
    #     """
    #     # self.ui.dial
    #     # if event.type() == QtCore.QEvent.Type(6):
    #     pass

    def base_converter(self, num: int) -> str:
        """
        Преобразование значения для отображения на lcdNumber

        :param num: Текущее значение horizontalSlider или dial
        :return: str
        """

        if self.ui.comboBox.currentText() == "dec":
            return str(num)
        elif self.ui.comboBox.currentText() == "oct":
            return oct(num)
        elif self.ui.comboBox.currentText() == "hex":
            return hex(num)
        else:
            return bin(num)

    def onHorizontalSliderMoved(self) -> None:
        """
        Обработка сигнала move для объекта horizontalSlider

        :return: None
        """
        self.ui.lcdNumber.display(self.base_converter(self.ui.horizontalSlider.value()))
        self.ui.dial.setSliderPosition(self.ui.horizontalSlider.value())

    def onDialMoved(self) -> None:
        """
        Обработка сигнала move для объекта dial

        :return: None
        """
        self.ui.lcdNumber.display(self.base_converter(self.ui.dial.value()))
        self.ui.horizontalSlider.setSliderPosition(self.ui.dial.value())

    def onComboBoxCurrentTextChanged(self) -> None:
        """
        Преобразование значения в lcdNumber при выборе другой системы счисления в comboBox
        :return: None
        """
        self.ui.lcdNumber.display(self.base_converter(self.ui.horizontalSlider.value()))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
