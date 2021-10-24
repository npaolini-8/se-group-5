from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QIcon
from sys import exit, argv
from database_funcs import Warehouse
from main_gui import MainWindow
from login_gui import LoginMainWindow


#Application controls all sub-windows
class Application(QApplication):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('Resources/icon.png'))
        self.warehouse = Warehouse()
        if len(argv) == 1:
            self.init()
        else:
            if argv[1] == 'm':
                self.mainWindow = MainWindow(self)
                self.mainWindow.show()
            else:
                self.init()

    def init(self):
        self.threadpool = QThreadPool()
        self.loginWindow = LoginMainWindow(self)
        self.mainWindow = None
        self.loginWindow.show()

    #Close login window and open main window
    def main_startup(self, user):
        self.mainWindow = MainWindow(self)
        self.mainWindow.show()
        if self.loginWindow != None:
            self.loginWindow = None

if __name__ == '__main__':
    app = Application()
    exit(app.exec())
