import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()

        self.window.setWindowTitle("Welcome To WareHouse")
        self.window.setGeometry(500,100,350,600)

        self.image_path = "login.jpg"

        self.lable_image = self.createLable(75,28,200,200)

        

        
        

        self.initGui()
        self.window.setStyleSheet("background-color:#32a852")

        self.window.show()

        sys.exit(app.exec_())

    
    def initGui(self):
        self.displayImage()

        username = QtWidgets.QTextEdit(self.window)
        username.setGeometry(25, 270, 300, 40)
        username.setText('User Name')
        username.setStyleSheet("background-color:#cbd3d7; color:#8E8E8E;padding: 6px 2px;border: 1px solid #9dced4")

        password = QtWidgets.QTextEdit(self.window)
        password.setGeometry(25, 330, 300, 40)
        password.setText('Password')
        password.setStyleSheet("background-color:#cbd3d7; color:#8E8E8E;padding: 6px 2px;border: 1px solid #9dced4")

        
        login_btn=QtWidgets.QPushButton(self.window)
        login_btn.setGeometry(25, 400, 300, 40)
        login_btn.setText("Login")
        login_btn.setStyleSheet("background-color:#9dced4;color:#2E2E2E;border:2px solid #9dced4")

    def displayImage(self):
        image=QtGui.QImage(self.image_path)
        display_image= QtGui.QPixmap.fromImage(image)

        self.lable_image.setPixmap(display_image)
        self.lable_image.setScaledContents(True)

    def createLable(self, left, top, width, height):
        created_label = QtWidgets.QLabel(self.window)
        created_label.setGeometry(left, top, width, height)
        created_label.setStyleSheet("border: 1 solid #9dced4;background-color: #4e4e4e")

        return created_label


main = MainWindow()
