"""
Файл для повторения темы генерации сигналов и передачи данных из одного виджета в другой

Напомнить про работу с пользовательскими сигналами.

Предлагается создать 2 формы:
* На первый форме label с надписью "Пройдите регистрацию" и pushButton с текстом "Зарегистрироваться"
* На второй (QDialog) форме:
  * lineEdit с placeholder'ом "Введите логин"
  * lineEdit с placeholder'ом "Введите пароль"
  * pushButton "Зарегистрироваться"

  при нажатии на кнопку, данные из lineEdit'ов передаются в главное окно, в
  котором надпись "Пройдите регистрацию", меняется на "Добро пожаловать {данные из lineEdit с логином}"
  (пароль можно показать в терминале в захешированном виде)
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initChildren()
        self.initSignals()

    def initUi(self):
        self.labelCompleteRegistration = QtWidgets.QLabel("Complete the registration")
        self.pushButtonRegistration = QtWidgets.QPushButton("Register")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.labelCompleteRegistration)
        layout.addWidget(self.pushButtonRegistration)

        self.setLayout(layout)

    def initChildren(self):
        self.registrationDialog = RegistrationDialog()

    def initSignals(self):
        self.pushButtonRegistration.clicked.connect(self.registrationDialog.exec)
        self.registrationDialog.registered.connect(self.registerEnded)

    def registerEnded(self, signal_data):
        self.labelCompleteRegistration.setText(f"Welcome {signal_data[0]}")
        print("password", signal_data[1])


class RegistrationDialog(QtWidgets.QDialog):
    registered = QtCore.Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        self.lineEditLogin = QtWidgets.QLineEdit()
        self.lineEditLogin.setPlaceholderText("Enter login")

        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setPlaceholderText("Enter password")

        self.pushButtonRegistration = QtWidgets.QPushButton("Registration")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditLogin)
        layout.addWidget(self.lineEditPassword)
        layout.addWidget(self.pushButtonRegistration)

        self.setLayout(layout)

    def initSignals(self):
        self.pushButtonRegistration.clicked.connect(self.onPushButtonRegistrationClicked)

    def onPushButtonRegistrationClicked(self):
        self.registered.emit((self.lineEditLogin.text(), self.lineEditPassword.text()))
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
