"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. DONE Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. DONE Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. DONE Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. DONE Сохранять значение выбранного в comboBox режима отображения
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

        combo_box_save = QtCore.QSettings("combo_box_save")
        print(combo_box_save.value("text", "dec"))
        dial_save = QtCore.QSettings("dial_save")
        print(dial_save.value("text", "0"))

        self.min_value = -15
        self.max_value = 15

        self.ui.horizontalSlider.setMinimum(self.min_value)
        self.ui.horizontalSlider.setMaximum(self.max_value)

        self.ui.dial.setMinimum(self.min_value)
        self.ui.dial.setMaximum(self.max_value)

        self.ui.comboBox.addItems(["dec", "oct", "hex", "bin"])

        self.ui.lcdNumber.setDigitCount(7)

        self.ui.comboBox.setCurrentText(combo_box_save.value("text", "dec"))
        self.ui.dial.setSliderPosition(int(str(dial_save.value("text", "0"))))
        self.ui.horizontalSlider.setSliderPosition(int(str(dial_save.value("text", "0"))))
        self.ui.lcdNumber.display(self.base_converter(self.ui.dial.value()))

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.ui.horizontalSlider.sliderMoved.connect(self.onHorizontalSliderMoved)
        self.ui.dial.sliderMoved.connect(self.onDialMoved)
        self.ui.dial.valueChanged.connect(self.onDialMoved)
        self.ui.comboBox.currentTextChanged.connect(self.onComboBoxCurrentTextChanged)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Обработка нажатия на клавиши клавиатуры

        :param event: QtGui.QKeyEvent
        :return: None
        """

        if event.text() == "+":
            self.ui.dial.setSliderPosition(self.ui.dial.sliderPosition() + 1)
            print(self.ui.dial.sliderPosition())
        if event.text() == "-":
            self.ui.dial.setSliderPosition(self.ui.dial.sliderPosition() - 1)
            print(self.ui.dial.sliderPosition())

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
        self.ui.dial.setSliderPosition(self.ui.horizontalSlider.value())
        self.ui.lcdNumber.display(self.base_converter(self.ui.horizontalSlider.value()))

    def onDialMoved(self) -> None:
        """
        Обработка сигнала move для объекта dial

        :return: None
        """
        self.ui.horizontalSlider.setSliderPosition(self.ui.dial.value())
        self.ui.lcdNumber.display(self.base_converter(self.ui.dial.value()))

    def onComboBoxCurrentTextChanged(self) -> None:
        """
        Преобразование значения в lcdNumber при выборе другой системы счисления в comboBox
        :return: None
        """
        self.ui.lcdNumber.display(self.base_converter(self.ui.horizontalSlider.value()))

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Обработка события "Закрытие окна"

        :param event: QtGui.QCloseEvent
        :return: None
        """
        combo_box_save = QtCore.QSettings("combo_box_save")
        combo_box_save.setValue("text", self.ui.comboBox.currentText())

        dial_save = QtCore.QSettings("dial_save")
        dial_save.setValue("text", str(self.ui.dial.value()))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
