from PySide6.QtWidgets import QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton, QLabel
from time import sleep
from utils import Worker
from PySide6.QtCore import QThreadPool

#Login gui
class LoginWindow(QMainWindow):
    def __init__(self, warehouse_controller):
        super().__init__()
        self.warehouse_controller = warehouse_controller
        self.init_window_props()
        self.init_widgets()
        self.threadpool = QThreadPool()

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
        self.warehouse_controller.switch_to(self, 'main')

    def try_to_login(self):
        valid = not (len(self.userName.text()) == 0 or len(self.passWord.text()) == 0)
        if valid:  #If username and password fields aren't empty
            try:
                self.user = self.warehouse_controller.connect_user(self.userName.text(), self.passWord.text())  #Will cause exception if server is not connected -- will return None if no user with those credentials

                if self.user == None:  #If user + password doesn't exist
                    self.errorLbl.setStyleSheet("color: red;")
                    self.errorLbl.setText("Invalid login credentials.\nPlease try again.")
                else:
                    self.errorLbl.setStyleSheet("color: green;")
                    self.errorLbl.setText("User found.  Logging in.")

                    #Thread an animation to run before closing the login gui and opening main gui
                    worker = Worker(self.load_animation)
                    worker.signals.finished.connect(self.main_startup)
                    self.threadpool.start(worker)

            except Exception as e:
                print(e)
                self.errorLbl.setStyleSheet("color: red;")
                self.errorLbl.setText("Server error - Server may be down.")
        else:
            self.errorLbl.setStyleSheet("color: red;")
            self.errorLbl.setText("One or more fields are blank.")
