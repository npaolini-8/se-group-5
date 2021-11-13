from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

class ItemsWindow(QDialog):
    def __init__(self, warehouse_controller):
        super(ItemsWindow, self).__init__()
        self.ui = loadUi("UI/items_window.ui", self)
