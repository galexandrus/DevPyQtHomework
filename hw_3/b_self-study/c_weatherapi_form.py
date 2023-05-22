# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c_weatherapi_form.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(412, 492)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonStart = QPushButton(Form)
        self.pushButtonStart.setObjectName(u"pushButtonStart")
        self.pushButtonStart.setMinimumSize(QSize(70, 40))
        self.pushButtonStart.setMaximumSize(QSize(70, 40))
        font = QFont()
        font.setPointSize(14)
        self.pushButtonStart.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonStart)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButtonChangeCoords = QPushButton(Form)
        self.pushButtonChangeCoords.setObjectName(u"pushButtonChangeCoords")
        self.pushButtonChangeCoords.setMinimumSize(QSize(200, 40))
        self.pushButtonChangeCoords.setMaximumSize(QSize(200, 40))
        self.pushButtonChangeCoords.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonChangeCoords)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButtonStop = QPushButton(Form)
        self.pushButtonStop.setObjectName(u"pushButtonStop")
        self.pushButtonStop.setMinimumSize(QSize(70, 40))
        self.pushButtonStop.setMaximumSize(QSize(70, 40))
        self.pushButtonStop.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonStop)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelLatitude = QLabel(Form)
        self.labelLatitude.setObjectName(u"labelLatitude")
        self.labelLatitude.setMinimumSize(QSize(150, 40))
        self.labelLatitude.setMaximumSize(QSize(150, 40))
        self.labelLatitude.setFont(font)

        self.horizontalLayout.addWidget(self.labelLatitude)

        self.lineEditLatitude = QLineEdit(Form)
        self.lineEditLatitude.setObjectName(u"lineEditLatitude")
        self.lineEditLatitude.setMinimumSize(QSize(150, 40))
        self.lineEditLatitude.setMaximumSize(QSize(150, 40))
        self.lineEditLatitude.setFont(font)
        self.lineEditLatitude.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lineEditLatitude)

        self.labelLatitudeUnits = QLabel(Form)
        self.labelLatitudeUnits.setObjectName(u"labelLatitudeUnits")
        self.labelLatitudeUnits.setMinimumSize(QSize(80, 40))
        self.labelLatitudeUnits.setMaximumSize(QSize(80, 40))
        self.labelLatitudeUnits.setFont(font)

        self.horizontalLayout.addWidget(self.labelLatitudeUnits)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelLongitude = QLabel(Form)
        self.labelLongitude.setObjectName(u"labelLongitude")
        self.labelLongitude.setMinimumSize(QSize(150, 40))
        self.labelLongitude.setMaximumSize(QSize(150, 40))
        self.labelLongitude.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelLongitude)

        self.lineEditLongitude = QLineEdit(Form)
        self.lineEditLongitude.setObjectName(u"lineEditLongitude")
        self.lineEditLongitude.setMinimumSize(QSize(150, 40))
        self.lineEditLongitude.setMaximumSize(QSize(150, 40))
        self.lineEditLongitude.setFont(font)
        self.lineEditLongitude.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lineEditLongitude)

        self.labelLongitudeUnits = QLabel(Form)
        self.labelLongitudeUnits.setObjectName(u"labelLongitudeUnits")
        self.labelLongitudeUnits.setMinimumSize(QSize(80, 40))
        self.labelLongitudeUnits.setMaximumSize(QSize(80, 40))
        self.labelLongitudeUnits.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelLongitudeUnits)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelDelay = QLabel(Form)
        self.labelDelay.setObjectName(u"labelDelay")
        self.labelDelay.setMinimumSize(QSize(150, 40))
        self.labelDelay.setMaximumSize(QSize(150, 40))
        self.labelDelay.setFont(font)

        self.horizontalLayout_4.addWidget(self.labelDelay)

        self.lineEditDelay = QLineEdit(Form)
        self.lineEditDelay.setObjectName(u"lineEditDelay")
        self.lineEditDelay.setMinimumSize(QSize(150, 40))
        self.lineEditDelay.setMaximumSize(QSize(150, 40))
        self.lineEditDelay.setFont(font)
        self.lineEditDelay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lineEditDelay)

        self.labelDelayUnits = QLabel(Form)
        self.labelDelayUnits.setObjectName(u"labelDelayUnits")
        self.labelDelayUnits.setMinimumSize(QSize(80, 40))
        self.labelDelayUnits.setMaximumSize(QSize(80, 40))
        self.labelDelayUnits.setFont(font)

        self.horizontalLayout_4.addWidget(self.labelDelayUnits)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelDateTime = QLabel(Form)
        self.labelDateTime.setObjectName(u"labelDateTime")
        self.labelDateTime.setMinimumSize(QSize(150, 40))
        self.labelDateTime.setMaximumSize(QSize(150, 40))
        self.labelDateTime.setFont(font)

        self.horizontalLayout_5.addWidget(self.labelDateTime)

        self.labelDateTimeValue = QLabel(Form)
        self.labelDateTimeValue.setObjectName(u"labelDateTimeValue")
        self.labelDateTimeValue.setMinimumSize(QSize(150, 40))
        self.labelDateTimeValue.setMaximumSize(QSize(150, 40))
        self.labelDateTimeValue.setFont(font)
        self.labelDateTimeValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.labelDateTimeValue)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelTemperature = QLabel(Form)
        self.labelTemperature.setObjectName(u"labelTemperature")
        self.labelTemperature.setMinimumSize(QSize(150, 40))
        self.labelTemperature.setMaximumSize(QSize(150, 40))
        self.labelTemperature.setFont(font)

        self.horizontalLayout_6.addWidget(self.labelTemperature)

        self.labelTemperatureValue = QLabel(Form)
        self.labelTemperatureValue.setObjectName(u"labelTemperatureValue")
        self.labelTemperatureValue.setMinimumSize(QSize(150, 40))
        self.labelTemperatureValue.setMaximumSize(QSize(150, 40))
        self.labelTemperatureValue.setFont(font)
        self.labelTemperatureValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.labelTemperatureValue)

        self.labelTemperatureUnits = QLabel(Form)
        self.labelTemperatureUnits.setObjectName(u"labelTemperatureUnits")
        self.labelTemperatureUnits.setMinimumSize(QSize(80, 40))
        self.labelTemperatureUnits.setMaximumSize(QSize(80, 40))
        self.labelTemperatureUnits.setFont(font)

        self.horizontalLayout_6.addWidget(self.labelTemperatureUnits)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labelWeatherCode = QLabel(Form)
        self.labelWeatherCode.setObjectName(u"labelWeatherCode")
        self.labelWeatherCode.setMinimumSize(QSize(150, 40))
        self.labelWeatherCode.setMaximumSize(QSize(150, 40))
        self.labelWeatherCode.setFont(font)

        self.horizontalLayout_7.addWidget(self.labelWeatherCode)

        self.labelWeatherCodeValue = QLabel(Form)
        self.labelWeatherCodeValue.setObjectName(u"labelWeatherCodeValue")
        self.labelWeatherCodeValue.setMinimumSize(QSize(150, 40))
        self.labelWeatherCodeValue.setMaximumSize(QSize(150, 40))
        self.labelWeatherCodeValue.setFont(font)
        self.labelWeatherCodeValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.labelWeatherCodeValue)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.labelIsDay = QLabel(Form)
        self.labelIsDay.setObjectName(u"labelIsDay")
        self.labelIsDay.setMinimumSize(QSize(150, 40))
        self.labelIsDay.setMaximumSize(QSize(150, 40))
        self.labelIsDay.setFont(font)

        self.horizontalLayout_8.addWidget(self.labelIsDay)

        self.labelIsDayValue = QLabel(Form)
        self.labelIsDayValue.setObjectName(u"labelIsDayValue")
        self.labelIsDayValue.setMinimumSize(QSize(150, 40))
        self.labelIsDayValue.setMaximumSize(QSize(150, 40))
        self.labelIsDayValue.setFont(font)
        self.labelIsDayValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.labelIsDayValue)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labelWindDirection = QLabel(Form)
        self.labelWindDirection.setObjectName(u"labelWindDirection")
        self.labelWindDirection.setMinimumSize(QSize(150, 40))
        self.labelWindDirection.setMaximumSize(QSize(150, 40))
        self.labelWindDirection.setFont(font)

        self.horizontalLayout_9.addWidget(self.labelWindDirection)

        self.labelWindDirectionValue = QLabel(Form)
        self.labelWindDirectionValue.setObjectName(u"labelWindDirectionValue")
        self.labelWindDirectionValue.setMinimumSize(QSize(150, 40))
        self.labelWindDirectionValue.setMaximumSize(QSize(150, 40))
        self.labelWindDirectionValue.setFont(font)
        self.labelWindDirectionValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.labelWindDirectionValue)

        self.horizontalSpacer_4 = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.labelWindSpeed = QLabel(Form)
        self.labelWindSpeed.setObjectName(u"labelWindSpeed")
        self.labelWindSpeed.setMinimumSize(QSize(150, 40))
        self.labelWindSpeed.setMaximumSize(QSize(150, 40))
        self.labelWindSpeed.setFont(font)

        self.horizontalLayout_10.addWidget(self.labelWindSpeed)

        self.labelWindSpeedValue = QLabel(Form)
        self.labelWindSpeedValue.setObjectName(u"labelWindSpeedValue")
        self.labelWindSpeedValue.setMinimumSize(QSize(150, 40))
        self.labelWindSpeedValue.setMaximumSize(QSize(150, 40))
        self.labelWindSpeedValue.setFont(font)
        self.labelWindSpeedValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.labelWindSpeedValue)

        self.labelWindSpeedUnits = QLabel(Form)
        self.labelWindSpeedUnits.setObjectName(u"labelWindSpeedUnits")
        self.labelWindSpeedUnits.setMinimumSize(QSize(80, 40))
        self.labelWindSpeedUnits.setMaximumSize(QSize(80, 40))
        self.labelWindSpeedUnits.setFont(font)

        self.horizontalLayout_10.addWidget(self.labelWindSpeedUnits)


        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonStart.setText(QCoreApplication.translate("Form", u"Start", None))
        self.pushButtonChangeCoords.setText(QCoreApplication.translate("Form", u"Change coordinates", None))
        self.pushButtonStop.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.labelLatitude.setText(QCoreApplication.translate("Form", u"Latitude", None))
        self.lineEditLatitude.setPlaceholderText(QCoreApplication.translate("Form", u"enter latitude", None))
        self.labelLatitudeUnits.setText(QCoreApplication.translate("Form", u"\u00b0", None))
        self.labelLongitude.setText(QCoreApplication.translate("Form", u"Longitude", None))
        self.lineEditLongitude.setPlaceholderText(QCoreApplication.translate("Form", u"enter longitude", None))
        self.labelLongitudeUnits.setText(QCoreApplication.translate("Form", u"\u00b0", None))
        self.labelDelay.setText(QCoreApplication.translate("Form", u"Delay", None))
        self.lineEditDelay.setPlaceholderText(QCoreApplication.translate("Form", u"enter delay", None))
        self.labelDelayUnits.setText(QCoreApplication.translate("Form", u"s", None))
        self.labelDateTime.setText(QCoreApplication.translate("Form", u"Date & time", None))
        self.labelDateTimeValue.setText(QCoreApplication.translate("Form", u"DateTimeValue", None))
        self.labelTemperature.setText(QCoreApplication.translate("Form", u"Temperature", None))
        self.labelTemperatureValue.setText(QCoreApplication.translate("Form", u"TemperatureValue", None))
        self.labelTemperatureUnits.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.labelWeatherCode.setText(QCoreApplication.translate("Form", u"Weather code", None))
        self.labelWeatherCodeValue.setText(QCoreApplication.translate("Form", u"WeatherCodeVal", None))
        self.labelIsDay.setText(QCoreApplication.translate("Form", u"Is day", None))
        self.labelIsDayValue.setText(QCoreApplication.translate("Form", u"IsDayValue", None))
        self.labelWindDirection.setText(QCoreApplication.translate("Form", u"Wind direction", None))
        self.labelWindDirectionValue.setText(QCoreApplication.translate("Form", u"WindDirectionVal", None))
        self.labelWindSpeed.setText(QCoreApplication.translate("Form", u"Wind speed", None))
        self.labelWindSpeedValue.setText(QCoreApplication.translate("Form", u"WindSpeedValue", None))
        self.labelWindSpeedUnits.setText(QCoreApplication.translate("Form", u"m/s", None))
    # retranslateUi

