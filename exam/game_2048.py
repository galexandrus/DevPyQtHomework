from PySide6 import QtWidgets, QtCore, QtGui
from game_2048_form import Ui_Form
from logic import Game2048


# noinspection PyAttributeOutsideInit,PyPep8Naming
class Window(QtWidgets.QWidget):
    signCaught = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.current_sign = None

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.game = Game2048()

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация интерфейса

        :return: None
        """
        topScoreInMemory = QtCore.QSettings("game_2048_top_score")
        restoredScoreStr = str(topScoreInMemory.value("text", ""))
        if restoredScoreStr:
            restoredScoreList = [int(str_val) for str_val in restoredScoreStr.split(" ")]
            self.game.top_score = restoredScoreList

        self.colours = {
            0: "background-color: #bcb9c2;",
            2: "background-color: #fffee5;",
            4: "background-color: #dcd37b;",
            8: "background-color: #ffd035;",
            16: "background-color: #cc9245;",
            32: "background-color: #a15c3e;",
            64: "background-color: #81588d;",
            128: "background-color: #c24998;",
            256: "background-color: #a42f3b;",
            512: "background-color: #f45b7a;",
            1024: "background-color: #35e3e3;",
            2048: "background-color: #5ebb49;",
            4096: "background-color: #458352;",
        }

        self.ui.labelTopScoreValue.setText(f"{self.game.top_score[0]}")
        self.ui.labelYourScoreValue.setText(f"{self.game.your_score}")
        self.ui.labelStatusBar.setText('Welcome! \n'
                                       'You can play by "wasd" keys')
        self.game.new_num_appear()
        self.updateField()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.signCaught.connect(self.onSignCaught)
        self.ui.pushButtonShowTop5.clicked.connect(self.onPushButtonShowTop5)

    def onSignCaught(self, sign: str):
        self.current_sign = sign
        self.makeTurn()

    def makeTurn(self) -> None:
        """
        Игровой процесс

        :return: None
        """

        self.game.turn(self.current_sign)

        if self.game.new_num_appear():  # If we have successfully inserted a new value
            self.updateField()
            self.current_sign = None
        else:  # If we can't insert a new value
            self.signCaught.disconnect(self.onSignCaught)
            # self.gameOver()

    def updateField(self) -> None:
        """
        Обновление игрового поля

        :return: None
        """
        self.ui.labelYourScoreValue.setText(str(self.game.your_score))
        self.ui.labelTopScoreValue.setText(str(self.game.top_score[0]))

        self.ui.label_00.setText(f"{self.game.field[0][0]}")
        self.ui.label_01.setText(f"{self.game.field[0][1]}")
        self.ui.label_02.setText(f"{self.game.field[0][2]}")
        self.ui.label_03.setText(f"{self.game.field[0][3]}")
        self.ui.label_10.setText(f"{self.game.field[1][0]}")
        self.ui.label_11.setText(f"{self.game.field[1][1]}")
        self.ui.label_12.setText(f"{self.game.field[1][2]}")
        self.ui.label_13.setText(f"{self.game.field[1][3]}")
        self.ui.label_20.setText(f"{self.game.field[2][0]}")
        self.ui.label_21.setText(f"{self.game.field[2][1]}")
        self.ui.label_22.setText(f"{self.game.field[2][2]}")
        self.ui.label_23.setText(f"{self.game.field[2][3]}")
        self.ui.label_30.setText(f"{self.game.field[3][0]}")
        self.ui.label_31.setText(f"{self.game.field[3][1]}")
        self.ui.label_32.setText(f"{self.game.field[3][2]}")
        self.ui.label_33.setText(f"{self.game.field[3][3]}")

        self.ui.label_00.setStyleSheet(self.colours[self.game.field[0][0]])
        self.ui.label_01.setStyleSheet(self.colours[self.game.field[0][1]])
        self.ui.label_02.setStyleSheet(self.colours[self.game.field[0][2]])
        self.ui.label_03.setStyleSheet(self.colours[self.game.field[0][3]])
        self.ui.label_10.setStyleSheet(self.colours[self.game.field[1][0]])
        self.ui.label_11.setStyleSheet(self.colours[self.game.field[1][1]])
        self.ui.label_12.setStyleSheet(self.colours[self.game.field[1][2]])
        self.ui.label_13.setStyleSheet(self.colours[self.game.field[1][3]])
        self.ui.label_20.setStyleSheet(self.colours[self.game.field[2][0]])
        self.ui.label_21.setStyleSheet(self.colours[self.game.field[2][1]])
        self.ui.label_22.setStyleSheet(self.colours[self.game.field[2][2]])
        self.ui.label_23.setStyleSheet(self.colours[self.game.field[2][3]])
        self.ui.label_30.setStyleSheet(self.colours[self.game.field[3][0]])
        self.ui.label_31.setStyleSheet(self.colours[self.game.field[3][1]])
        self.ui.label_32.setStyleSheet(self.colours[self.game.field[3][2]])
        self.ui.label_33.setStyleSheet(self.colours[self.game.field[3][3]])

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Обработка нажатия на клавиши клавиатуры

        :param event: QtGui.QKeyEvent
        :return: None
        """
        if event.text() in self.game.signs_to_move:
            self.signCaught.emit(event.text())
            self.ui.labelStatusBar.setText("")
        else:
            self.ui.labelStatusBar.setText("The sign must be in 'wasd': \n"
                                           "w - move up\n"
                                           "a - move left\n"
                                           "s - move down\n"
                                           "d - move right")

    def onPushButtonShowTop5(self):
        self.ui.labelStatusBar.setText(f"top 1: {self.game.top_score[0]}\n"
                                       f"top 2: {self.game.top_score[1]}\n"
                                       f"top 3: {self.game.top_score[2]}\n"
                                       f"top 4: {self.game.top_score[3]}\n"
                                       f"top 5: {self.game.top_score[4]}")

    # def gameOver(self):
    #     self.game.update_top_score()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.game.update_top_score()
        topScoreInMemory = QtCore.QSettings("game_2048_top_score")
        topScoreInMemory.setValue("text", " ".join([str(score) for score in self.game.top_score]))
        print(" ".join([str(score) for score in self.game.top_score]))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
