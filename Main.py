from PyQt5 import QtWidgets
from AppWidgets.MainWindow.main_window import MainWindow
import sys

if __name__ == '__main__':
    main_win_app = QtWidgets.QApplication(sys.argv)
    MainWin = MainWindow()
    MainWin.load_configs()
    MainWin.show()
    sys.exit(main_win_app.exec_())
