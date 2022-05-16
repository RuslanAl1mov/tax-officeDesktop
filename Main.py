from PyQt5 import QtWidgets
from AppWidgets.MainWindow.main_window import MainWindow
from conf import config
import sys

if __name__ == '__main__':
    main_win_app = QtWidgets.QApplication(sys.argv)
    MainWin = MainWindow()
    MainWin.load_configs(config.CONFIG_FILE_PATH)
    MainWin.show()
    sys.exit(main_win_app.exec_())
