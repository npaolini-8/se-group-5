from PySide6.QtCore import Qt
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 50, 261, 501))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.items_btn = QPushButton(self.verticalLayoutWidget)
        self.items_btn.setObjectName(u"items_btn")
        self.items_btn.setMinimumSize(QSize(0, 80))

        self.verticalLayout.addWidget(self.items_btn)

        self.create_order_btn = QPushButton(self.verticalLayoutWidget)
        self.create_order_btn.setObjectName(u"create_order_btn")
        self.create_order_btn.setMinimumSize(QSize(0, 80))

        self.verticalLayout.addWidget(self.create_order_btn)

        self.process_order_btn = QPushButton(self.verticalLayoutWidget)
        self.process_order_btn.setObjectName(u"process_order_btn")
        self.process_order_btn.setMinimumSize(QSize(0, 80))

        self.verticalLayout.addWidget(self.process_order_btn)

        self.backup_btn = QPushButton(self.verticalLayoutWidget)
        self.backup_btn.setObjectName(u"backup_btn")
        self.backup_btn.setMinimumSize(QSize(0, 80))

        self.verticalLayout.addWidget(self.backup_btn)

        self.admin_panel_btn = QPushButton(self.verticalLayoutWidget)
        self.admin_panel_btn.setObjectName(u"admin_panel_btn")
        self.admin_panel_btn.setMinimumSize(QSize(0, 80))

        self.verticalLayout.addWidget(self.admin_panel_btn)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(290, 10, 491, 531))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.incoming_orders_tbl = QTableWidget(self.verticalLayoutWidget_2)
        self.incoming_orders_tbl.setObjectName(u"incoming_orders_tbl")
        self.incoming_orders_tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.incoming_orders_tbl.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.incoming_orders_tbl)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.outgoing_orders_tbl = QTableWidget(self.verticalLayoutWidget_2)
        self.outgoing_orders_tbl.setObjectName(u"outgoing_orders_tbl")
        self.outgoing_orders_tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.outgoing_orders_tbl.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.outgoing_orders_tbl)

        self.logout_btn = QPushButton(self.centralwidget)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setGeometry(QRect(20, 10, 88, 34))
        self.user_lbl = QLabel(self.centralwidget)
        self.user_lbl.setObjectName(u"user_lbl")
        self.user_lbl.setGeometry(QRect(120, 30, 161, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.items_btn.setText(QCoreApplication.translate("MainWindow", u"Items", None))
        self.create_order_btn.setText(QCoreApplication.translate("MainWindow", u"Create Order", None))
        self.process_order_btn.setText(QCoreApplication.translate("MainWindow", u"Process Order", None))
        self.backup_btn.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.admin_panel_btn.setText(QCoreApplication.translate("MainWindow", u"Admin Panel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"                                                      Incoming Orders", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"                                                      Outgoing Orders", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.user_lbl.setText("")
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

    def init_buttons(self):
        self.ui.logout_btn.clicked.connect(self.logout_clicked)
        self.ui.items_btn.clicked.connect(self.items_clicked)
        self.ui.create_order_btn.clicked.connect(self.create_order_clicked)
        self.ui.process_order_btn.clicked.connect(self.process_order_clicked)
        self.ui.backup_btn.clicked.connect(self.backup_clicked)
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
        self.init_table(self.ui.incoming_orders_tbl, self.warehouse_controller.get_incoming_orders())
        self.init_table(self.ui.outgoing_orders_tbl, self.warehouse_controller.get_outgoing_orders())

    def logout_clicked(self):
        self.warehouse_controller.switch_to(self, 'login')

    def items_clicked(self):
        self.warehouse_controller.switch_to(self, 'items')

    def create_order_clicked(self):
        self.warehouse_controller.switch_to(self, 'create_order')

    def process_order_clicked(self):
        self.warehouse_controller.switch_to(self, 'process_order')
        current_row = self.ui.outgoing_orders_tbl.currentRow()
        if current_row >= 0:
            print(self.ui.outgoing_orders_tbl.item(current_row, 0).text())

    def backup_clicked(self):
        self.warehouse_controller.switch_to(self, 'backup')

    def admin_panel_clicked(self):
        self.warehouse_controller.switch_to(self, 'admin_panel')

    def center_on_screen(self):
        geometry = self.screen().availableGeometry()
        self.move((geometry.width() - self.geometry().width()) / 2, (geometry.height() - self.geometry().height()) / 2)

    def refresh_incoming_orders(self):
        self.ui.incoming_orders_tbl.clearContents()

    def refresh_outgoing_orders(self):
        self.ui.outgoing_orders_tbl.clearContents()
