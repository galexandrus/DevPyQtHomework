from PySide6 import QtWidgets, QtCore


# noinspection PyAttributeOutsideInit,PyPep8Naming
class LoginWindow(QtWidgets.QWidget):
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

        self.setWindowTitle("Entrance to app ")

        size = QtCore.QSize(400, 200)
        self.setFixedSize(size)

        labelLogin = QtWidgets.QLabel()
        labelLogin.setMinimumWidth(70)
        labelLogin.setText("Login:")

        labelPassword = QtWidgets.QLabel()
        labelPassword.setMinimumWidth(70)
        labelPassword.setText("Password:")

        self.lineEditLogin = QtWidgets.QLineEdit()

        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.pushButtonRegistration = QtWidgets.QPushButton()
        self.pushButtonRegistration.setText("Registration")

        self.pushButtonOk = QtWidgets.QPushButton()
        self.pushButtonOk.setText("Ok")

        self.pushButtonCancel = QtWidgets.QPushButton()
        self.pushButtonCancel.setText("Cancel")

        # layouts
        layoutLogin = QtWidgets.QHBoxLayout()
        layoutLogin.addWidget(labelLogin)
        layoutLogin.addWidget(self.lineEditLogin)

        layoutPassword = QtWidgets.QHBoxLayout()
        layoutPassword.addWidget(labelPassword)
        layoutPassword.addWidget(self.lineEditPassword)

        layoutRegistration = QtWidgets.QHBoxLayout()
        layoutRegistration.addSpacerItem(
            QtWidgets.QSpacerItem(
                20, 10, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        layoutRegistration.addWidget(self.pushButtonRegistration)

        layoutHandle = QtWidgets.QHBoxLayout()
        layoutHandle.addSpacerItem(
            QtWidgets.QSpacerItem(
                20, 10, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        layoutHandle.addWidget(self.pushButtonOk)
        layoutHandle.addWidget(self.pushButtonCancel)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLogin)
        layoutMain.addLayout(layoutPassword)
        layoutMain.addLayout(layoutRegistration)
        layoutMain.addLayout(layoutHandle)

        self.setLayout(layoutMain)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = LoginWindow()
    win.show()

    app.exec()
