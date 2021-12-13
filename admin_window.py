from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_windowwXcNks.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AdminWindow.sizePolicy().hasHeightForWidth())
        AdminWindow.setSizePolicy(sizePolicy)
        AdminWindow.setStyleSheet(u"background-color: #295B63;")
        self.return_btn = QPushButton(AdminWindow)
        self.return_btn.setObjectName(u"return_btn")
        self.return_btn.setGeometry(QRect(20, 10, 75, 24))
        self.return_btn.setStyleSheet(u"color: #B6E3F0;")
        self.verticalLayoutWidget = QWidget(AdminWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(350, 100, 281, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.curr_user_label = QLabel(self.verticalLayoutWidget)
        self.curr_user_label.setObjectName(u"curr_user_label")
        self.curr_user_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.curr_user_label)

        self.user_name_line = QLineEdit(self.verticalLayoutWidget)
        self.user_name_line.setObjectName(u"user_name_line")
        self.user_name_line.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"border-radius: 10px;\n"
"font-size: 12px;")

        self.verticalLayout.addWidget(self.user_name_line)

        self.password_line = QLineEdit(self.verticalLayoutWidget)
        self.password_line.setObjectName(u"password_line")
        self.password_line.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"border-radius: 10px;\n"
"font-size: 12px;")

        self.verticalLayout.addWidget(self.password_line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.user_radio = QRadioButton(self.verticalLayoutWidget)
        self.user_radio.setObjectName(u"user_radio")
        self.user_radio.setStyleSheet(u"color: #B6E3F0;")

        self.horizontalLayout.addWidget(self.user_radio)

        self.super_radio = QRadioButton(self.verticalLayoutWidget)
        self.super_radio.setObjectName(u"super_radio")
        self.super_radio.setStyleSheet(u"color: #B6E3F0;")

        self.horizontalLayout.addWidget(self.super_radio)

        self.admin_radio = QRadioButton(self.verticalLayoutWidget)
        self.admin_radio.setObjectName(u"admin_radio")
        self.admin_radio.setStyleSheet(u"color: #B6E3F0;")

        self.horizontalLayout.addWidget(self.admin_radio)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.active_check = QCheckBox(self.verticalLayoutWidget)
        self.active_check.setObjectName(u"active_check")
        self.active_check.setStyleSheet(u"color: #B6E3F0;")

        self.horizontalLayout_2.addWidget(self.active_check)

        self.lock_check = QCheckBox(self.verticalLayoutWidget)
        self.lock_check.setObjectName(u"lock_check")
        self.lock_check.setStyleSheet(u"color: #B6E3F0;")

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
        self.save_user_button.setStyleSheet(u"color: #B6E3F0;")

        self.verticalLayout.addWidget(self.save_user_button)

        self.verticalLayoutWidget_2 = QWidget(AdminWindow)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 100, 331, 321))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.new_user_button = QPushButton(self.verticalLayoutWidget_2)
        self.new_user_button.setObjectName(u"new_user_button")
        self.new_user_button.setStyleSheet(u"color: #B6E3F0;")

        self.verticalLayout_2.addWidget(self.new_user_button)

        self.user_search_bar = QLineEdit(self.verticalLayoutWidget_2)
        self.user_search_bar.setObjectName(u"user_search_bar")
        self.user_search_bar.setStyleSheet(u"background-color: #4395a3;\n"
"color: white;\n"
"\n"
"font-size: 12px;")

        self.verticalLayout_2.addWidget(self.user_search_bar)

        self.users_table = QTableWidget(self.verticalLayoutWidget_2)
        self.users_table.setObjectName(u"users_table")
        self.users_table.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"border-radius: 10px;\n"
"font-size: 12px;")

        self.verticalLayout_2.addWidget(self.users_table)

        self.verticalLayoutWidget_3 = QWidget(AdminWindow)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 440, 781, 80))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.db_fxn_lbl = QLabel(self.verticalLayoutWidget_3)
        self.db_fxn_lbl.setObjectName(u"db_fxn_lbl")
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.db_fxn_lbl.setFont(font)
        self.db_fxn_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.db_fxn_lbl)

        self.db_bu_buttons = QHBoxLayout()
        self.db_bu_buttons.setObjectName(u"db_bu_buttons")
        self.bu_create_btn = QPushButton(self.verticalLayoutWidget_3)
        self.bu_create_btn.setObjectName(u"bu_create_btn")
        self.bu_create_btn.setStyleSheet(u"color: #B6E3F0;")

        self.db_bu_buttons.addWidget(self.bu_create_btn)

        self.restore_items_btn = QPushButton(self.verticalLayoutWidget_3)
        self.restore_items_btn.setObjectName(u"restore_items_btn")
        self.restore_items_btn.setStyleSheet(u"color: #B6E3F0;")

        self.db_bu_buttons.addWidget(self.restore_items_btn)

        self.restore_users_btn = QPushButton(self.verticalLayoutWidget_3)
        self.restore_users_btn.setObjectName(u"restore_users_btn")
        self.restore_users_btn.setStyleSheet(u"color: #B6E3F0;")

        self.db_bu_buttons.addWidget(self.restore_users_btn)

        self.restore_orders_btn = QPushButton(self.verticalLayoutWidget_3)
        self.restore_orders_btn.setObjectName(u"restore_orders_btn")
        self.restore_orders_btn.setStyleSheet(u"color: #B6E3F0;")

        self.db_bu_buttons.addWidget(self.restore_orders_btn)

        self.restore_orders_history_btn = QPushButton(self.verticalLayoutWidget_3)
        self.restore_orders_history_btn.setObjectName(u"restore_orders_history_btn")
        self.restore_orders_history_btn.setStyleSheet(u"color: #B6E3F0;")

        self.db_bu_buttons.addWidget(self.restore_orders_history_btn)


        self.verticalLayout_3.addLayout(self.db_bu_buttons)


        self.retranslateUi(AdminWindow)

        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"Admin Panel", None))
        self.return_btn.setText(QCoreApplication.translate("AdminWindow", u"Return", None))
        self.curr_user_label.setText(QCoreApplication.translate("AdminWindow", u"Creating a New User", None))
        self.user_name_line.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"Username", None))
        self.password_line.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"Password", None))
        self.user_radio.setText(QCoreApplication.translate("AdminWindow", u"User", None))
        self.super_radio.setText(QCoreApplication.translate("AdminWindow", u"Supervisor", None))
        self.admin_radio.setText(QCoreApplication.translate("AdminWindow", u"Admin", None))
        self.active_check.setText(QCoreApplication.translate("AdminWindow", u"Is Active?", None))
        self.lock_check.setText(QCoreApplication.translate("AdminWindow", u"Is Locked?", None))
        self.err_label.setText("")
        self.save_user_button.setText(QCoreApplication.translate("AdminWindow", u"Save User", None))
        self.new_user_button.setText(QCoreApplication.translate("AdminWindow", u"Create a New User", None))
        self.user_search_bar.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"Search for a user...", None))
        self.db_fxn_lbl.setText(QCoreApplication.translate("AdminWindow", u"Database Backup and Restore", None))
        self.bu_create_btn.setText(QCoreApplication.translate("AdminWindow", u"Create Backup", None))
        self.restore_items_btn.setText(QCoreApplication.translate("AdminWindow", u"Restore Items", None))
        self.restore_users_btn.setText(QCoreApplication.translate("AdminWindow", u"Restore Users", None))
        self.restore_orders_btn.setText(QCoreApplication.translate("AdminWindow", u"Restore Orders", None))
        self.restore_orders_history_btn.setText(QCoreApplication.translate("AdminWindow", u"Restore Orders History", None))
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

        self.ui.users_table.verticalHeader().setVisible(False)
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
        self.ui.bu_create_btn.clicked.connect(self.create_backups)
        self.ui.restore_items_btn.clicked.connect(self.warehouse_controller.restore_items)
        self.ui.restore_users_btn.clicked.connect(self.warehouse_controller.restore_users)
        self.ui.restore_orders_btn.clicked.connect(self.warehouse_controller.restore_orders)
        self.ui.restore_orders_history_btn.clicked.connect(self.warehouse_controller.restore_orders_history)

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
        self.set_error("",True)

    #"" represents new user account
    def create_new_clicked(self):
        self.curr_user = ""
        self.ui.curr_user_label.setText("Creating a New User")
        self.ui.user_name_line.setText("")
        self.ui.user_radio.setChecked(True)
        self.ui.active_check.setChecked(True)
        self.ui.lock_check.setChecked(False)
        self.ui.user_name_line.setFocus()
        self.set_error("",True)

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

    def set_error(self,error, good):
        self.ui.err_label.setText(error)
        if good:
            self.ui.err_label.setStyleSheet("color: green;")
        else:
            self.ui.err_label.setStyleSheet("color: red;")

    def save_user(self):

        username = self.ui.user_name_line.text()
        password = self.ui.password_line.text()
        role = self.role_check()
        locked = self.ui.lock_check.isChecked()
        active = self.ui.active_check.isChecked()

        if role is None:
            self.set_error("Role Required",False)
        elif username is None or username == "":
            self.set_error("Username required",False)
        elif self.curr_user == "": #new user case
            if self.warehouse_controller.validate_new_username( username ) != "OK":
                self.set_error("Username in use",False)
            #elif password is None or password == "": #removing for now, setting pw to None
            #    self.set_error("Password required")
            else: #valid new user input
                self.warehouse_controller.create_new_user(username,password,role)
                self.clear_form()
                self.refresh_form()
                self.set_error("New User Created",True)
        else: #updating existing user passing empty strings for PWs
            if username != self.curr_user: #changing username
                if self.warehouse_controller.validate_new_username( username ) != "OK":
                    self.set_error("Username in use",False)
                else: #valid username change
                    self.warehouse_controller.edit_user(self.curr_user, password=password,role=role,newUsername=username,active=active,locked=locked)
                    self.clear_form()
                    self.set_error(self.curr_user + " updated to new username: " + username,True)
                    self.refresh_form()

            else: #updating user, username staying the same
                self.warehouse_controller.edit_user(self.curr_user, password=password,role=role,active=active,locked=locked)
                self.clear_form()
                self.set_error(self.curr_user + " updated",True)
                self.refresh_form()

    def create_backups(self):
        self.warehouse_controller.create_backup()
