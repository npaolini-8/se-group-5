from PySide6.QtWidgets import QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton, QLabel
from time import sleep
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
        self.setStyleSheet("background-color:#808000")

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
        self.userName.setStyleSheet("background-color:#000000; color:#cbd3d7;padding: 6px 2px;border: 1px solid #cbd3d7")
        self.passWord = QLineEdit()
        self.passWord.setPlaceholderText("Enter Password")
        self.passWord.setStyleSheet("background-color:#000000; color:#cbd3d7;padding: 6px 2px;border: 1px solid #cbd3d7")
        self.passWord.setEchoMode(QLineEdit.Password)

        #Login button
        
        loginBtn = QPushButton("Login")
        loginBtn.setStyleSheet("background-color: #000000;color:#cbd3d7;border:2px solid #cbd3d7")
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
        self.errorLbl.setStyleSheet("color: green;")
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
        self.errorLbl.setText("")
        self.warehouse_controller.switch_to(self, 'main')

    def try_to_login(self):
        valid = not (len(self.userName.text()) == 0 or len(self.passWord.text()) == 0)
        if valid:  #If username and password fields aren't empty
            try:
                user = self.warehouse_controller.connect_user(self.userName.text(), self.passWord.text())  #Will cause exception if server is not connected -- will return None if no user with those credentials

                if user == None:  #If user + password doesn't exist
                    self.warehouse_controller.increment_user_lock(self.userName.text())
                    self.errorLbl.setStyleSheet("color: red;")
                    self.errorLbl.setText(f"Invalid login credentials.\nPlease try again.")
                    
                else:
                    if self.warehouse_controller.get_user_lock(self.userName.text()) >= 3:
                        self.errorLbl.setStyleSheet("color: red;")
                        self.errorLbl.setText(f"Account is currently locked.\nPlease contact an administrator.")
                    else:
                        self.errorLbl.setStyleSheet("color: green;")
                        self.errorLbl.setText("User found.  Logging in.")
                        self.warehouse_controller.set_current_user(user)

                        #Thread an animation to run before closing the login gui and opening main gui
                        #worker = Worker(self.load_animation)
                        #worker.signals.finished.connect(self.main_startup)
                        #self.threadpool.start(worker)
                        self.main_startup()

            except Exception as e:
                print(e)
                self.errorLbl.setStyleSheet("color: red;")
                self.errorLbl.setText("Server error - Server may be down.")
        else:
            self.errorLbl.setStyleSheet("color: red;")
            self.errorLbl.setText("One or more fields are blank.")
