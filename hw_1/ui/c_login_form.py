# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c_login_form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)


# noinspection PyAttributeOutsideInit,PyPep8Naming
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 160)
        Form.setMinimumSize(QSize(320, 160))
        Form.setMaximumSize(QSize(320, 160))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelLogin = QLabel(Form)
        self.labelLogin.setObjectName(u"labelLogin")
        self.labelLogin.setMinimumSize(QSize(70, 0))

        self.horizontalLayout.addWidget(self.labelLogin)

        self.lineEditLogin = QLineEdit(Form)
        self.lineEditLogin.setObjectName(u"lineEditLogin")

        self.horizontalLayout.addWidget(self.lineEditLogin)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelPassword = QLabel(Form)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_2.addWidget(self.labelPassword)

        self.lineEditPassword = QLineEdit(Form)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_2.addWidget(self.lineEditPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButtonRegistration = QPushButton(Form)
        self.pushButtonRegistration.setObjectName(u"pushButtonRegistration")

        self.horizontalLayout_3.addWidget(self.pushButtonRegistration)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButtonOk = QPushButton(Form)
        self.pushButtonOk.setObjectName(u"pushButtonOk")

        self.horizontalLayout_4.addWidget(self.pushButtonOk)

        self.pushButtonCancel = QPushButton(Form)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.horizontalLayout_4.addWidget(self.pushButtonCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelLogin.setText(QCoreApplication.translate("Form", u"Login:", None))
        self.labelPassword.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.pushButtonRegistration.setText(QCoreApplication.translate("Form", u"Registration", None))
        self.pushButtonOk.setText(QCoreApplication.translate("Form", u"Ok", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

