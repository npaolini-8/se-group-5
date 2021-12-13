# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_windowtCkSQI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 600)
        LoginWindow.setStyleSheet(u"background-color: #295B63;\n"
"\n"
"\n"
"")
        self.verticalLayoutWidget = QWidget(LoginWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 50, 591, 476))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLbl = QLabel(self.verticalLayoutWidget)
        self.titleLbl.setObjectName(u"titleLbl")
        font = QFont()
        font.setFamilies([u"Serif"])
        font.setPointSize(20)
        self.titleLbl.setFont(font)
        self.titleLbl.setStyleSheet(u"color: #B6E3F0;")
        self.titleLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLbl)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.userName = QLineEdit(self.verticalLayoutWidget)
        self.userName.setObjectName(u"userName")
        self.userName.setMinimumSize(QSize(0, 30))
        self.userName.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Serif"])
        self.userName.setFont(font1)
        self.userName.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"border-radius: 8px;\n"
"font-size: 12px;")

        self.verticalLayout.addWidget(self.userName)

        self.passWord = QLineEdit(self.verticalLayoutWidget)
        self.passWord.setObjectName(u"passWord")
        self.passWord.setMinimumSize(QSize(0, 30))
        self.passWord.setFont(font1)
        self.passWord.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"border-radius: 8px;\n"
"font-size: 12px;")
        self.passWord.setEchoMode(QLineEdit.Password)
        self.passWord.setReadOnly(False)

        self.verticalLayout.addWidget(self.passWord)

        self.loginBtn = QPushButton(self.verticalLayoutWidget)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(0, 80))
        font2 = QFont()
        font2.setFamilies([u"Serif"])
        font2.setPointSize(26)
        font2.setItalic(False)
        self.loginBtn.setFont(font2)
        self.loginBtn.setStyleSheet(u"color: #B6E3F0;\n"
"")

        self.verticalLayout.addWidget(self.loginBtn)

        self.errorLbl = QLabel(self.verticalLayoutWidget)
        self.errorLbl.setObjectName(u"errorLbl")
        self.errorLbl.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setPointSize(14)
        self.errorLbl.setFont(font3)
        self.errorLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.errorLbl)


        self.retranslateUi(LoginWindow)

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





from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QDialog


#Login gui
class LoginWindow(QDialog):
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
        self.move((geometry.width() - self.geometry().width()) / 2, (geometry.height() - self.geometry().height()) / 2)
        self.reset_mode = False
        self.one_pw_entered = False
        self.temp_pw = ""
        self.reset_fail_count = 0

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
    # def load_animation(self):
    #     self.ui.errorLbl.setStyleSheet("color: green;")
    #     sleep(0.15)
    #     self.ui.errorLbl.setText("User found.  Logging in..")
    #     sleep(0.15)
    #     self.ui.errorLbl.setText("User found.  Logging in...")
    #     sleep(0.15)
    #     self.ui.errorLbl.setText("User found.  Logging in....")
    #     sleep(0.15)
    #     self.ui.errorLbl.setText("User found.  Logging in.....")
    #     sleep(0.15)
    #     self.ui.errorLbl.setText("User found.  Logging in......")
    #     sleep(0.15)

    def main_startup(self):
        self.ui.errorLbl.setText("")
        self.warehouse_controller.switch_to(self, 'main')

    def set_error(self, error, is_good):
        self.ui.errorLbl.setText(error)
        if is_good:
            self.ui.errorLbl.setStyleSheet("color: green;")
        else:
            self.ui.errorLbl.setStyleSheet("color: red;")

    def valid_pw( self,password ):
        if len(password) >= 8 and len(password) <= 30:
            return True
        else:
            return False

    def try_to_login(self):
        valid = not (len(self.ui.userName.text()) == 0 or len(self.ui.passWord.text()) == 0)

        if valid:  #If username and password fields aren't empty
            try:
                if self.warehouse_controller.check_none_password(self.ui.userName.text()): #password reset mode
                    if not(self.reset_mode):
                        self.reset_mode = True
                        self.set_error("Account flagged for password reset, please enter new password", True)
                        self.ui.passWord.setText("")
                        self.ui.passWord.setFocus()
                        #self.ui.userName.setReadOnly(True)
                    elif self.reset_mode and not(self.one_pw_entered): #need to enter valid password
                        if self.valid_pw(self.ui.passWord.text()): #new pw OK
                            self.temp_pw = self.ui.passWord.text()
                            self.one_pw_entered = True
                            self.set_error("Please re-enter new password", True)
                            self.ui.passWord.setText("")
                            self.ui.passWord.setFocus()
                        else: #pw did not meet reqs
                            self.set_error("Please enter a valid password", False)
                            self.ui.passWord.setText("")
                            self.ui.passWord.setFocus()
                    elif self.reset_mode and self.one_pw_entered: #need to enter password again
                        if self.ui.passWord.text() == self.temp_pw: #second pw accepted
                            self.set_error("New password accepted", True)

                            user = self.warehouse_controller.find_user(self.ui.userName.text())
                            self.warehouse_controller.set_current_user(user)
                            self.warehouse_controller.clear_user_lock(user["Username"])

                            self.warehouse_controller.set_new_pw(self.ui.userName.text(), password=self.temp_pw)

                            self.ui.userName.setReadOnly(False)
                            self.reset_mode = False
                            self.one_pw_entered = False
                            self.temp_pw = ""
                            self.reset_fail_count = 0
                            self.main_startup()
                        elif self.reset_fail_count >= 5: #safegaurd in case they forget first pw
                            self.set_error("Too many failures, restarting password reset- Please enter a new Password", False)
                            self.reset_fail_count = 0
                            self.one_pw_entered = False
                            self.ui.passWord.setText("")
                            self.ui.userName.setFocus()
                        else: #second pw does not match first
                            self.set_error("Please enter the same password again", False)
                            self.reset_fail_count += 1
                            self.ui.passWord.setText("")
                            self.ui.passWord.setFocus()


                else:
                    user = self.warehouse_controller.connect_user(self.ui.userName.text(), self.ui.passWord.text())  #Will cause exception if server is not connected -- will return None if no user with those credentials

                    if user == None:  #If user + password doesn't exist
                        self.warehouse_controller.increment_user_lock(self.ui.userName.text())
                        self.ui.errorLbl.setStyleSheet("color: red;")
                        self.ui.errorLbl.setText(f"Invalid login credentials.\nPlease try again.")


                        self.ui.userName.setFocus()


                    else:
                        if self.warehouse_controller.get_user_lock(self.ui.userName.text()) >= 3:
                            self.ui.errorLbl.setStyleSheet("color: red;")
                            self.ui.errorLbl.setText(f"Account is currently locked.\nPlease contact an administrator.")
                            self.ui.userName.setFocus()
                        else:
                            self.ui.errorLbl.setStyleSheet("color: green;")
                            self.ui.errorLbl.setText("User found.  Logging in.")
                            self.warehouse_controller.set_current_user(user)
                            self.warehouse_controller.clear_user_lock(user["Username"])
                            self.ui.userName.setFocus()
                            #Thread an animation to run before closing the login gui and opening main gui
                            #worker = Worker(self.load_animation)
                            #worker.signals.finished.connect(self.main_startup)
                            #self.threadpool.start(worker)
                            self.main_startup()
            except Exception as e:
                #print(e)
                self.ui.errorLbl.setStyleSheet("color: red;")
                self.ui.errorLbl.setText("Server error - Server may be down.")
                self.ui.userName.setFocus()
        else:
            if self.reset_mode:
                self.set_error("Please enter a new password", False)
                self.ui.passWord.setFocus()
            else:
                self.ui.errorLbl.setStyleSheet("color: red;")
                self.ui.errorLbl.setText("One or more fields are blank.")
                self.ui.userName.setFocus()

    def clear_input(self):
        self.ui.userName.setText("")
        self.ui.passWord.setText("")
        self.ui.errorLbl.setText("")
        self.ui.userName.setFocus()
