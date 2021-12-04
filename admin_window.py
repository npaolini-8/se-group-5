
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QHeaderView, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QAbstractItemView, QLabel)

class Ui_AdminWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.return_btn = QPushButton(Dialog)
        self.return_btn.setObjectName(u"return_btn")
        self.return_btn.setGeometry(QRect(20, 10, 75, 24))
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(350, 110, 281, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.curr_user_label = QLabel(self.verticalLayoutWidget)
        self.curr_user_label.setObjectName(u"curr_user_label")

        self.verticalLayout.addWidget(self.curr_user_label)

        self.user_name_line = QLineEdit(self.verticalLayoutWidget)
        self.user_name_line.setObjectName(u"user_name_line")

        self.verticalLayout.addWidget(self.user_name_line)

        self.password_line = QLineEdit(self.verticalLayoutWidget)
        self.password_line.setObjectName(u"password_line")

        self.verticalLayout.addWidget(self.password_line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.user_radio = QRadioButton(self.verticalLayoutWidget)
        self.user_radio.setObjectName(u"user_radio")

        self.horizontalLayout.addWidget(self.user_radio)

        self.super_radio = QRadioButton(self.verticalLayoutWidget)
        self.super_radio.setObjectName(u"super_radio")

        self.horizontalLayout.addWidget(self.super_radio)

        self.admin_radio = QRadioButton(self.verticalLayoutWidget)
        self.admin_radio.setObjectName(u"admin_radio")

        self.horizontalLayout.addWidget(self.admin_radio)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.active_check = QCheckBox(self.verticalLayoutWidget)
        self.active_check.setObjectName(u"active_check")

        self.horizontalLayout_2.addWidget(self.active_check)

        self.lock_check = QCheckBox(self.verticalLayoutWidget)
        self.lock_check.setObjectName(u"lock_check")

        self.horizontalLayout_2.addWidget(self.lock_check)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.err_label = QLabel(self.verticalLayoutWidget)
        self.err_label.setObjectName(u"err_label")
        self.err_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.err_label)

        self.save_user_button = QPushButton(self.verticalLayoutWidget)
        self.save_user_button.setObjectName(u"save_user_button")

        self.verticalLayout.addWidget(self.save_user_button)

        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 100, 331, 321))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.new_user_button = QPushButton(self.verticalLayoutWidget_2)
        self.new_user_button.setObjectName(u"new_user_button")

        self.verticalLayout_2.addWidget(self.new_user_button)

        self.user_search_bar = QLineEdit(self.verticalLayoutWidget_2)
        self.user_search_bar.setObjectName(u"user_search_bar")

        self.verticalLayout_2.addWidget(self.user_search_bar)

        self.users_table = QTableWidget(self.verticalLayoutWidget_2)
        self.users_table.setObjectName(u"users_table")

        self.verticalLayout_2.addWidget(self.users_table)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Admin Panel", None))
        self.return_btn.setText(QCoreApplication.translate("Dialog", u"Return", None))
        self.curr_user_label.setText(QCoreApplication.translate("Dialog", u"Creating a New User", None))
        self.user_name_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Username", None))
        self.password_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.user_radio.setText(QCoreApplication.translate("Dialog", u"User", None))
        self.super_radio.setText(QCoreApplication.translate("Dialog", u"Supervisor", None))
        self.admin_radio.setText(QCoreApplication.translate("Dialog", u"Admin", None))
        self.active_check.setText(QCoreApplication.translate("Dialog", u"Is Active?", None))
        self.lock_check.setText(QCoreApplication.translate("Dialog", u"Is Locked?", None))
        self.err_label.setText("")
        self.save_user_button.setText(QCoreApplication.translate("Dialog", u"Save User", None))
        self.new_user_button.setText(QCoreApplication.translate("Dialog", u"Create a New User", None))
        self.user_search_bar.setPlaceholderText(QCoreApplication.translate("Dialog", u"Search for a user...", None))
    # retranslateUi



class AdminWindow(QDialog):
    def __init__(self, warehouse_controller):
        super(AdminWindow, self).__init__()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)
        self.warehouse_controller = warehouse_controller
        self.init_buttons()
        self.init_table()
        self.center_on_screen()
        self.ui.user_search_bar.textChanged.connect(self.filter_users)
        self.ui.users_table.clicked.connect(self.select_user)
        self.ui.active_check.setChecked(True)
        
    #loads table with user info, fetched by refresh_users
    def init_table(self):
        self.ui.users_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.users_table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.ui.users_table.setColumnCount(4)
        self.ui.users_table.setHorizontalHeaderLabels(["Username", "Active?","Locked?", "Role"])
        header = self.ui.users_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        self.refresh_table()

        # self.ui.users_table.setRowCount( len(self.users) )

        # i = 0
        # for user in self.users:
        #     name_item = QTableWidgetItem(user["Username"])
        #     active_item = QTableWidgetItem(str(user["isActive"]))
        #     lock_item = QTableWidgetItem(str(user["isLocked"]))
        #     role_item = QTableWidgetItem(user["Role"])

        #     self.ui.users_table.setItem(i, 0, name_item)
        #     self.ui.users_table.setItem(i, 1, active_item)
        #     self.ui.users_table.setItem(i, 2, lock_item)
        #     self.ui.users_table.setItem(i, 3, role_item)

        #     i+=1
    
    def refresh_table(self):
        self.refresh_users()
        self.ui.users_table.setRowCount( len(self.users) )

        i = 0
        for user in self.users:
            name_item = QTableWidgetItem(user["Username"])
            active_item = QTableWidgetItem(str(user["isActive"]))
            lock_item = QTableWidgetItem(str(user["isLocked"]))
            role_item = QTableWidgetItem(user["Role"])

            name_item.setFlags(name_item.flags() ^ Qt.ItemIsEditable)
            active_item.setFlags(active_item.flags() ^ Qt.ItemIsEditable)
            lock_item.setFlags(lock_item.flags() ^ Qt.ItemIsEditable)
            role_item.setFlags(role_item.flags() ^ Qt.ItemIsEditable)

            self.ui.users_table.setItem(i, 0, name_item)
            self.ui.users_table.setItem(i, 1, active_item)
            self.ui.users_table.setItem(i, 2, lock_item)
            self.ui.users_table.setItem(i, 3, role_item)

            i+=1

    def init_buttons(self):
        self.ui.return_btn.clicked.connect(self.return_clicked)
        self.ui.new_user_button.clicked.connect(self.create_new_clicked)
        self.ui.save_user_button.clicked.connect(self.save_user)

    def return_clicked(self):
        self.warehouse_controller.switch_to(self, 'main')
    #loads list of warehouse users
    #curr_user represents user account currently being edited
    def refresh_users(self):
        self.users = self.warehouse_controller.get_users()
        self.curr_user = ""

    def refresh_form(self):
        self.refresh_users()
        self.refresh_table()
        self.ui.curr_user_label.setText("Creating a New User")

    def center_on_screen(self):
        geometry = self.screen().availableGeometry()
        self.move((geometry.width() - self.geometry().width()) / 2, (geometry.height() - self.geometry().height()) / 2)

    def clear_form(self):
        self.ui.user_name_line.setText("")
        self.ui.password_line.setText("")
        self.ui.user_radio.setChecked(False)
        self.ui.super_radio.setChecked(False)
        self.ui.admin_radio.setChecked(False)
        self.ui.active_check.setChecked(True)
        self.ui.lock_check.setChecked(False)
        self.set_error("")

    #"" represents new user account
    def create_new_clicked(self):
        self.curr_user = ""
        self.ui.curr_user_label.setText("Creating a New User")
        self.ui.user_name_line.setText("")
        self.ui.user_radio.setChecked(True)
        self.ui.active_check.setChecked(True)
        self.ui.lock_check.setChecked(False)
        self.ui.user_name_line.setFocus()
        self.set_error("")

    def filter_users(self):
        filter_string = self.ui.user_search_bar.text()
        for row in range(self.ui.users_table.rowCount()):
            if filter_string.lower() in self.ui.users_table.item(row,0).text().lower():
                filtered = False
            else:
                filtered = True
            self.ui.users_table.setRowHidden(row, filtered)

    def select_user(self,item):
        row = item.row()
        
        user = self.ui.users_table.item(row,0).text()
        self.curr_user = user
        self.ui.user_name_line.setText(user)
        self.ui.curr_user_label.setText("Editing: " + user)
        
        self.ui.password_line.setText(None)

        active = self.ui.users_table.item(row, 1).text()
        if active == "True":
            active = True
        else:
            active = False

        locked = self.ui.users_table.item(row, 2).text()
        if locked == "True":
            locked = True
        else:
            locked = False
        
        self.ui.active_check.setChecked(active)
        self.ui.lock_check.setChecked(locked)

        role = self.ui.users_table.item(row, 3).text()
        if role == "User":
            self.ui.user_radio.setChecked(True)
        elif role == "Supervisor":
            self.ui.super_radio.setChecked(True)
        elif role == "Admin":
            self.ui.admin_radio.setChecked(True)
        
        self.ui.password_line.setFocus()

    def role_check(self):
        role = None

        if self.ui.user_radio.isChecked():
            role = "User"
        elif self.ui.super_radio.isChecked():
            role = "Supervisor"
        elif self.ui.admin_radio.isChecked():
            role = "Admin"

        return role
    
    def set_error(self,error):
        self.ui.err_label.setText(error)

    def save_user(self):

        username = self.ui.user_name_line.text()
        password = self.ui.password_line.text()
        role = self.role_check()
        locked = self.ui.lock_check.isChecked()
        active = self.ui.active_check.isChecked()

        if role is None:
            self.set_error("Role Required")
        elif username is None or username == "":
            self.set_error("Username required")
        elif self.curr_user == "": #new user case
            if password is None or password == "":
                self.set_error("Password required")
            elif self.warehouse_controller.validate_new_username( username ) != "OK":
                self.set_error("Username in use")
            else: #valid new user input
                self.warehouse_controller.create_new_user(username,password,role)
                self.clear_form()
                self.refresh_form()
                self.set_error("New User Created")
        else: #updating existing user
            if username != self.curr_user: #changing username
                if self.warehouse_controller.validate_new_username( username ) != "OK":
                    self.set_error("Username in use")
                else: #valid username change
                    self.warehouse_controller.edit_user(self.curr_user, password=password,role=role,newUsername=username,active=active,locked=locked)
                    self.clear_form()
                    self.set_error(self.curr_user + " updated to new username: " + username)
                    self.refresh_form()
                    
            else: #updating user, username staying the same
                self.warehouse_controller.edit_user(self.curr_user, password=password,role=role,active=active,locked=locked)
                self.clear_form()
                self.set_error(self.curr_user + " updated")
                self.refresh_form()
                
