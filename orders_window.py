from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

class OrdersWindow(QDialog):
    def __init__(self, warehouse_controller):
        super(OrdersWindow, self).__init__()
        self.ui = loadUi("UI/orders_window.ui", self)
