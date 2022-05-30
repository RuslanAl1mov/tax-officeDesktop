# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class ClientInfoFrame(QtWidgets.QFrame):
    """
    Класс для создания формы с информацией о Юридическом лице.
    """
    def __init__(self, WidgetContent, cl_info, parent=None):
        """
        Инициализация класса и родительского окна.
        :param WidgetContent: ContentWidget родителя
        :param cl_info: Информация о Юридическом лице, которая должна быть выведена в создаваемой форме
        :param parent: None
        """
        super(ClientInfoFrame, self).__init__(parent)
        self.scrollAreaWidgetContents = WidgetContent
        self.cl_info = cl_info

    def client_inform_frame(self):
        """
        Функция создающая форму с информацией о Юридическом лице.
        :return: Форма с информацией о Юридическом лице.
        """
        self.activity_info_Frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.activity_info_Frame.setMinimumSize(QtCore.QSize(0, 0))
        self.activity_info_Frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.activity_info_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.activity_info_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.activity_info_Frame.setObjectName("activity_info_Frame")
        self.activity_info_Frame.setStyleSheet("QLabel{"
                                               "border-radius: 8px; "
                                               "border: 1px solid #C7C7C7; "
                                               "background-color:white;"
                                               "font-family: \"Bahnschrift SemiBold\";"
                                               "font-size: 17px;}")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.activity_info_Frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        # Фамилия лица
        self.client_secname_show_Label = QtWidgets.QLabel(self.activity_info_Frame)
        self.client_secname_show_Label.setMinimumSize(QtCore.QSize(0, 30))
        self.client_secname_show_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.client_secname_show_Label.setObjectName("client_secname_show_Label")
        self.client_secname_show_Label.setText(self.cl_info[1])
        self.horizontalLayout_6.addWidget(self.client_secname_show_Label)
        # Имя лица
        self.client_name_show_Label = QtWidgets.QLabel(self.activity_info_Frame)
        self.client_name_show_Label.setText(self.cl_info[0])
        self.client_name_show_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.client_name_show_Label.setObjectName("client_name_show_Label")
        self.horizontalLayout_6.addWidget(self.client_name_show_Label)
        # Отчество лица
        self.client_fathername_show_Label = QtWidgets.QLabel(self.activity_info_Frame)
        self.client_fathername_show_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.client_fathername_show_Label.setObjectName("client_fathername_show_Label")
        self.client_fathername_show_Label.setText(self.cl_info[2])
        self.horizontalLayout_6.addWidget(self.client_fathername_show_Label)
        # Кол-во форм деятельности
        self.client_activities_num_show_Label = QtWidgets.QLabel(self.activity_info_Frame)
        self.client_activities_num_show_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.client_activities_num_show_Label.setObjectName("client_activities_num_show_Label")
        self.client_activities_num_show_Label.setText(str(self.cl_info[3]))
        self.horizontalLayout_6.addWidget(self.client_activities_num_show_Label)

        return self.activity_info_Frame






