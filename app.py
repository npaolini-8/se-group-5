from PySide6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QLineEdit,
QDockWidget, QCheckBox, QVBoxLayout, QWidget, QPushButton, QLabel, QSizePolicy)
from PySide6.QtCore import Qt, QTimer,QRunnable, Slot, QThreadPool, Signal, QObject, QThread
from pymongo import MongoClient
from ssl import CERT_NONE
from time import sleep
from sys import exit, argv

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
        self.app.main_startup(self.client, self.user)

    def try_to_login(self):
        valid = not (len(self.userName.text()) == 0 or len(self.passWord.text()) == 0)
        if valid:
            self.client = MongoClient("mongodb+srv://softgod1:banana123@group5warehouse.kvdys.mongodb.net/test",
                                  ssl_cert_reqs=CERT_NONE, serverSelectionTimeoutMS=1000)
            try:
                self.client.server_info()
                db = self.client.warehouse
                users = db.users
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
    def __init__(self):
        super().__init__()
        self.init_window_props() #Set window title, dimensions, location
        self.init_central_widget()
        self.init_dock_widgets()
        self.init_menu()

    def init_central_widget(self):
        layout = QVBoxLayout()
        addItemBtn = QPushButton("Add Item to Database")
        #Username and Password LineEdits
        idEdit = QLineEdit()
        idEdit.setPlaceholderText("_id")
        modelNumberEdit = QLineEdit()
        modelNumberEdit.setPlaceholderText("Model Number")
        brandEdit = QLineEdit()
        brandEdit.setPlaceholderText("Brand")
        descriptionEdit = QTextEdit()
        descriptionEdit.setPlaceholderText("Description")

        layout.addWidget(addItemBtn)
        layout.addWidget(idEdit)
        layout.addWidget(modelNumberEdit)
        layout.addWidget(brandEdit)
        layout.addWidget(descriptionEdit)
        layout.addStretch(1)
        container_widget = QWidget()
        container_widget.setLayout(layout)
        self.setCentralWidget(container_widget)

    def init_dock_widgets(self):
        widget = QDockWidget("Item Finder")
        self.addDockWidget(Qt.LeftDockWidgetArea, widget)
        self.resizeDocks([widget], [self.dimensions[0] * 0.25], Qt.Horizontal)
        layout = QVBoxLayout()
        label = QLabel("Search By:")
        #label.setStyleSheet("border: 1px solid black;")

        layout.addWidget(label)
        #label.setAlignment(Qt.AlignTop)
        label.setMaximumHeight(100)
        layout.addWidget(QPushButton("Press"))
        layout.addWidget(QPushButton("Press"))
        layout.addWidget(QPushButton("Press"))
        layout.addWidget(QPushButton("Press"))
        #layout.addStrut(200) #Add minimum width/height

        layout.addStretch(1)
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
        #if (len(argv) == 0):
        self.threadpool = QThreadPool()
        self.loginWindow = LoginMainWindow(self)
        self.mainWindow = None
        self.loginWindow.show()
        #else:
        #    if argv[0] == 'm':
        #        self.mainWindow = MainWindow()
        #        self.mainWindow.show()

    #Close login window and open main window
    def main_startup(self, client, user):
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        if self.loginWindow != None:
            self.loginWindow = None

if __name__ == '__main__':
    app = Application()
    exit(app.exec())
