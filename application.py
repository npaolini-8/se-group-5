from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QIcon
from sys import exit, argv
from create_order_window import CreateOrderWindow
from login_window import LoginWindow
from main_window import MainWindow
from items_window import ItemsWindow
from orders_window import OrdersWindow
from admin_window import AdminWindow


#Application controls all sub-windows
class Application(QApplication):
    def __init__(self, warehouse_controller):
        self.setStyle('Fusion')
        super().__init__()
        self.setWindowIcon(QIcon('Resources/icon.png'))
        self.warehouse_controller = warehouse_controller
        if len(argv) == 1 or argv[1] == 'n':  #n -- normal startup
            self.start()
        elif argv[1] == 'm':                #m -- skip to main window
            self.start(skipLogin = True)


    def start(self, skipLogin = False):
        self.threadpool = QThreadPool()
        self.login_window = LoginWindow(self.warehouse_controller)
        self.main_window = MainWindow(self.warehouse_controller)
        self.order_processing_window = OrdersWindow(self.warehouse_controller)
        self.items_window = ItemsWindow(self.warehouse_controller)
        self.create_order_window = CreateOrderWindow(self.warehouse_controller)
        self.admin_window = AdminWindow(self.warehouse_controller)

        if skipLogin:
            self.warehouse_controller.set_current_user(self.warehouse_controller.connect_user('admin', 'admin'))
            self.main_window.show()
        else:
            self.login_window.show()

    def restart(self):
        self.login_window = LoginWindow(self.warehouse_controller)
        self.main_window = MainWindow(self.warehouse_controller)
        self.order_processing_window = OrdersWindow(self.warehouse_controller)
        self.items_window = ItemsWindow(self.warehouse_controller)
        self.create_order_window = CreateOrderWindow(self.warehouse_controller)
        self.admin_window = AdminWindow(self.warehouse_controller)