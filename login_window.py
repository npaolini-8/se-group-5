from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QMainWindow,
    QWidget)


from time import sleep
from PySide6.QtCore import QThreadPool

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 600)
        self.verticalLayoutWidget = QWidget(LoginWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(130, 150, 511, 221))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLbl = QLabel(self.verticalLayoutWidget)
        self.titleLbl.setObjectName(u"titleLbl")
        self.titleLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLbl)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.userName = QLineEdit(self.verticalLayoutWidget)
        self.userName.setObjectName(u"userName")

        self.verticalLayout.addWidget(self.userName)

        self.passWord = QLineEdit(self.verticalLayoutWidget)
        self.passWord.setObjectName(u"passWord")
        self.passWord.setEchoMode(QLineEdit.Password)
        self.passWord.setReadOnly(False)

        self.verticalLayout.addWidget(self.passWord)

        self.loginBtn = QPushButton(self.verticalLayoutWidget)
        self.loginBtn.setObjectName(u"loginBtn")

        self.verticalLayout.addWidget(self.loginBtn)

        self.errorLbl = QLabel(self.verticalLayoutWidget)
        self.errorLbl.setObjectName(u"errorLbl")
        self.errorLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.errorLbl)


        self.retranslateUi(LoginWindow)

        self.loginBtn.setDefault(True)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"PyDepot Login", None))
        self.titleLbl.setText(QCoreApplication.translate("LoginWindow", u"PyDepot", None))
        self.userName.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Username...", None))
        self.passWord.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password...", None))
        self.loginBtn.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.errorLbl.setText("")
    # retranslateUi


#Login gui
class LoginWindow(QMainWindow):
    def __init__(self, warehouse_controller):
        super(LoginWindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.init_buttons()
        self.warehouse_controller = warehouse_controller
        #self.init_window_props()
        #self.init_widgets()
        self.threadpool = QThreadPool()
        geometry = self.screen().availableGeometry()
        self.dimensions = (geometry.width() * 0.35, geometry.height() * 0.35)
        self.setFixedSize(self.dimensions[0], self.dimensions[1])
        self.move((geometry.width() - self.dimensions[0]) / 2, (geometry.height() - self.dimensions[1]) / 2)

    def init_buttons(self):
        self.ui.loginBtn.clicked.connect(self.try_to_login)

    # def init_window_props(self):
    #     self.setWindowTitle('Warehouse System Login')
        

    #     #Set window width and heights as percentages of screen resolution
        
    #     self.setStyleSheet("background-color:#808000")

    #     #Center window on screen
        
       

    # def init_widgets(self):
    #     #Create and configure vertical layout
    #     layout = QVBoxLayout()
    #     layout.setContentsMargins(self.dimensions[0] * 0.3, self.dimensions[1] * 0.3,
    #                            self.dimensions[0] * 0.3, self.dimensions[1] * 0.3)

    #     #Username and Password LineEdits
    #     self.userName = QLineEdit()
    #     self.userName.setPlaceholderText("Enter Username")
    #     self.userName.setStyleSheet("background-color:#000000; color:#cbd3d7;padding: 6px 2px;border: 1px solid #cbd3d7")
    #     self.passWord = QLineEdit()
    #     self.passWord.setPlaceholderText("Enter Password")
    #     self.passWord.setStyleSheet("background-color:#000000; color:#cbd3d7;padding: 6px 2px;border: 1px solid #cbd3d7")
    #     self.passWord.setEchoMode(QLineEdit.Password)

    #     #Login button
        
    #     loginBtn = QPushButton("Login")
    #     loginBtn.setStyleSheet("background-color: #000000;color:#cbd3d7;border:2px solid #cbd3d7")
    #     loginBtn.clicked.connect(self.try_to_login)

    #     #Error label for failed attempts
    #     self.errorLbl = QLabel("")
    #     self.errorLbl.setMaximumHeight(50)
    #     self.errorLbl.setStyleSheet("color: red;")

    #     #Add all widgets to layout
    #     layout.addWidget(self.userName)
    #     layout.addWidget(self.passWord)
    #     layout.addWidget(loginBtn)
    #     layout.addWidget(self.errorLbl)

    #     #Use a QWidget to hold the layout and set it as centralWidget
    #     container = QWidget()
    #     container.setLayout(layout)
    #     self.setCentralWidget(container)

    #Just a cool little login text animation as a confirmation that you are logging in
    def load_animation(self):
        self.ui.errorLbl.setStyleSheet("color: green;")
        sleep(0.15)
        self.ui.errorLbl.setText("User found.  Logging in..")
        sleep(0.15)
        self.ui.errorLbl.setText("User found.  Logging in...")
        sleep(0.15)
        self.ui.errorLbl.setText("User found.  Logging in....")
        sleep(0.15)
        self.ui.errorLbl.setText("User found.  Logging in.....")
        sleep(0.15)
        self.ui.errorLbl.setText("User found.  Logging in......")
        sleep(0.15)

    def main_startup(self):
        self.ui.errorLbl.setText("")
        self.warehouse_controller.switch_to(self, 'main')

    def try_to_login(self):
        valid = not (len(self.ui.userName.text()) == 0 or len(self.ui.passWord.text()) == 0)
        
        if valid:  #If username and password fields aren't empty
            try:
                user = self.warehouse_controller.connect_user(self.ui.userName.text(), self.ui.passWord.text())  #Will cause exception if server is not connected -- will return None if no user with those credentials

                if user == None:  #If user + password doesn't exist
                    self.warehouse_controller.increment_user_lock(self.ui.userName.text())
                    self.ui.errorLbl.setStyleSheet("color: red;")
                    self.ui.errorLbl.setText(f"Invalid login credentials.\nPlease try again.")
                    
                else:
                    if self.warehouse_controller.get_user_lock(self.ui.userName.text()) >= 3:
                        self.ui.errorLbl.setStyleSheet("color: red;")
                        self.ui.errorLbl.setText(f"Account is currently locked.\nPlease contact an administrator.")
                    else:
                        self.ui.errorLbl.setStyleSheet("color: green;")
                        self.ui.errorLbl.setText("User found.  Logging in.")
                        self.warehouse_controller.set_current_user(user)
                        self.warehouse_controller.clear_user_lock(user["Username"])
                        #Thread an animation to run before closing the login gui and opening main gui
                        #worker = Worker(self.load_animation)
                        #worker.signals.finished.connect(self.main_startup)
                        #self.threadpool.start(worker)
                        self.main_startup()

            except Exception as e:
                #print(e)
                self.ui.errorLbl.setStyleSheet("color: red;")
                self.ui.errorLbl.setText("Server error - Server may be down.")
        else:
            self.ui.errorLbl.setStyleSheet("color: red;")
            self.ui.errorLbl.setText("One or more fields are blank.")
