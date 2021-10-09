import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QLineEdit,
QDockWidget, QCheckBox, QVBoxLayout, QWidget, QPushButton, QLabel, QSizePolicy)
from PySide6.QtCore import Qt
from pymongo import MongoClient
import ssl

#user -- softgod1
#password -- banana123

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window_props()
        self.init_widgets()

    def init_window_props(self):
        self.setWindowTitle('Inventory Management Extreme Edition')
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

    def try_to_login(self):
        valid = not (len(self.userName.text()) == 0 or len(self.passWord.text()) == 0)
        if valid:
            client = MongoClient("mongodb+srv://softgod1:banana123@group5warehouse.kvdys.mongodb.net/test",
                                    ssl_cert_reqs=ssl.CERT_NONE, serverSelectionTimeoutMS=1000)
            try:
                client.server_info()
                db = client.warehouse
                users = db.users
                user = users.find_one({"_id": self.userName.text(),"Password": self.passWord.text()})  #BretC1, bananafish6
                if user == None:
                    self.errorLbl.setStyleSheet("color: red;")
                    self.errorLbl.setText("INVALID LOGIN CREDENTIALS\nPLEASE TRY AGAIN")
                else:
                    self.errorLbl.setStyleSheet("color: green;")
                    self.errorLbl.setText("User found.  Logging in...")
                    self.main_startup(client, user)
            except Exception as e:
                print(e)
                self.errorLbl.setStyleSheet("color: red;")
                self.errorLbl.setText("SERVER ERROR -- SERVER MAY BE DOWN")
        else:
            self.errorLbl.setStyleSheet("color: red;")
            self.errorLbl.setText("ONE OR MORE FIELDS ARE BLANK")

    def main_startup(self, client, user):
        print("NICE")


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
