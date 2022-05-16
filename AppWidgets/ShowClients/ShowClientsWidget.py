# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from AppWidgets.ShowClients.clientInfoFrame import ClientInfoFrame
from DataBaseFunctions.db_connection import DB_Connect


class ShowClientsList(QtWidgets.QWidget):
    def __init__(self, Main_TabWidget, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        self.Main_TabWidget = Main_TabWidget

    def show_clients_list(self):
        def load_inform_for_frame():
            connection = DB_Connect()
            users_information_hash = connection.information_out("legal_entities")
            users_information = []
            for user in users_information_hash:
                users_information.append(list(user.values()))
            for user in users_information:
                activities_for_count = []
                activities_information = connection.param_information_out(table_name="appropriation",
                                                                          param_name="manager_id", param=int(user[0]))
                for activity in activities_information:
                    if list(activity.values())[-1] == 0:
                        activities_for_count.append(activity)
                ClientFrame = ClientInfoFrame(self.scrollAreaWidgetContents,
                                              [user[1], user[2], user[3], len(activities_for_count)])
                self.verticalLayout_3.addWidget(ClientFrame.client_inform_frame())

            self.scroll_area_FrameSpacer = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            self.scroll_area_FrameSpacer.setObjectName("scroll_area_FrameSpacer")
            self.verticalLayout_3.addWidget(self.scroll_area_FrameSpacer)

        def clickCloseTab():
            self.Main_TabWidget.removeTab(self.Main_TabWidget.indexOf(self.tab))

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab.setStyleSheet("QPushButton{border-radius: 8px; "
                               "border: 1px solid #C7C7C7; "
                               "background-color:white;"
                               "font-family: \"Bahnschrift SemiBold\";"
                               "font-size: 14px;}"
                               ""
                               "QPushButton:hover{"
                               "background-color:rgb(221, 221, 221);}"
                               "QPushButton:pressed{"
                               "background-color:rgb(156, 156, 156);"
                               "color:rgb(241, 241, 241)}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tab_title_Label = QtWidgets.QLabel(self.tab)
        self.tab_title_Label.setMinimumSize(QtCore.QSize(0, 36))
        self.tab_title_Label.setMaximumSize(QtCore.QSize(16777215, 90))
        self.tab_title_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_title_Label.setObjectName("tab_title_Label")
        self.tab_title_Label.setText("Журнал Юр. лиц")
        self.tab_title_Label.setStyleSheet("background-color: rgba(169, 169, 169, 60);"
                                           "border-radius: 15px;"
                                           "font-family: \"Bahnschrift SemiBold\";"
                                           "font-size: 20px;"
                                           "color: black")
        self.verticalLayout_2.addWidget(self.tab_title_Label)
        self.client_activities_info_Frame = QtWidgets.QFrame(self.tab)
        self.client_activities_info_Frame.setMinimumSize(QtCore.QSize(0, 223))
        self.client_activities_info_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.client_activities_info_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.client_activities_info_Frame.setObjectName("client_activities_info_Frame")
        self.client_activities_info_Frame.setStyleSheet("QLabel{"
                                                        "background-color:white;"
                                                        "font-family: \"Bahnschrift SemiBold\";"
                                                        "font-size: 17px;}")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.client_activities_info_Frame)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.client_name_Label = QtWidgets.QLabel(self.client_activities_info_Frame)
        self.client_name_Label.setMinimumSize(QtCore.QSize(0, 30))
        self.client_name_Label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.client_name_Label.setTextFormat(QtCore.Qt.AutoText)
        self.client_name_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.client_name_Label.setObjectName("client_name_Label")
        self.client_name_Label.setText("Имя")
        self.gridLayout_9.addWidget(self.client_name_Label, 0, 1, 1, 1)
        self.client_secname_Label = QtWidgets.QLabel(self.client_activities_info_Frame)
        self.client_secname_Label.setMinimumSize(QtCore.QSize(0, 30))
        self.client_secname_Label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.client_secname_Label.setTextFormat(QtCore.Qt.AutoText)
        self.client_secname_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.client_secname_Label.setObjectName("client_secname_Label")
        self.client_secname_Label.setText("Фамилия")
        self.gridLayout_9.addWidget(self.client_secname_Label, 0, 0, 1, 1)
        self.client_fathername_Label = QtWidgets.QLabel(self.client_activities_info_Frame)
        self.client_fathername_Label.setMinimumSize(QtCore.QSize(0, 30))
        self.client_fathername_Label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.client_fathername_Label.setTextFormat(QtCore.Qt.AutoText)
        self.client_fathername_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.client_fathername_Label.setObjectName("client_fathername_Label")
        self.client_fathername_Label.setText("Отчество")
        self.gridLayout_9.addWidget(self.client_fathername_Label, 0, 2, 1, 1)
        self.client_activities_num_Label = QtWidgets.QLabel(self.client_activities_info_Frame)
        self.client_activities_num_Label.setMinimumSize(QtCore.QSize(0, 30))
        self.client_activities_num_Label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.client_activities_num_Label.setTextFormat(QtCore.Qt.AutoText)
        self.client_activities_num_Label.setText("Видов деят-ти")
        self.client_activities_num_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.client_activities_num_Label.setObjectName("client_activities_num_Label")
        self.gridLayout_9.addWidget(self.client_activities_num_Label, 0, 3, 1, 1)

        self.activity_ScrollArea = QtWidgets.QScrollArea(self.client_activities_info_Frame)
        self.activity_ScrollArea.setMinimumSize(QtCore.QSize(0, 80))
        self.activity_ScrollArea.setWidgetResizable(True)
        self.activity_ScrollArea.setObjectName("activity_ScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 939, 530))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        load_inform_for_frame()
        self.activity_ScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_9.addWidget(self.activity_ScrollArea, 1, 0, 1, 4)
        self.verticalLayout_2.addWidget(self.client_activities_info_Frame)

        # ЗАкрыть форму
        self.close_tab_Frame = QtWidgets.QFrame(self.tab)
        self.close_tab_Frame.setMinimumSize(QtCore.QSize(400, 50))
        self.close_tab_Frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.close_tab_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.close_tab_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.close_tab_Frame.setObjectName("close_tab_Frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.close_tab_Frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.close_tab_FrameSpacer = QtWidgets.QFrame(self.close_tab_Frame)
        self.close_tab_FrameSpacer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.close_tab_FrameSpacer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.close_tab_FrameSpacer.setObjectName("close_tab_FrameSpacer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.close_tab_FrameSpacer)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4.addWidget(self.close_tab_FrameSpacer)
        self.close_tab_btn_Frame = QtWidgets.QFrame(self.close_tab_Frame)
        self.close_tab_btn_Frame.setMinimumSize(QtCore.QSize(250, 50))
        self.close_tab_btn_Frame.setMaximumSize(QtCore.QSize(300, 50))
        self.close_tab_btn_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.close_tab_btn_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.close_tab_btn_Frame.setObjectName("close_tab_btn_Frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.close_tab_btn_Frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.close_tab_Btn = QtWidgets.QPushButton(self.close_tab_btn_Frame)
        self.close_tab_Btn.setMinimumSize(QtCore.QSize(0, 30))
        self.close_tab_Btn.setText("Готово")
        self.close_tab_Btn.setObjectName("close_tab_Btn")
        self.close_tab_Btn.clicked.connect(clickCloseTab)
        self.horizontalLayout_3.addWidget(self.close_tab_Btn)
        self.horizontalLayout_4.addWidget(self.close_tab_btn_Frame)
        self.verticalLayout_2.addWidget(self.close_tab_Frame)

        return self.tab
