from PySide6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QLineEdit,
QDockWidget, QCheckBox, QVBoxLayout, QWidget, QPushButton, QLabel, QSizePolicy)
from PySide6.QtCore import Qt, QTimer,QRunnable, Slot, QThreadPool, Signal, QObject, QThread
#from pymongo import MongoClient
from ssl import CERT_NONE
from time import sleep
from sys import exit, argv
from database_funcs import Warehouse

#Signals from worker threads
class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

#Worker threads
class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        #self.kwargs['progress_callback'] = self.signals.progress

    #Run a function in this thread
    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()

#Login gui
class LoginMainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.warehouse = app.warehouse
        self.init_window_props()
        self.init_widgets()

    def init_window_props(self):
        self.setWindowTitle('Warehouse System Login')
        geometry = self.screen().availableGeometry()

        #Set window width and heights as percentages of screen resolution
        self.dimensions = (geometry.width() * 0.35, geometry.height() * 0.35)
        self.setFixedSize(self.dimensions[0], self.dimensions[1])

        #Center window on screen
        self.move((geometry.width() - self.dimensions[0]) / 2, (geometry.height() - self.dimensions[1]) / 2)

    def init_widgets(self):
        #Create and configure vertical layout
        layout = QVBoxLayout()
        layout.setContentsMargins(self.dimensions[0] * 0.3, self.dimensions[1] * 0.3,
                               self.dimensions[0] * 0.3, self.dimensions[1] * 0.3)

        #Username and Password LineEdits
        self.userName = QLineEdit()
        self.userName.setPlaceholderText("Enter Username")
        self.passWord = QLineEdit()
        self.passWord.setPlaceholderText("Enter Password")
        self.passWord.setEchoMode(QLineEdit.Password)

        #Login button
        loginBtn = QPushButton("Login")
        loginBtn.clicked.connect(self.try_to_login)

        #Error label for failed attempts
        self.errorLbl = QLabel("")
        self.errorLbl.setMaximumHeight(50)
        self.errorLbl.setStyleSheet("color: red;")

        #Add all widgets to layout
        layout.addWidget(self.userName)
        layout.addWidget(self.passWord)
        layout.addWidget(loginBtn)
        layout.addWidget(self.errorLbl)

        #Use a QWidget to hold the layout and set it as centralWidget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    #Just a cool little login text animation as a confirmation that you are logging in
    def load_animation(self):
        sleep(0.15)
        self.errorLbl.setText("User found.  Logging in..")
        sleep(0.15)
        self.errorLbl.setText("User found.  Logging in...")
        sleep(0.15)
        self.errorLbl.setText("User found.  Logging in....")
        sleep(0.15)
        self.errorLbl.setText("User found.  Logging in.....")
        sleep(0.15)
        self.errorLbl.setText("User found.  Logging in......")
        sleep(0.15)

    def main_startup(self):
        self.app.main_startup(self.user)

    def try_to_login(self):
        valid = not (len(self.userName.text()) == 0 or len(self.passWord.text()) == 0)
        if valid:
            #self.client = MongoClient("mongodb+srv://softgod1:banana123@group5warehouse.kvdys.mongodb.net/test",
                                  #ssl_cert_reqs=CERT_NONE, serverSelectionTimeoutMS=1000)
            try:
                client = self.warehouse.cluster
                client.server_info()
                users = self.warehouse.users_collection
                self.user = users.find_one({"_id": self.userName.text(),"Password": self.passWord.text()})  #BretC1, bananafish6
                if self.user == None:
                    self.errorLbl.setStyleSheet("color: red;")
                    self.errorLbl.setText("Invalid login credentials.\nPlease try again.")
                else:
                    self.errorLbl.setStyleSheet("color: green;")
                    self.errorLbl.setText("User found.  Logging in.")

                    #Thread an animation to run before closing the login gui and opening main gui
                    worker = Worker(self.load_animation)
                    worker.signals.finished.connect(self.main_startup)
                    self.app.threadpool.start(worker)

            except Exception as e:
                print(e)
                self.errorLbl.setStyleSheet("color: red;")
                self.errorLbl.setText("Server error - Server may be down.")
        else:
            self.errorLbl.setStyleSheet("color: red;")
            self.errorLbl.setText("One or more fields are blank.")

#Main gui that most users will be using
#Not even close to finished -- just here as a placeholder
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.warehouse = app.warehouse
        self.init_window_props() #Set window title, dimensions, location
        self.init_central_widget()
        self.init_dock_widgets()
        self.init_menu()

    def try_add_item(self):
        if len(self.idEdit.text()) > 0 and len(self.modelNumberEdit.text()) > 0 and len(self.brandEdit.text()) > 0 and len(self.descriptionEdit.toPlainText()) > 0:
            if self.warehouse.find_item(self.idEdit.text()) == None:
                self.warehouse.create_main_item(self.idEdit.text(), self.descriptionEdit.toPlainText(), self.modelNumberEdit.text(), self.brandEdit.text())
                self.errorLbl.setStyleSheet("color: green;")
                self.errorLbl.setText(self.idEdit.text() + ' successfully added to database.')
                self.idEdit.clear()
                self.modelNumberEdit.clear()
                self.brandEdit.clear()
                self.descriptionEdit.clear()
                self.refresh_items()
            else:
                self.errorLbl.setStyleSheet("color: red;")
                self.errorLbl.setText(self.idEdit.text() + ' already exists. Cannot add item.')
        else:
            self.errorLbl.setStyleSheet("color: red;")
            self.errorLbl.setText('One or more fields are empty. Cannot add item.')


    def init_central_widget(self):
        layout = QVBoxLayout()
        addItemBtn = QPushButton("Add Item to Database")
        addItemBtn.clicked.connect(self.try_add_item)
        #Username and Password LineEdits
        self.idEdit = QLineEdit()
        self.idEdit.setPlaceholderText("_id")
        self.modelNumberEdit = QLineEdit()
        self.modelNumberEdit.setPlaceholderText("Model Number")
        self.brandEdit = QLineEdit()
        self.brandEdit.setPlaceholderText("Brand")
        self.descriptionEdit = QTextEdit()
        self.descriptionEdit.setPlaceholderText("Description")
        self.errorLbl = QLabel("")
        self.errorLbl.setMaximumHeight(50)
        self.errorLbl.setStyleSheet("color: red;")

        layout.addWidget(self.errorLbl)
        layout.addWidget(addItemBtn)
        layout.addWidget(self.idEdit)
        layout.addWidget(self.modelNumberEdit)
        layout.addWidget(self.brandEdit)
        layout.addWidget(self.descriptionEdit)
        layout.addStretch(1)
        container_widget = QWidget()
        container_widget.setLayout(layout)
        self.setCentralWidget(container_widget)

    def refresh_items(self):
        self.itemBox.clear()
        items = self.warehouse.get_items()
        for item in items:
            self.itemBox.append(item['_id'] + ': ' + item['Description'] + '\n\n')

    def init_dock_widgets(self):
        widget = QDockWidget("Item Catalog")
        self.addDockWidget(Qt.LeftDockWidgetArea, widget)
        self.resizeDocks([widget], [self.dimensions[0] * 0.25], Qt.Horizontal)
        layout = QVBoxLayout()

        self.itemBox = QTextEdit()
        self.itemBox.setReadOnly(True)
        self.refresh_items()

        layout.addWidget(self.itemBox)

        #layout.addStretch(1)
        container_widget = QWidget()
        container_widget.setLayout(layout)
        widget.setWidget(container_widget)

    def init_window_props(self):
        self.setWindowTitle('Warehouse System Control Panel')
        geometry = self.screen().availableGeometry()
        self.dimensions = (geometry.width() * 0.8, geometry.height() * 0.8)
        self.resize(self.dimensions[0], self.dimensions[1])
        self.move((geometry.width() - self.dimensions[0]) / 2, (geometry.height() - self.dimensions[1]) / 2)

    def init_menu(self):
        self.menuBar().addMenu("File")
        self.menuBar().addMenu("Edit")
        self.menuBar().addMenu("View")

#Application controls all sub-windows
class Application(QApplication):
    def __init__(self):
        super().__init__()
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
