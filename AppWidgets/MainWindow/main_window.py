# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from AppWidgets.AddNewClient.AddClientWidget import NewClientAdd
from AppWidgets.SearchClient.ClientSearchWidget import SearchClient
from AppWidgets.ShowClients.ShowClientsWidget import ShowClientsList
from conf import config
import configparser
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('./icons/main_icon.png'))
        MainWindow.resize(881, 717)
        MainWindow.setWindowTitle("Налоговая инспекция")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(570, 600)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setObjectName("main_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.main_frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.status_line_Frame = QtWidgets.QFrame(self.main_frame)
        self.status_line_Frame.setMinimumSize(QtCore.QSize(0, 50))
        self.status_line_Frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.status_line_Frame.setObjectName("status_line_Frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.status_line_Frame)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.program_name_Label = QtWidgets.QLabel(self.status_line_Frame)
        self.program_name_Label.setMinimumSize(QtCore.QSize(180, 0))
        self.program_name_Label.setMaximumSize(QtCore.QSize(180, 16777215))
        self.program_name_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.program_name_Label.setObjectName("program_name_Label")
        self.program_name_Label.setText("Налоговая инспекция")
        self.program_name_Label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \
                                               stop:0 rgba(124, 124, 124, 149), stop:1 rgba(255, 255, 255, 0));"
                                              "border-radius: 10px;"
                                              "font-family:\"Times New Roman\";"
                                              "font-size: 18px")
        self.horizontalLayout.addWidget(self.program_name_Label)

        self.status_line_SpacerFrame = QtWidgets.QFrame(self.status_line_Frame)
        self.status_line_SpacerFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.status_line_SpacerFrame.setObjectName("status_line_SpacerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.status_line_SpacerFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.status_line_Label = QtWidgets.QLabel(self.status_line_SpacerFrame)
        self.status_line_Label.setStyleSheet("background-color: rgb(222, 222, 222)")
        self.status_line_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_line_Label.setObjectName("status_line_Label")
        self.status_line_Label.setText("ИЗМЕНЕНИЯ")
        self.status_line_Label.setStyleSheet("background-color: rgba(169, 169, 169, 60);"
                                             "border-radius: 10px;"
                                             "font-family: \"Bahnschrift SemiBold\";"
                                             "font-size: 20px;")
        self.horizontalLayout_2.addWidget(self.status_line_Label)
        self.horizontalLayout.addWidget(self.status_line_SpacerFrame)

        self.log_in_Btn = QtWidgets.QPushButton(self.status_line_Frame)
        self.log_in_Btn.setMinimumSize(QtCore.QSize(40, 40))
        self.log_in_Btn.setMaximumSize(QtCore.QSize(40, 40))
        self.log_in_Btn.setStyleSheet("")
        self.log_in_Btn.setObjectName("log_in_Btn")
        self.log_in_Btn.setText("Log in")
        self.log_in_Btn.setStyleSheet("QPushButton{background-color: rgba(169, 169, 169, 60);"
                                      "border-radius: 20px;"
                                      "font-family: \"Bahnschrift SemiBold\"}"
                                      "QPushButton#log_in_Btn:hover{"
                                      "background-color: rgba(0, 141, 28, 100);}"
                                      "QPushButton#log_in_Btn:pressed{"
                                      "background-color: rgba(0, 141, 28, 140);"
                                      "border_width: 2px}")
        self.log_in_Btn.clicked.connect(self.clicLoginBtn)
        self.horizontalLayout.addWidget(self.log_in_Btn)
        self.gridLayout_2.addWidget(self.status_line_Frame, 0, 0, 1, 2)

        self.frame = QtWidgets.QFrame(self.main_frame)
        self.frame.setMinimumSize(QtCore.QSize(160, 400))
        self.frame.setMaximumSize(QtCore.QSize(180, 16777215))
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("QPushButton{"
                                 "background-color: rgba(169, 169, 169, 120);"
                                 "border-radius: 8px;"
                                 "font-family: \"Bahnschrift SemiBold\";"
                                 "font-size: 13px;}"
                                 "QPushButton:hover{"
                                 "background-color: rgba(0, 141, 28, 120);}"
                                 "QPushButton:pressed{"
                                 "background-color: rgba(0, 141, 28, 160);}")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.function1_Btn = QtWidgets.QPushButton(self.frame)
        self.function1_Btn.setMinimumSize(QtCore.QSize(0, 50))
        self.function1_Btn.setObjectName("function1_Btn")
        self.function1_Btn.setText("Добавить юр.лицо/ \n Добавить деят-ть")
        self.function1_Btn.clicked.connect(self.start_Function1)
        self.verticalLayout.addWidget(self.function1_Btn)

        self.function2_Btn = QtWidgets.QPushButton(self.frame)
        self.function2_Btn.setMinimumSize(QtCore.QSize(0, 50))
        self.function2_Btn.setObjectName("function2_Btn")
        self.function2_Btn.setText("Найти юр.лицо")
        self.function2_Btn.clicked.connect(self.start_Function2)
        self.verticalLayout.addWidget(self.function2_Btn)

        self.function3_Btn = QtWidgets.QPushButton(self.frame)
        self.function3_Btn.setMinimumSize(QtCore.QSize(0, 50))
        self.function3_Btn.setObjectName("finction3_Btn")
        self.function3_Btn.setText("Показать список \n юр.лиц")
        self.function3_Btn.clicked.connect(self.start_Function3)
        self.verticalLayout.addWidget(self.function3_Btn)

        self.function4_Btn = QtWidgets.QPushButton(self.frame)
        self.function4_Btn.setMinimumSize(QtCore.QSize(0, 50))
        self.function4_Btn.setObjectName("function4_Btn")
        self.function4_Btn.setText("Здесь может быть \n ваша кнопка")
        self.function4_Btn.clicked.connect(self.start_Function4)
        self.verticalLayout.addWidget(self.function4_Btn)

        self.main_menu_SpacerFrame = QtWidgets.QFrame(self.frame)
        self.main_menu_SpacerFrame.setObjectName("main_menu_SpacerFrame")
        self.verticalLayout.addWidget(self.main_menu_SpacerFrame)

        self.quit_Bnt = QtWidgets.QPushButton(self.frame)
        self.quit_Bnt.setMinimumSize(QtCore.QSize(0, 40))
        self.quit_Bnt.setObjectName("quit_Bnt")
        self.quit_Bnt.setText("Exit")
        self.quit_Bnt.clicked.connect(self.ClickExitBtn)
        self.verticalLayout.addWidget(self.quit_Bnt)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.main_widgets_Frame = QtWidgets.QFrame(self.main_frame)
        self.main_widgets_Frame.setMinimumSize(QtCore.QSize(400, 400))
        self.main_widgets_Frame.setObjectName("main_widgets_Frame")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.main_widgets_Frame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.main_TabWidget = QtWidgets.QTabWidget(self.main_widgets_Frame)
        self.main_TabWidget.setMinimumSize(QtCore.QSize(400, 400))
        # self.main_TabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        # self.main_TabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        # self.main_TabWidget.setUsesScrollButtons(True)
        self.main_TabWidget.setObjectName("main_TabWidget")
        self.gridLayout_3.addWidget(self.main_TabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.main_widgets_Frame, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.main_frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

    def load_configs(self, path_to_config_file):
        config = configparser.ConfigParser()
        config.read(path_to_config_file)
        if config.get("Login", "user") == "0":
            self.function1_Btn.setEnabled(True)
        elif config.get("Login", "user") == "1":
            self.function1_Btn.setEnabled(False)

    def clicLoginBtn(self):
        def dialog_window():
            def clickChangeUser():
                configuration = configparser.ConfigParser()
                configuration.read(config.CONFIG_FILE_PATH)
                if self.comboBox.currentIndex() == 0 and configuration.get("Login", "user") == "1":
                    configuration.set("Login", "user", "0")  # 0 - налоговая 1 - юр лицо
                    with open(config.CONFIG_FILE_PATH, "w") as config_file:
                        configuration.write(config_file)

                    for i in range(self.main_TabWidget.count()):
                        self.main_TabWidget.widget(i).deleteLater()

                    self.load_configs(config.CONFIG_FILE_PATH)
                elif self.comboBox.currentIndex() == 1 and configuration.get("Login", "user") == "0":
                    configuration.set("Login", "user", "1")  # 0 - налоговая 1 - юр лицо
                    with open(config.CONFIG_FILE_PATH, "w") as config_file:
                        configuration.write(config_file)

                    for i in range(self.main_TabWidget.count()):
                        self.main_TabWidget.widget(i).deleteLater()

                    self.load_configs(config.CONFIG_FILE_PATH)

                self.stack1.close()


            def clickCloseDialogWindow():
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
            self.comboBox.addItem("Налоговая служба")
            self.comboBox.addItem("Юридическое лицо")

            configuration = configparser.ConfigParser()
            configuration.read(config.CONFIG_FILE_PATH)
            self.comboBox.setCurrentIndex(int(configuration.get("Login", "user")))

            self.label = QtWidgets.QLabel(self.frame)
            self.label.setGeometry(QtCore.QRect(10, 10, 281, 51))
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
            self.label.setText("Сменить пользователя")
            self.close_dialog_window_Btn = QtWidgets.QPushButton(self.frame)
            self.close_dialog_window_Btn.setGeometry(QtCore.QRect(20, 140, 121, 41))
            self.close_dialog_window_Btn.setObjectName("close_dialog_window_Btn")
            self.close_dialog_window_Btn.setText("ЗАКРЫТЬ")
            self.close_dialog_window_Btn.clicked.connect(clickCloseDialogWindow)
            self.change_user_Btn = QtWidgets.QPushButton(self.frame)
            self.change_user_Btn.setGeometry(QtCore.QRect(150, 140, 121, 41))
            self.change_user_Btn.setObjectName("change_user_Btn")
            self.change_user_Btn.setText("СМЕНИТЬ")
            self.change_user_Btn.clicked.connect(clickChangeUser)

        self.QtStack = QtWidgets.QStackedLayout()
        self.stack1 = QtWidgets.QWidget()
        dialog_window()
        self.QtStack.addWidget(self.stack1)


    def start_Function1(self):
        self.NewClientWidget = NewClientAdd(self.main_TabWidget, self.status_line_Label)
        self.add_client_tab = self.NewClientWidget.new_client_form()
        self.main_TabWidget.addTab(self.add_client_tab, "Создать юр.лицо")
        self.status_line_Label.setText("")
        # Переключение на новое окно
        self.main_TabWidget.setCurrentIndex(self.main_TabWidget.indexOf(self.add_client_tab))

        # self.main_TabWidget.setCurrentIndex(0)

    def start_Function2(self):
        self.SearchClientWidget = SearchClient(self.main_TabWidget, self.status_line_Label)
        self.add_search_client_tab = self.SearchClientWidget.search_client_form()
        self.main_TabWidget.addTab(self.add_search_client_tab, "Поиск юр.лица")
        self.status_line_Label.setText("")
        # Переключение на новое окно
        self.main_TabWidget.setCurrentIndex(self.main_TabWidget.indexOf(self.add_search_client_tab))

    def start_Function3(self):
        self.ShowClientsWidget = ShowClientsList(self.main_TabWidget)
        self.add_clients_list_tab = self.ShowClientsWidget.show_clients_list()
        self.main_TabWidget.addTab(self.add_clients_list_tab, "Список юр.лиц")
        self.status_line_Label.setText("")
        # Переключение на новое окно
        self.main_TabWidget.setCurrentIndex(self.main_TabWidget.indexOf(self.add_clients_list_tab))

    def start_Function4(self):
        pass

    def ClickExitBtn(self):
        sys.exit(main_win_app.exec_())


if __name__ == '__main__':
    main_win_app = QtWidgets.QApplication(sys.argv)
    MainWin = MainWindow()
    MainWin.load_configs(config.CONFIG_FILE_PATH)
    MainWin.show()
    sys.exit(main_win_app.exec_())
