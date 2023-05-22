# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'b_systemInfo_form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(352, 156)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelTimeDelay = QLabel(Form)
        self.labelTimeDelay.setObjectName(u"labelTimeDelay")
        self.labelTimeDelay.setMinimumSize(QSize(120, 40))
        self.labelTimeDelay.setMaximumSize(QSize(120, 40))
        font = QFont()
        font.setPointSize(14)
        self.labelTimeDelay.setFont(font)

        self.horizontalLayout.addWidget(self.labelTimeDelay)

        self.lineEditTimeDelay = QLineEdit(Form)
        self.lineEditTimeDelay.setObjectName(u"lineEditTimeDelay")
        self.lineEditTimeDelay.setMinimumSize(QSize(150, 40))
        self.lineEditTimeDelay.setMaximumSize(QSize(150, 40))
        self.lineEditTimeDelay.setFont(font)
        self.lineEditTimeDelay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lineEditTimeDelay)

        self.labelTimeDelayUnits = QLabel(Form)
        self.labelTimeDelayUnits.setObjectName(u"labelTimeDelayUnits")
        self.labelTimeDelayUnits.setMinimumSize(QSize(50, 40))
        self.labelTimeDelayUnits.setMaximumSize(QSize(50, 40))
        self.labelTimeDelayUnits.setFont(font)

        self.horizontalLayout.addWidget(self.labelTimeDelayUnits)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelCpuUsage = QLabel(Form)
        self.labelCpuUsage.setObjectName(u"labelCpuUsage")
        self.labelCpuUsage.setMinimumSize(QSize(120, 40))
        self.labelCpuUsage.setMaximumSize(QSize(120, 40))
        self.labelCpuUsage.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelCpuUsage)

        self.labelCpuUsageValue = QLabel(Form)
        self.labelCpuUsageValue.setObjectName(u"labelCpuUsageValue")
        self.labelCpuUsageValue.setMinimumSize(QSize(150, 40))
        self.labelCpuUsageValue.setMaximumSize(QSize(150, 40))
        self.labelCpuUsageValue.setFont(font)
        self.labelCpuUsageValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.labelCpuUsageValue)

        self.labelCpuUsageUnits = QLabel(Form)
        self.labelCpuUsageUnits.setObjectName(u"labelCpuUsageUnits")
        self.labelCpuUsageUnits.setMinimumSize(QSize(50, 40))
        self.labelCpuUsageUnits.setMaximumSize(QSize(50, 40))
        self.labelCpuUsageUnits.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelCpuUsageUnits)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelRamUsage = QLabel(Form)
        self.labelRamUsage.setObjectName(u"labelRamUsage")
        self.labelRamUsage.setMinimumSize(QSize(120, 40))
        self.labelRamUsage.setMaximumSize(QSize(120, 40))
        self.labelRamUsage.setFont(font)

        self.horizontalLayout_3.addWidget(self.labelRamUsage)

        self.labelRamUsageValue = QLabel(Form)
        self.labelRamUsageValue.setObjectName(u"labelRamUsageValue")
        self.labelRamUsageValue.setMinimumSize(QSize(150, 40))
        self.labelRamUsageValue.setMaximumSize(QSize(150, 40))
        self.labelRamUsageValue.setFont(font)
        self.labelRamUsageValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.labelRamUsageValue)

        self.labelRamUsageUnits = QLabel(Form)
        self.labelRamUsageUnits.setObjectName(u"labelRamUsageUnits")
        self.labelRamUsageUnits.setMinimumSize(QSize(50, 40))
        self.labelRamUsageUnits.setMaximumSize(QSize(50, 40))
        self.labelRamUsageUnits.setFont(font)

        self.horizontalLayout_3.addWidget(self.labelRamUsageUnits)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelTimeDelay.setText(QCoreApplication.translate("Form", u"Time delay", None))
        self.lineEditTimeDelay.setPlaceholderText(QCoreApplication.translate("Form", u"enter time here", None))
        self.labelTimeDelayUnits.setText(QCoreApplication.translate("Form", u"s", None))
        self.labelCpuUsage.setText(QCoreApplication.translate("Form", u"CPU usage", None))
        self.labelCpuUsageValue.setText(QCoreApplication.translate("Form", u"CPU usage value", None))
        self.labelCpuUsageUnits.setText(QCoreApplication.translate("Form", u"%", None))
        self.labelRamUsage.setText(QCoreApplication.translate("Form", u"RAM usage", None))
        self.labelRamUsageValue.setText(QCoreApplication.translate("Form", u"RAM usage value", None))
        self.labelRamUsageUnits.setText(QCoreApplication.translate("Form", u"%", None))
    # retranslateUi

