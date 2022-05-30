# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets

"""
Контроллер диалогового окна для смены пользователя
"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        """
        Функция создающая диалоговое окно.
        :param MainWindow: Родительское окно.
        :return:
        """

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 195)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 195))
        MainWindow.setMaximumSize(QtCore.QSize(300, 195))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setStyleSheet("QLabel{"
                                 "font-family: \"Bahnschrift SemiBold\";"
                                 "font-size: 15px;"
                                 "color: rgb(75, 75, 75)}"
                                 "QPushButton{border-radius: 8px;"
                                 "border: 1px solid #C7C7C7;"
                                 "background-color:white;"
                                 "font-family: \"Bahnschrift SemiBold\";"
                                 "font-size: 17px;}\n"
                                 "QPushButton:hover{"
                                 "background-color:rgb(221, 221, 221);}\n"
                                 "QPushButton:pressed{"
                                 "background-color:rgb(156, 156, 156);"
                                 "color:rgb(241, 241, 241)}"
                                 "QComboBox{"
                                 "font-family: \"Bahnschrift SemiBold\";"
                                 "font-size: 15px;"
                                 "border-radius: 8px;"
                                 "border: 1px solid #C7C7C7;"
                                 "background-color:white;}"
                                 "QComboBox::down-arrow{"
                                 "image: url(./icons/arrow.png);"
                                 "width: 13px;"
                                 "height: 13px;"
                                 "border-width:0px;"
                                 "border-radius: 1px;"
                                 "border-color:white;"
                                 "border-left-style:solid;}"
                                 "QComboBox::drop-down{"
                                 "width: 30px;"
                                 "border: 0px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 70, 281, 31))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 140, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 140, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Функция определения надписей на виджетах
        :param MainWindow: Родительское окно.
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Сменить пользователя:"))
        self.pushButton.setText(_translate("MainWindow", "ЗАКРЫТЬ"))
        self.pushButton_2.setText(_translate("MainWindow", "СМЕНИТЬ"))
