from warehouse import Warehouse
from application import Application

class WarehouseController():
    def __init__(self):
        self.warehouse = Warehouse()
        self.current_user = None
        self.app = Application(self)
        exit(self.app.exec())


    def switch_to(self, current, win_name):
        current.hide()
        if win_name == 'login':
            self.app.login_window.show()
        elif win_name == 'main':
            self.app.main_window.show()
        elif win_name == 'orders':
            self.app.orders_window.show()
        elif win_name == 'items':
            self.app.items_window.show()

    def connect_user(self, username, password):
        self.warehouse.cluster.server_info()  #This will fail if we don't have a connection to the server
        return self.warehouse.users_collection.find_one({"Username": username,"Password": password}) #BretC1, bananafish6

    def set_current_user(self, new_user):
        self.current_user = new_user

    def get_incoming_orders(self):  #Formatted purposefully
        orders = []
        for order in self.warehouse.get_incoming_orders():
            orders.append({'Client': order['Client'], 'Status': order['Status'], 'Order Items': str([str(item['Count']) + ' ' + item['Item Name'] + 's' for item in order['Order Items']])})
        return orders

    def get_outgoing_orders(self):  #Formatted purposefully
        orders = []
        for order in self.warehouse.get_outgoing_orders():
            orders.append({'Client': order['Client'], 'Status': order['Status'], 'Order Items': str([str(item['Count']) + ' ' + item['Item Name'] + 's' for item in order['Order Items']])})
        return orders
