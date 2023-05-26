# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_2048_form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(358, 617)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelTopScore = QLabel(Form)
        self.labelTopScore.setObjectName(u"labelTopScore")
        self.labelTopScore.setMinimumSize(QSize(120, 40))
        self.labelTopScore.setMaximumSize(QSize(120, 40))
        font = QFont()
        font.setPointSize(14)
        self.labelTopScore.setFont(font)

        self.horizontalLayout.addWidget(self.labelTopScore)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.labelTopScoreValue = QLabel(Form)
        self.labelTopScoreValue.setObjectName(u"labelTopScoreValue")
        self.labelTopScoreValue.setMinimumSize(QSize(150, 40))
        self.labelTopScoreValue.setMaximumSize(QSize(150, 40))
        self.labelTopScoreValue.setFont(font)
        self.labelTopScoreValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelTopScoreValue)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelYourScore = QLabel(Form)
        self.labelYourScore.setObjectName(u"labelYourScore")
        self.labelYourScore.setMinimumSize(QSize(120, 40))
        self.labelYourScore.setMaximumSize(QSize(120, 40))
        self.labelYourScore.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelYourScore)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.labelYourScoreValue = QLabel(Form)
        self.labelYourScoreValue.setObjectName(u"labelYourScoreValue")
        self.labelYourScoreValue.setMinimumSize(QSize(150, 40))
        self.labelYourScoreValue.setMaximumSize(QSize(150, 40))
        self.labelYourScoreValue.setFont(font)
        self.labelYourScoreValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.labelYourScoreValue)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_00 = QLabel(Form)
        self.label_00.setObjectName(u"label_00")
        self.label_00.setMinimumSize(QSize(80, 80))
        self.label_00.setMaximumSize(QSize(80, 80))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.label_00.setFont(font1)
        self.label_00.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_00)

        self.label_01 = QLabel(Form)
        self.label_01.setObjectName(u"label_01")
        self.label_01.setMinimumSize(QSize(80, 80))
        self.label_01.setMaximumSize(QSize(80, 80))
        self.label_01.setFont(font1)
        self.label_01.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_01)

        self.label_02 = QLabel(Form)
        self.label_02.setObjectName(u"label_02")
        self.label_02.setMinimumSize(QSize(80, 80))
        self.label_02.setMaximumSize(QSize(80, 80))
        self.label_02.setFont(font1)
        self.label_02.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_02)

        self.label_03 = QLabel(Form)
        self.label_03.setObjectName(u"label_03")
        self.label_03.setMinimumSize(QSize(80, 80))
        self.label_03.setMaximumSize(QSize(80, 80))
        self.label_03.setFont(font1)
        self.label_03.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_03)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(80, 80))
        self.label_10.setMaximumSize(QSize(80, 80))
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(80, 80))
        self.label_11.setMaximumSize(QSize(80, 80))
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(80, 80))
        self.label_12.setMaximumSize(QSize(80, 80))
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_12)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(80, 80))
        self.label_13.setMaximumSize(QSize(80, 80))
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_13)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(80, 80))
        self.label_20.setMaximumSize(QSize(80, 80))
        self.label_20.setFont(font1)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_20)

        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(80, 80))
        self.label_21.setMaximumSize(QSize(80, 80))
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_21)

        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(80, 80))
        self.label_22.setMaximumSize(QSize(80, 80))
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_22)

        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(80, 80))
        self.label_23.setMaximumSize(QSize(80, 80))
        self.label_23.setFont(font1)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_23)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_30 = QLabel(Form)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(80, 80))
        self.label_30.setMaximumSize(QSize(80, 80))
        self.label_30.setFont(font1)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_30)

        self.label_31 = QLabel(Form)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(80, 80))
        self.label_31.setMaximumSize(QSize(80, 80))
        self.label_31.setFont(font1)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_31)

        self.label_32 = QLabel(Form)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(80, 80))
        self.label_32.setMaximumSize(QSize(80, 80))
        self.label_32.setFont(font1)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_32)

        self.label_33 = QLabel(Form)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(80, 80))
        self.label_33.setMaximumSize(QSize(80, 80))
        self.label_33.setFont(font1)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_33)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.labelStatusBar = QLabel(Form)
        self.labelStatusBar.setObjectName(u"labelStatusBar")
        self.labelStatusBar.setMinimumSize(QSize(300, 120))
        self.labelStatusBar.setMaximumSize(QSize(9999, 120))
        font2 = QFont()
        font2.setPointSize(10)
        self.labelStatusBar.setFont(font2)

        self.verticalLayout.addWidget(self.labelStatusBar)

        self.pushButtonShowTop5 = QPushButton(Form)
        self.pushButtonShowTop5.setObjectName(u"pushButtonShowTop5")
        self.pushButtonShowTop5.setFont(font2)

        self.verticalLayout.addWidget(self.pushButtonShowTop5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelTopScore.setText(QCoreApplication.translate("Form", u"Top score:", None))
        self.labelTopScoreValue.setText(QCoreApplication.translate("Form", u"ScoreValue", None))
        self.labelYourScore.setText(QCoreApplication.translate("Form", u"Your score:", None))
        self.labelYourScoreValue.setText(QCoreApplication.translate("Form", u"ScoreValue", None))
        self.label_00.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_01.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_02.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_03.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"2", None))
        self.labelStatusBar.setText(QCoreApplication.translate("Form", u"Status bar", None))
        self.pushButtonShowTop5.setText(QCoreApplication.translate("Form", u"Show top 5 score", None))
    # retranslateUi

