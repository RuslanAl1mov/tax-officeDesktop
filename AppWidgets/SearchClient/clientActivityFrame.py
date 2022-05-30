# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from DataBaseFunctions.db_connection import DB_Connect
import configparser
from conf import config


class ScrollaAreaFrame(QtWidgets.QFrame):
    """
    Класс создающий форму для вывода вида деятельности Юридического лица из Базы Данных.
    """
    def __init__(self, scroll_area_Layout, WidgetContent, activity_info, parent=None):
        super(ScrollaAreaFrame, self).__init__(parent)
        self.scroll_area_Layout = scroll_area_Layout
        self.scrollAreaWidgetContents = WidgetContent
        self.connection = DB_Connect()
        print(activity_info)
        self.activity_info = activity_info

    def new_activity_frame(self):
        """
        Функция создающее рамку для вида деятельности, с ее название и кнопкой для удаления этого вида деятельности.
        :return: Созданное окно
        """
        def dialog_window(reasons):
            """
            Функция обработки нажатия на кнопку удаления вида деятельности у Юридического
            лица.
            При нажатии на кнопку, выводится диалоговое окно в котором указывается
            причина закрытия вида деятельности.
            :param reasons: Возможные причины закрытия вида деятельности (подкачиваются из БД).
            :return:
            """
            def clickRemoveActivity():
                """
                Нажатие на кнопку подтверждения удаления вида деятельности.
                :return:
                """
                self.activity_info.append(self.comboBox.currentIndex())
                self.connection.remove_activity(self.activity_info)  # Удаляем вид деятельности
                self.scroll_area_Layout.removeWidget(self.activity_info_Frame)
                self.stack1.close()
                self.activity_info_Frame.close()

            def clickCloseDialogWindow():
                """
                Нажатие на кнопку отмены закрытия вида деятельности.
                :return:
                """
                self.stack1.close()

            self.stack1.setMinimumSize(QtCore.QSize(300, 195))
            self.stack1.setMaximumSize(QtCore.QSize(300, 195))

            self.frame = QtWidgets.QFrame(self.stack1)
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.frame.setStyleSheet("QLabel{"
                                     "border-radius: 8px; "
                                     "border: 1px solid #C7C7C7; "
                                     "background-color:white;"
                                     "font-family: \"Bahnschrift SemiBold\";"
                                     "font-size: 17px;}"
                                     ""
                                     "QPushButton{border-radius: 8px; "
                                     "border: 1px solid #C7C7C7; "
                                     "background-color:white;"
                                     "font-family: \"Bahnschrift SemiBold\";"
                                     "font-size: 14px;}"
                                     ""
                                     "QPushButton:hover{"
                                     "background-color:rgb(221, 221, 221);}"
                                     "QPushButton:pressed{"
                                     "background-color:rgb(156, 156, 156);"
                                     "color:rgb(241, 241, 241)}"
                                     "QComboBox{"
                                     "font-family: \"Bahnschrift SemiBold\";"
                                     "font-size: 15px;"
                                     "border-radius: 8px;"
                                     "border: 1px solid #C7C7C7; "
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
            self.comboBox = QtWidgets.QComboBox(self.frame)
            self.comboBox.setGeometry(QtCore.QRect(10, 70, 281, 31))
            self.comboBox.setObjectName("comboBox")
            for reason in reasons:
                self.comboBox.addItem(reason[1])
            self.label = QtWidgets.QLabel(self.frame)
            self.label.setGeometry(QtCore.QRect(10, 10, 281, 51))
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
            self.label.setText("Причина закрытия:")
            self.close_dialog_window_Btn = QtWidgets.QPushButton(self.frame)
            self.close_dialog_window_Btn.setGeometry(QtCore.QRect(20, 140, 121, 41))
            self.close_dialog_window_Btn.setObjectName("close_dialog_window_Btn")
            self.close_dialog_window_Btn.setText("ЗАКРЫТЬ")
            self.close_dialog_window_Btn.clicked.connect(clickCloseDialogWindow)
            self.remove_activity_Btn = QtWidgets.QPushButton(self.frame)
            self.remove_activity_Btn.setGeometry(QtCore.QRect(150, 140, 121, 41))
            self.remove_activity_Btn.setObjectName("remove_activity_Btn")
            self.remove_activity_Btn.setText("ПОДВТВЕРДИТЬ")
            self.remove_activity_Btn.clicked.connect(clickRemoveActivity)

        def clickDeleteActivity():
            """
            Обработка нажатия на кнопку для выведения диалогового окна, для удаления вида
            деятельности у Юридического лица.
            :return:
            """
            self.stack1.show()

        def load_configs():
            """
            Функция подкачивающая из конфигурационного файла, по указанному пути,
            статус последнего пользователя.

            Пользователь может быть *Администратором или *Юр.лицом.

            В зависимости от статуса пользователя, Пользователь получает/теряет права
            для удаления вида деятельности у юридического лица.
            :return:
            """
            configuration = configparser.ConfigParser()
            configuration.read(config.CONFIG_FILE_PATH)
            if configuration.get("Login", "user") == "0":
                self.delete_activity_Btn.setEnabled(True)
            elif configuration.get("Login", "user") == "1":
                self.delete_activity_Btn.setEnabled(False)

        self.QtStack = QtWidgets.QStackedLayout()
        self.stack1 = QtWidgets.QWidget()
        close_reasons = self.connection.information_out("close_reasons")
        reasons = []
        for reason in close_reasons:
            reasons.append(list(reason.values()))
        dialog_window(reasons)
        self.QtStack.addWidget(self.stack1)
        self.stack1.close()

        self.activity_info_Frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.activity_info_Frame.setMinimumSize(QtCore.QSize(0, 0))
        self.activity_info_Frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.activity_info_Frame.setStyleSheet("QLabel{"
                                               "border-radius: 8px; "
                                               "border: 1px solid #C7C7C7; "
                                               "background-color:white;"
                                               "font-family: \"Bahnschrift SemiBold\";"
                                               "font-size: 17px;}"
                                               ""
                                               "QPushButton{border-radius: 8px; "
                                               "border: 1px solid #C7C7C7; "
                                               "background-color:white;"
                                               "font-family: \"Bahnschrift SemiBold\";"
                                               "font-size: 17px;}"
                                               ""
                                               "QPushButton:hover{"
                                               "background-color:rgb(221, 221, 221);}"
                                               "QPushButton:pressed{"
                                               "background-color:rgb(156, 156, 156);"
                                               "color:rgb(241, 241, 241)}")
        self.activity_info_Frame.setObjectName("activity_info_Frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.activity_info_Frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # Наименование вида деятельности
        self.activite_name_show_Label = QtWidgets.QLabel(self.activity_info_Frame)
        self.activite_name_show_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.activite_name_show_Label.setObjectName("activite_name_show_Label")
        self.activite_name_show_Label.setText(str(self.activity_info[1]))
        self.horizontalLayout_6.addWidget(self.activite_name_show_Label)
        # Налог на вид деятельности
        self.activite_tax_show_Label = QtWidgets.QLabel(self.activity_info_Frame)
        self.activite_tax_show_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.activite_tax_show_Label.setObjectName("activite_tax_show_Label")
        self.activite_tax_show_Label.setText(str(self.activity_info[2]))
        self.horizontalLayout_6.addWidget(self.activite_tax_show_Label)
        # штраф за вид деятельности
        self.activite_penalty_show_Label = QtWidgets.QLabel(self.activity_info_Frame)
        self.activite_penalty_show_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.activite_penalty_show_Label.setObjectName("activite_penalty_show_Label")
        self.activite_penalty_show_Label.setText(str(self.activity_info[3]))
        self.horizontalLayout_6.addWidget(self.activite_penalty_show_Label)
        # город регистрации вида деятельности
        self.activite_city_show_Label = QtWidgets.QLabel(self.activity_info_Frame)
        self.activite_city_show_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.activite_city_show_Label.setObjectName("activite_city_show_Label")
        self.activite_city_show_Label.setText(str(self.activity_info[4]))
        self.horizontalLayout_6.addWidget(self.activite_city_show_Label)
        # кнопка удаления вида деятельности
        self.delete_activity_Btn = QtWidgets.QPushButton(self.activity_info_Frame)
        self.delete_activity_Btn.setMinimumSize(QtCore.QSize(0, 50))
        self.delete_activity_Btn.setObjectName("delete_activity_Btn")
        self.delete_activity_Btn.setText("Удалить")
        self.delete_activity_Btn.clicked.connect(clickDeleteActivity)
        load_configs()
        self.horizontalLayout_6.addWidget(self.delete_activity_Btn)

        return self.activity_info_Frame
