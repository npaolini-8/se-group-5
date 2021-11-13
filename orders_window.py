from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

class OrdersWindow(QDialog):
    def __init__(self, warehouse_controller):
        super(OrdersWindow, self).__init__()
        self.ui = loadUi("UI/orders_window.ui", self)
        self.warehouse_controller = warehouse_controller
        self.init_buttons()

    def init_buttons(self):
        self.return_btn.clicked.connect(self.return_clicked)


    def return_clicked(self):
        self.warehouse_controller.switch_to(self, 'main')
