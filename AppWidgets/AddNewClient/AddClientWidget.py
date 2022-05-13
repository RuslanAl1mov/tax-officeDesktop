# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from DataBaseFunctions.db_connection import DB_Connect


class NewClientAdd(QtWidgets.QWidget):
    def __init__(self, Main_TabWidget, Status_Label, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        self.Main_TabWidget = Main_TabWidget
        self.status_line_Label = Status_Label
        self.connection = DB_Connect()
        self.tab = QtWidgets.QWidget()
        self.activity_Frame = QtWidgets.QFrame(self.tab)
        self.activity_add_Frame = QtWidgets.QFrame(self.activity_Frame)
        self.activity_add_ComboBox = QtWidgets.QComboBox(self.activity_add_Frame)
        db_activities_info = self.connection.information_out("activities")
        self.activities = []
        self.activities.append(["", "Выберите вид деятельности:", "", ""])
        self.activity_add_ComboBox.addItem("Выберите вид деятельности:")
        for hash_info in db_activities_info:
            self.activities.append(list(hash_info.values()))
            self.activity_add_ComboBox.addItem(list(hash_info.values())[1])

        self.city_set_ComboBox = QtWidgets.QComboBox(self.activity_add_Frame)
        db_cities_info = self.connection.information_out("discount_cities")
        self.cities = []
        self.city_set_ComboBox.setEnabled(False)
        for hash_info in db_cities_info:
            self.cities.append(list(hash_info.values()))
            self.city_set_ComboBox.addItem(
                list(hash_info.values())[1] + " - " + str(list(hash_info.values())[2]) + "р.")

    def new_client_form(self):
        def activity_combobox_edit(index):
            self.activity_tax_sum_LineEdit.setText(str(self.activities[index][2]))
            self.activity_penalty_sum_LineEdit.setText(str(self.activities[index][3]))
            if self.activity_add_ComboBox.currentText() == "Выберите вид деятельности:":
                self.city_set_ComboBox.setEnabled(False)
            else:
                self.city_set_ComboBox.setEnabled(True)

        def city_combobox_edit(index):
            self.activity_tax_sum_LineEdit.setText(
                str(int(self.activity_tax_sum_LineEdit.text()) - self.cities[index][2]))
            print(self.cities[index])

        def counter_cl_name_letters():
            try:
                if len(self.client_name_add_LineEdit.text()) > 30 or self.client_name_add_LineEdit.text()[-1].isdigit():
                    self.client_name_add_LineEdit.setText(self.client_name_add_LineEdit.text()[:-1])
                self.client_name_letter_num_Label.setText(str(len(self.client_name_add_LineEdit.text())))
            except IndexError:
                pass

        def counter_cl_secname_letters():
            try:
                if len(self.client_secname_add_LineEdit.text()) > 30 or self.client_secname_add_LineEdit.text()[
                    -1].isdigit():
                    self.client_secname_add_LineEdit.setText(self.client_secname_add_LineEdit.text()[:-1])
                self.client_secname_letter_num_Label.setText(str(len(self.client_secname_add_LineEdit.text())))
            except IndexError:
                pass

        def counter_cl_fathername_letters():
            try:
                if len(self.client_fathername_add_LineEdit.text()) > 30 or self.client_fathername_add_LineEdit.text()[
                    -1].isdigit():
                    self.client_fathername_add_LineEdit.setText(self.client_fathername_add_LineEdit.text()[:-1])
                self.client_fathername_letter_num_Label.setText(str(len(self.client_fathername_add_LineEdit.text())))
            except IndexError:
                pass

        def clickDont_save_client_Btn():
            self.Main_TabWidget.removeTab(self.Main_TabWidget.indexOf(self.tab))

        def clickSaveClient():
            connection = DB_Connect()
            line_edit_Error_style_sheet = "color: red"
            line_edit_Default_style_sheet = "color: black"
            client_information = []
            order_correct = True
            # Проверка наличия имени в строке имени клиента
            if self.client_name_add_LineEdit.text() == '':
                self.client_name_add_Label.setStyleSheet(line_edit_Error_style_sheet)
                order_correct = False
            else:
                self.client_name_add_Label.setStyleSheet(line_edit_Default_style_sheet)
                client_information.append(self.client_name_add_LineEdit.text().lower())

            # Проверка наличия фамилии в строке фамилии клиента
            if self.client_secname_add_LineEdit.text() == '':
                self.client_secname_add_Label.setStyleSheet(line_edit_Error_style_sheet)
                order_correct = False
            else:
                self.client_secname_add_Label.setStyleSheet(line_edit_Default_style_sheet)
                client_information.append(self.client_secname_add_LineEdit.text().lower())

            # Проверка наличия отчества в строке отчества клиента
            if self.client_fathername_add_LineEdit.text() == '':
                self.client_fathername_add_Label.setStyleSheet(line_edit_Error_style_sheet)
                order_correct = False
            else:
                self.client_fathername_add_Label.setStyleSheet(line_edit_Default_style_sheet)
                client_information.append(self.client_fathername_add_LineEdit.text().lower())

            client_information.append(self.date_of_birth_DateEdit.text().replace('.', '-'))

            if self.activity_add_ComboBox.currentText() == "Выберите вид деятельности:":
                self.activity_penalty_sum_Label.setStyleSheet(line_edit_Error_style_sheet)
                self.activity_tax_sum_Label.setStyleSheet(line_edit_Error_style_sheet)
                order_correct = False
            else:
                self.activity_penalty_sum_Label.setStyleSheet(line_edit_Default_style_sheet)
                self.activity_tax_sum_Label.setStyleSheet(line_edit_Default_style_sheet)
                for activity in self.activities:
                    if self.activity_add_ComboBox.currentText() == activity[1]:
                        client_information.append(int(activity[0]))

            for city in self.cities:
                if city[1] + " - " + str(city[2]) + "р." == self.city_set_ComboBox.currentText():
                    client_information.append(city[0])

            if order_correct:
                if connection.check_user_existing(
                        [client_information[0], client_information[1], client_information[2]]):
                    save_activity = connection.save_new_activity(client_information)
                    self.status_line_Label.setText("Вид деятельности сохранен/обновлен")
                    self.Main_TabWidget.removeTab(self.Main_TabWidget.indexOf(self.tab))
                else:
                    save_status = self.connection.save_new_client(info=client_information)
                    self.connection.close_conn()
                    if save_status == "informaton_saved":
                        self.status_line_Label.setText("Новое Юр.Лицо Сохранено")
                        self.Main_TabWidget.removeTab(self.Main_TabWidget.indexOf(self.tab))

            connection.close_conn()

        # self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("NewClientAdd")
        self.tab.setStyleSheet("QLabel{font-family: \"Bahnschrift SemiBold\";"
                               "font-size: 15px;"
                               "color: rgb(75, 75, 75)}"

                               "QComboBox{font-family: \"Bahnschrift SemiBold\";"
                               "font-size: 15px;"
                               "border-radius: 8px;"
                               "border: 1px solid #C7C7C7; "
                               "background-color:white;}"

                               "QLineEdit{border-radius: 8px; "
                               "border: 1px solid #C7C7C7; "
                               "background-color:white;"
                               "font-family: \"Bahnschrift SemiBold\";"
                               "font-size: 17px;}"
                               ""
                               "QComboBox::down-arrow{image: url(./icons/arrow.png);"
                               "width: 13px;"
                               "height: 13px;"
                               "border-width:0px;"
                               "border-radius: 1px;"
                               "border-color:white;"
                               "border-left-style:solid;}"
                               ""
                               "QComboBox::drop-down{width: 30px;"
                               "border: 0px;}"
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
                               )
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # tab title
        self.tab_title_Label = QtWidgets.QLabel(self.tab)
        self.tab_title_Label.setMaximumSize(QtCore.QSize(16777215, 90))
        self.tab_title_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_title_Label.setObjectName("tab_title_Label")
        self.tab_title_Label.setText("Добавление нового Юр. лица")
        self.tab_title_Label.setStyleSheet("background-color: rgba(169, 169, 169, 60);"
                                           "border-radius: 30px;"
                                           "font-family: \"Bahnschrift SemiBold\";"
                                           "font-size: 20px;"
                                           "color: black")
        self.verticalLayout_2.addWidget(self.tab_title_Label)
        # client name add frame
        self.name_Frame = QtWidgets.QFrame(self.tab)
        self.name_Frame.setObjectName("name_Frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.name_Frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.client_name_add_Frame = QtWidgets.QFrame(self.name_Frame)
        self.client_name_add_Frame.setMaximumSize(QtCore.QSize(570, 63))
        self.client_name_add_Frame.setObjectName("client_name_add_Frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.client_name_add_Frame)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(3)
        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.client_name_add_Label = QtWidgets.QLabel(self.client_name_add_Frame)
        self.client_name_add_Label.setMinimumSize(QtCore.QSize(0, 20))
        self.client_name_add_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.client_name_add_Label.setObjectName("client_name_add_Label")
        self.client_name_add_Label.setText("Имя")
        self.gridLayout_6.addWidget(self.client_name_add_Label, 0, 0, 1, 1)
        self.client_name_add_LineEdit = QtWidgets.QLineEdit(self.client_name_add_Frame)
        self.client_name_add_LineEdit.setMinimumSize(QtCore.QSize(300, 30))
        self.client_name_add_LineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.client_name_add_LineEdit.setObjectName("client_name_add_LineEdit")
        self.client_name_add_LineEdit.textChanged.connect(counter_cl_name_letters)
        self.gridLayout_6.addWidget(self.client_name_add_LineEdit, 1, 0, 1, 1)
        self.client_name_letter_num_Label = QtWidgets.QLabel(self.client_name_add_Frame)
        self.client_name_letter_num_Label.setMinimumSize(QtCore.QSize(40, 30))
        self.client_name_letter_num_Label.setMaximumSize(QtCore.QSize(40, 30))
        self.client_name_letter_num_Label.setObjectName("client_name_letter_num_Label")
        self.client_name_letter_num_Label.setText("0")
        self.gridLayout_6.addWidget(self.client_name_letter_num_Label, 1, 1, 1, 1)
        self.horizontalLayout_8.addWidget(self.client_name_add_Frame)
        self.verticalLayout_2.addWidget(self.name_Frame)

        # client second name add
        self.secname_Frame = QtWidgets.QFrame(self.tab)
        self.secname_Frame.setObjectName("secname_Frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.secname_Frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cleient_secname_add_Frame = QtWidgets.QFrame(self.secname_Frame)
        self.cleient_secname_add_Frame.setMinimumSize(QtCore.QSize(0, 0))
        self.cleient_secname_add_Frame.setMaximumSize(QtCore.QSize(570, 63))
        self.cleient_secname_add_Frame.setObjectName("cleient_secname_add_Frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.cleient_secname_add_Frame)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setHorizontalSpacing(5)
        self.gridLayout_7.setVerticalSpacing(2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.client_secname_add_LineEdit = QtWidgets.QLineEdit(self.cleient_secname_add_Frame)
        self.client_secname_add_LineEdit.setMinimumSize(QtCore.QSize(300, 30))
        self.client_secname_add_LineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.client_secname_add_LineEdit.setObjectName("client_secname_add_LineEdit")
        self.client_secname_add_LineEdit.textChanged.connect(counter_cl_secname_letters)
        self.gridLayout_7.addWidget(self.client_secname_add_LineEdit, 1, 0, 1, 1)
        self.client_secname_add_Label = QtWidgets.QLabel(self.cleient_secname_add_Frame)
        self.client_secname_add_Label.setMinimumSize(QtCore.QSize(0, 20))
        self.client_secname_add_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.client_secname_add_Label.setObjectName("client_secname_add_Label")
        self.client_secname_add_Label.setText("Фамилия")
        self.gridLayout_7.addWidget(self.client_secname_add_Label, 0, 0, 1, 1)
        self.client_secname_letter_num_Label = QtWidgets.QLabel(self.cleient_secname_add_Frame)
        self.client_secname_letter_num_Label.setMinimumSize(QtCore.QSize(40, 30))
        self.client_secname_letter_num_Label.setMaximumSize(QtCore.QSize(40, 30))
        self.client_secname_letter_num_Label.setObjectName("client_secname_letter_num_Label")
        self.client_secname_letter_num_Label.setText("0")
        self.gridLayout_7.addWidget(self.client_secname_letter_num_Label, 1, 1, 1, 1)
        self.horizontalLayout_6.addWidget(self.cleient_secname_add_Frame)
        self.verticalLayout_2.addWidget(self.secname_Frame)

        # client father name add
        self.fathername_Frame = QtWidgets.QFrame(self.tab)
        self.fathername_Frame.setObjectName("fathername_Frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.fathername_Frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.client_fathername_add_Frame = QtWidgets.QFrame(self.fathername_Frame)
        self.client_fathername_add_Frame.setMinimumSize(QtCore.QSize(0, 0))
        self.client_fathername_add_Frame.setMaximumSize(QtCore.QSize(570, 63))
        self.client_fathername_add_Frame.setObjectName("client_fathername_add_Frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.client_fathername_add_Frame)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setHorizontalSpacing(5)
        self.gridLayout_8.setVerticalSpacing(2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.client_fathername_add_Label = QtWidgets.QLabel(self.client_fathername_add_Frame)
        self.client_fathername_add_Label.setMinimumSize(QtCore.QSize(0, 20))
        self.client_fathername_add_Label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.client_fathername_add_Label.setObjectName("client_fathername_add_Label")
        self.client_fathername_add_Label.setText("Отчество")
        self.gridLayout_8.addWidget(self.client_fathername_add_Label, 0, 0, 1, 1)
        self.client_fathername_add_LineEdit = QtWidgets.QLineEdit(self.client_fathername_add_Frame)
        self.client_fathername_add_LineEdit.setMinimumSize(QtCore.QSize(300, 30))
        self.client_fathername_add_LineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.client_fathername_add_LineEdit.setObjectName("client_fathername_add_LineEdit")
        self.client_fathername_add_LineEdit.textChanged.connect(counter_cl_fathername_letters)
        self.gridLayout_8.addWidget(self.client_fathername_add_LineEdit, 1, 0, 1, 1)
        self.client_fathername_letter_num_Label = QtWidgets.QLabel(self.client_fathername_add_Frame)
        self.client_fathername_letter_num_Label.setMinimumSize(QtCore.QSize(40, 30))
        self.client_fathername_letter_num_Label.setMaximumSize(QtCore.QSize(40, 30))
        self.client_fathername_letter_num_Label.setObjectName("client_fathername_letter_num_Label")
        self.client_fathername_letter_num_Label.setText("0")
        self.gridLayout_8.addWidget(self.client_fathername_letter_num_Label, 1, 1, 1, 1)
        self.horizontalLayout_7.addWidget(self.client_fathername_add_Frame)
        self.verticalLayout_2.addWidget(self.fathername_Frame)

        # client birthday date add
        self.birthday_Frame = QtWidgets.QFrame(self.tab)
        self.birthday_Frame.setMinimumSize(QtCore.QSize(400, 65))
        self.birthday_Frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.birthday_Frame.setObjectName("birthday_Frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.birthday_Frame)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.client_birthday_add_Frame = QtWidgets.QFrame(self.birthday_Frame)
        self.client_birthday_add_Frame.setMaximumSize(QtCore.QSize(570, 65))
        self.client_birthday_add_Frame.setObjectName("client_birthday_add_Frame")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.client_birthday_add_Frame)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.date_of_birth_Label = QtWidgets.QLabel(self.client_birthday_add_Frame)
        self.date_of_birth_Label.setMinimumSize(QtCore.QSize(100, 20))
        self.date_of_birth_Label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.date_of_birth_Label.setObjectName("date_of_birth_Label")
        self.gridLayout_9.addWidget(self.date_of_birth_Label, 0, 0, 1, 2)
        self.date_of_birth_Label.setText("Дата рождения")
        self.date_of_birth_DateEdit = QtWidgets.QDateEdit(self.client_birthday_add_Frame)
        self.date_of_birth_DateEdit.setMinimumSize(QtCore.QSize(100, 20))
        self.date_of_birth_DateEdit.setMaximumSize(QtCore.QSize(100, 20))
        self.date_of_birth_DateEdit.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.date_of_birth_DateEdit.setCalendarPopup(True)
        self.date_of_birth_DateEdit.setObjectName("date_of_birth_DateEdit")
        self.gridLayout_9.addWidget(self.date_of_birth_DateEdit, 1, 0, 1, 1)
        self.date_of_birth_FrameSpacer = QtWidgets.QFrame(self.client_birthday_add_Frame)
        self.date_of_birth_FrameSpacer.setObjectName("date_of_birth_FrameSpacer")
        self.gridLayout_9.addWidget(self.date_of_birth_FrameSpacer, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.client_birthday_add_Frame, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.birthday_Frame)

        # add activity
        # self.activity_Frame = QtWidgets.QFrame(self.tab)
        self.activity_Frame.setObjectName("activity_Frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.activity_Frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        # self.activity_add_Frame = QtWidgets.QFrame(self.activity_Frame)
        self.activity_add_Frame.setMinimumSize(QtCore.QSize(400, 140))
        self.activity_add_Frame.setMaximumSize(QtCore.QSize(570, 160))
        self.activity_add_Frame.setObjectName("activity_add_Frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.activity_add_Frame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        # self.activity_add_ComboBox = QtWidgets.QComboBox(self.activity_add_Frame)
        self.activity_add_ComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.activity_add_ComboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.activity_add_ComboBox.setObjectName("activity_add_ComboBox")
        self.activity_add_ComboBox.currentIndexChanged.connect(activity_combobox_edit)
        self.gridLayout_4.addWidget(self.activity_add_ComboBox, 2, 0, 1, 3)
        self.activity_tax_sum_LineEdit = QtWidgets.QLineEdit(self.activity_add_Frame)
        self.activity_tax_sum_LineEdit.setMinimumSize(QtCore.QSize(150, 30))
        self.activity_tax_sum_LineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.activity_tax_sum_LineEdit.setObjectName("activity_tax_sum_LineEdit")
        self.activity_tax_sum_LineEdit.setReadOnly(True)
        self.gridLayout_4.addWidget(self.activity_tax_sum_LineEdit, 4, 0, 1, 1)
        self.activity_penalty_sum_LineEdit = QtWidgets.QLineEdit(self.activity_add_Frame)
        self.activity_penalty_sum_LineEdit.setMinimumSize(QtCore.QSize(150, 30))
        self.activity_penalty_sum_LineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.activity_penalty_sum_LineEdit.setObjectName("activity_penalty_sum_LineEdit")
        self.activity_penalty_sum_LineEdit.setReadOnly(True)
        # self.activity_penalty_sum_LineEdit.setEnabled(False)
        self.gridLayout_4.addWidget(self.activity_penalty_sum_LineEdit, 4, 1, 1, 1)
        self.activity_penalty_sum_Label = QtWidgets.QLabel(self.activity_add_Frame)
        self.activity_penalty_sum_Label.setMinimumSize(QtCore.QSize(150, 20))
        self.activity_penalty_sum_Label.setMaximumSize(QtCore.QSize(200, 20))
        self.activity_penalty_sum_Label.setObjectName("activity_penalty_sum_Label")
        self.activity_penalty_sum_Label.setText("Пеня")
        self.gridLayout_4.addWidget(self.activity_penalty_sum_Label, 3, 1, 1, 1)
        self.activity_tax_sum_Label = QtWidgets.QLabel(self.activity_add_Frame)
        self.activity_tax_sum_Label.setMinimumSize(QtCore.QSize(150, 20))
        self.activity_tax_sum_Label.setMaximumSize(QtCore.QSize(200, 20))
        self.activity_tax_sum_Label.setObjectName("activity_tax_sum_Label")
        self.activity_tax_sum_Label.setText("Ежемесячный налог")
        self.gridLayout_4.addWidget(self.activity_tax_sum_Label, 3, 0, 1, 1)

        self.city_set_Label = QtWidgets.QLabel(self.activity_add_Frame)
        self.city_set_Label.setMinimumSize(QtCore.QSize(150, 20))
        self.city_set_Label.setMaximumSize(QtCore.QSize(200, 20))
        self.city_set_Label.setObjectName("activity_penalty_sum_Label")
        self.city_set_Label.setText("Выберите город:")
        self.gridLayout_4.addWidget(self.city_set_Label, 3, 2, 1, 1)
        self.city_set_ComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.city_set_ComboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.city_set_ComboBox.setObjectName("activity_add_ComboBox")
        self.city_set_ComboBox.currentIndexChanged.connect(city_combobox_edit)
        self.gridLayout_4.addWidget(self.city_set_ComboBox, 4, 2, 1, 1)
        self.horizontalLayout_9.addWidget(self.activity_add_Frame)
        self.verticalLayout_2.addWidget(self.activity_Frame)

        # save new client
        self.save_Frame = QtWidgets.QFrame(self.tab)
        self.save_Frame.setMinimumSize(QtCore.QSize(400, 50))
        self.save_Frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.save_Frame.setObjectName("save_Frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.save_Frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.save_client_FrameSpacer = QtWidgets.QFrame(self.save_Frame)
        self.save_client_FrameSpacer.setObjectName("save_client_FrameSpacer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.save_client_FrameSpacer)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4.addWidget(self.save_client_FrameSpacer)
        self.save_client_Frame = QtWidgets.QFrame(self.save_Frame)
        self.save_client_Frame.setMinimumSize(QtCore.QSize(250, 50))
        self.save_client_Frame.setMaximumSize(QtCore.QSize(300, 50))
        self.save_client_Frame.setObjectName("save_client_Frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.save_client_Frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dont_save_client_Btn = QtWidgets.QPushButton(self.save_client_Frame)
        self.dont_save_client_Btn.setMinimumSize(QtCore.QSize(0, 30))
        self.dont_save_client_Btn.setObjectName("dont_save_client_Btn")
        self.dont_save_client_Btn.setText("Удалить")
        self.dont_save_client_Btn.clicked.connect(clickDont_save_client_Btn)
        self.horizontalLayout_3.addWidget(self.dont_save_client_Btn)
        self.save_client_Btn = QtWidgets.QPushButton(self.save_client_Frame)
        self.save_client_Btn.setMinimumSize(QtCore.QSize(0, 30))
        self.save_client_Btn.setObjectName("save_client_Btn")
        self.save_client_Btn.setText("Сохранить")
        self.save_client_Btn.clicked.connect(clickSaveClient)
        self.horizontalLayout_3.addWidget(self.save_client_Btn)
        self.horizontalLayout_4.addWidget(self.save_client_Frame)
        self.verticalLayout_2.addWidget(self.save_Frame)

        return self.tab
