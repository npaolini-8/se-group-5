from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self, warehouse_controller):
        super(MainWindow, self).__init__()
        self.ui = loadUi("UI/main_window.ui", self)
        self.warehouse_controller = warehouse_controller
        self.init_buttons()
        self.center_on_screen()

    def init_buttons(self):
        self.logout_btn.clicked.connect(self.logout_clicked)
        self.items_btn.clicked.connect(self.items_clicked)
        self.create_order_btn.clicked.connect(self.orders_clicked)

    def logout_clicked(self):
        self.warehouse_controller.switch_to(self, 'login')

    def items_clicked(self):
        self.warehouse_controller.switch_to(self, 'items')

    def orders_clicked(self):
        self.warehouse_controller.switch_to(self, 'orders')

    def center_on_screen(self):
        geometry = self.screen().availableGeometry()
        self.move((geometry.width() - self.geometry().width()) / 2, (geometry.height() - self.geometry().height()) / 2)
