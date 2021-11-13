from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self, warehouse_controller):
        super(MainWindow, self).__init__()
        self.ui = loadUi("UI/main_window.ui", self)
        self.warehouse_controller = warehouse_controller
        self.init_buttons()

    def init_buttons(self):
        self.items_btn.clicked.connect(self.items_clicked)
        self.create_order_btn.clicked.connect(self.orders_clicked)

    def items_clicked(self):
        self.warehouse_controller.switch_to(self, 'items')

    def orders_clicked(self):
        self.warehouse_controller.switch_to(self, 'orders')
