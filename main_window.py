from PySide6.QtCore import Qt
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowhQcosH.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 590)
        MainWindow.setStyleSheet(u"background-color: #295B63;\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 50, 261, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.items_btn = QPushButton(self.verticalLayoutWidget)
        self.items_btn.setObjectName(u"items_btn")
        self.items_btn.setMinimumSize(QSize(0, 80))
        self.items_btn.setStyleSheet(u"color: #B6E3F0;\n"
"font-size: 12px;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.items_btn)

        self.create_order_btn = QPushButton(self.verticalLayoutWidget)
        self.create_order_btn.setObjectName(u"create_order_btn")
        self.create_order_btn.setMinimumSize(QSize(0, 80))
        self.create_order_btn.setStyleSheet(u"color: #B6E3F0;\n"
"font-size: 12px;\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.create_order_btn)

        self.process_order_btn = QPushButton(self.verticalLayoutWidget)
        self.process_order_btn.setObjectName(u"process_order_btn")
        self.process_order_btn.setMinimumSize(QSize(0, 80))
        self.process_order_btn.setStyleSheet(u"color: #B6E3F0;\n"
"font-size: 12px;")

        self.verticalLayout.addWidget(self.process_order_btn)

        self.admin_panel_btn = QPushButton(self.verticalLayoutWidget)
        self.admin_panel_btn.setObjectName(u"admin_panel_btn")
        self.admin_panel_btn.setMinimumSize(QSize(0, 80))
        self.admin_panel_btn.setStyleSheet(u"color: #B6E3F0;\n"
"font-size: 12px;")

        self.verticalLayout.addWidget(self.admin_panel_btn)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(290, 10, 491, 491))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #B6E3F0;\n"
"font-size: 12px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.incoming_orders_tbl = QTableWidget(self.verticalLayoutWidget_2)
        self.incoming_orders_tbl.setObjectName(u"incoming_orders_tbl")
        self.incoming_orders_tbl.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"border-radius: 10px;\n"
"font-size: 12px;")
        self.incoming_orders_tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.incoming_orders_tbl.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.incoming_orders_tbl)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #B6E3F0;\n"
"font-size: 12px;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.outgoing_orders_tbl = QTableWidget(self.verticalLayoutWidget_2)
        self.outgoing_orders_tbl.setObjectName(u"outgoing_orders_tbl")
        self.outgoing_orders_tbl.setStyleSheet(u"background-color: #526c75;\n"
"color: #B6E3F0;\n"
"border-radius: 10px;\n"
"font-size: 12px;")
        self.outgoing_orders_tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.outgoing_orders_tbl.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.outgoing_orders_tbl)

        self.logout_btn = QPushButton(self.centralwidget)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setGeometry(QRect(20, 10, 88, 34))
        self.logout_btn.setStyleSheet(u"color: #B6E3F0;\n"
"font-size: 12px;")
        self.user_lbl = QLabel(self.centralwidget)
        self.user_lbl.setObjectName(u"user_lbl")
        self.user_lbl.setGeometry(QRect(120, 20, 161, 21))
        font = QFont()
        font.setPointSize(11)
        self.user_lbl.setFont(font)
        self.error_lbl = QLabel(self.centralwidget)
        self.error_lbl.setObjectName(u"error_lbl")
        self.error_lbl.setGeometry(QRect(30, 510, 751, 41))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.error_lbl.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyDepot", None))
        self.items_btn.setText(QCoreApplication.translate("MainWindow", u"Items", None))
        self.create_order_btn.setText(QCoreApplication.translate("MainWindow", u"Create Order", None))
        self.process_order_btn.setText(QCoreApplication.translate("MainWindow", u"Process Order", None))
        self.admin_panel_btn.setText(QCoreApplication.translate("MainWindow", u"Admin Panel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Incoming Orders", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Outgoing Orders", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.user_lbl.setText("")
        self.error_lbl.setText("")
    # retranslateUi




class MainWindow(QMainWindow):
    def __init__(self, warehouse_controller):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.warehouse_controller = warehouse_controller
        self.init_buttons()
        self.init_tables()
        self.center_on_screen()
        self.ui.incoming_orders_tbl.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.outgoing_orders_tbl.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.user_lbl.setStyleSheet("color: green;")
        self.ui.error_lbl.setStyleSheet("color: red;")

    def set_error(self, msg):
        self.ui.error_lbl.setText(msg)

    def init_buttons(self):
        self.ui.logout_btn.clicked.connect(self.logout_clicked)
        self.ui.items_btn.clicked.connect(self.items_clicked)
        self.ui.create_order_btn.clicked.connect(self.create_order_clicked)
        self.ui.process_order_btn.clicked.connect(self.process_order_clicked)
        #self.ui.backup_btn.clicked.connect(self.backup_clicked)
        self.ui.admin_panel_btn.clicked.connect(self.admin_panel_clicked)

    def init_table(self, table, list):
        col_count = 0
        row_count = 0
        headers = []

        if len(list) > 0:
            col_count = len(list[0].keys())
            headers = list[0].keys()
            row_count = len(list)

        table.setColumnCount(col_count)
        table.setRowCount(row_count)
        table.verticalHeader().setVisible(False)
        table.setHorizontalHeaderLabels(headers)

        for i in range(len(list)):
            count = 0
            for key in list[i]:
                item = QTableWidgetItem(list[i][key].__str__())
                #item.setFlags(Qt.ItemIsDragEnabled)
                #item.setFlags(item.flags() != Qt.ItemIsEditable)
                table.setItem(i, count, item)
                count += 1

    def init_tables(self):
        #self.init_table(self.ui.incoming_orders_tbl, self.warehouse_controller.get_incoming_orders())
        #self.init_table(self.ui.outgoing_orders_tbl, self.warehouse_controller.get_outgoing_orders())

        self.ui.incoming_orders_tbl.setColumnCount(4)
        self.ui.outgoing_orders_tbl.setColumnCount(4)

        self.ui.incoming_orders_tbl.setHorizontalHeaderLabels(["Order ID", "Client", "Status", "Item Count"])
        self.ui.outgoing_orders_tbl.setHorizontalHeaderLabels(["Order ID", "Client", "Status", "Item Count"])

        header = self.ui.incoming_orders_tbl.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        header = self.ui.outgoing_orders_tbl.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)


        self.ui.incoming_orders_tbl.verticalHeader().setVisible(False)
        self.ui.outgoing_orders_tbl.verticalHeader().setVisible(False)

        self.refresh_tables()

    def refresh_tables(self):
        incoming = self.warehouse_controller.get_incoming_orders_raw()
        outgoing = self.warehouse_controller.get_outgoing_orders_raw()

        self.load_table(self.ui.incoming_orders_tbl, incoming)
        self.load_table(self.ui.outgoing_orders_tbl, outgoing)

    def load_table(self, table:QTableWidget, order_list:list):
        table.setRowCount(len(order_list))

        i = 0
        for list_item in order_list:
            id_item = QTableWidgetItem(list_item["_id"].__str__())
            client_item = QTableWidgetItem(list_item["Client"])
            status_item = QTableWidgetItem(list_item["Status"])

            sum = 0
            for item in list_item["Order Items"]:
                sum += item["Count"]

            count_item = QTableWidgetItem(str(sum))

            id_item.setFlags(id_item.flags() ^ Qt.ItemIsEditable)
            client_item.setFlags(client_item.flags() ^ Qt.ItemIsEditable)
            status_item.setFlags(status_item.flags() ^ Qt.ItemIsEditable)
            count_item.setFlags(count_item.flags() ^ Qt.ItemIsEditable)

            table.setItem(i,0,id_item)
            table.setItem(i,1,client_item)
            table.setItem(i,2,status_item)
            table.setItem(i,3,count_item)

            i += 1



    def logout_clicked(self):
        self.warehouse_controller.reinstantiate_application()
        self.warehouse_controller.switch_to(self, 'login')

    def items_clicked(self):
        self.warehouse_controller.switch_to(self, 'items')

    def create_order_clicked(self):
        if self.warehouse_controller.access_check("Supervisor"):
            self.warehouse_controller.switch_to(self, 'create_order')
        else:
            self.set_error('Current user does not have Supervisor access')

    def process_order_clicked(self):
        self.warehouse_controller.switch_to(self, 'process_order')
        current_row = self.ui.outgoing_orders_tbl.currentRow()
        if current_row >= 0:
            print(self.ui.outgoing_orders_tbl.item(current_row, 0).text())

    # def backup_clicked(self):
    #     self.warehouse_controller.switch_to(self, 'backup')

    def admin_panel_clicked(self):
        if self.warehouse_controller.get_current_role() == "Admin":
            self.warehouse_controller.switch_to(self, 'admin_window')
        else:
            self.set_error('Current user does not have Admin access')


    def center_on_screen(self):
        geometry = self.screen().availableGeometry()
        self.move((geometry.width() - self.geometry().width()) / 2, (geometry.height() - self.geometry().height()) / 2)

    def refresh_incoming_orders(self):
        self.ui.incoming_orders_tbl.clearContents()

    def refresh_outgoing_orders(self):
        self.ui.outgoing_orders_tbl.clearContents()
