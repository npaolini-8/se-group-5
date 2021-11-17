from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QSizePolicy
from PyQt6.uic import loadUi
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, warehouse_controller):
        super(MainWindow, self).__init__()
        self.ui = loadUi("UI/main_window.ui", self)
        self.warehouse_controller = warehouse_controller
        self.init_buttons()
        self.init_tables()
        self.center_on_screen()

    def init_buttons(self):
        self.logout_btn.clicked.connect(self.logout_clicked)
        self.items_btn.clicked.connect(self.items_clicked)
        self.create_order_btn.clicked.connect(self.orders_clicked)

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
        self.init_table(self.incoming_orders_tbl, self.warehouse_controller.get_incoming_orders())
        self.init_table(self.outgoing_orders_tbl, self.warehouse_controller.get_outgoing_orders())

    def logout_clicked(self):
        self.warehouse_controller.switch_to(self, 'login')

    def items_clicked(self):
        self.warehouse_controller.switch_to(self, 'items')

    def orders_clicked(self):
        self.warehouse_controller.switch_to(self, 'orders')

    def center_on_screen(self):
        geometry = self.screen().availableGeometry()
        self.move((geometry.width() - self.geometry().width()) / 2, (geometry.height() - self.geometry().height()) / 2)

    def refresh_incoming_orders(self):
        self.incoming_orders_tbl.clearContents()

    def refresh_outgoing_orders(self):
        self.outgoing_orders_tbl.clearContents()
