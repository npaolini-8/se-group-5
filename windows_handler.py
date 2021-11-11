import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt6.uic import loadUi
from database_funcs import Warehouse

warehouse = Warehouse()

class LoginWindow(QDialog):
    def __init__(self, warehouse):
        super(LoginWindow, self).__init__()
        self.ui = loadUi("login_window.ui", self)
        self.login_btn.clicked.connect(self.try_to_login)
        self.warehouse = warehouse

    def try_to_login(self):
        valid = not (len(self.username_line.text()) == 0 or len(self.password_line.text()) == 0)
        if valid:  #If username and password fields aren't empty
            #try:
            client = self.warehouse.cluster
            client.server_info()  #This will fail if we don't have a connection to the server
            users = self.warehouse.users_collection
            self.user = users.find_one({"Username": self.username_line.text(),"Password": self.password_line.text()}) #BretC1, bananafish6
                #if self.user == None:  #If user + password doesn't exist
                    #self.errorLbl.setStyleSheet("color: red;")
                    #self.errorLbl.setText("Invalid login credentials.\nPlease try again.")
                #else:
                    #self.errorLbl.setStyleSheet("color: green;")
                    #self.errorLbl.setText("User found.  Logging in.")
            loginwindow.hide()
            mainwindow.show()


            #except Exception as e:
            #    print(e)
            #    self.errorLbl.setStyleSheet("color: red;")
            #    self.errorLbl.setText("Server error - Server may be down.")
        #else:
        #    self.errorLbl.setStyleSheet("color: red;")
        #    self.errorLbl.setText("One or more fields are blank.")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = loadUi("main_window.ui", self)

class OrdersWindow(QDialog):
    def __init__(self):
        super(OrdersWindow, self).__init__()
        self.ui = loadUi("orders_window.ui", self)

class ItemsWindow(QDialog):
    def __init__(self):
        super(ItemsWindow, self).__init__()
        self.ui = loadUi("items_window.ui", self)


app = QApplication(sys.argv)
loginwindow = LoginWindow(warehouse)
mainwindow = MainWindow()
orderswindow = OrdersWindow()
itemswindow = ItemsWindow()

widget = QtWidgets.QStackedWidget()
widget.addWidget(loginwindow)
widget.addWidget(mainwindow)
widget.addWidget(orderswindow)
widget.addWidget(itemswindow)

widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
app.exec()