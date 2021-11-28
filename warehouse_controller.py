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
            self.app.main_window.ui.user_lbl.setText('Logged in as ' + self.get_current_username())
        elif win_name == 'items':
            self.app.items_window.show()
        elif win_name == 'create_order':
            self.app.create_order_window.show()
        elif win_name == 'process_order':
            self.app.orders_window.show()
        elif win_name == 'backup':
            current.show()
            #self.app.backup_window.show()
            #self.app.main_window.show()
            #current.show()
            

        elif win_name == 'admin_window':
            self.app.admin_window.show()
            #self.app.main_window.show()
            #pass


    def get_current_username(self):
        return self.current_user["Username"]

    def get_current_role(self):
        return self.current_user["Role"] #could be Admin, User


    def connect_user(self, username, password):
        self.warehouse.cluster.server_info()  #This will fail if we don't have a connection to the server
        return self.warehouse.users_collection.find_one({"Username": username,"Password": password}) #BretC1, bananafish6

    def set_current_user(self, new_user):
        self.current_user = new_user

    def get_incoming_orders(self):  #Formatted purposefully
        orders = []
        for order in self.warehouse.get_incoming_orders():
            orders.append({'Order ID': order['_id'], 'Client': order['Client'], 'Status': order['Status'], 'Order Items': str([str(item['Count']) + ' ' + item['Item Name'] + 's' for item in order['Order Items']])})
        return orders

    def get_outgoing_orders(self):  #Formatted purposefully
        orders = []
        for order in self.warehouse.get_outgoing_orders():
            orders.append({'Order ID': order['_id'], 'Client': order['Client'], 'Status': order['Status'], 'Order Items': str([str(item['Count']) + ' ' + item['Item Name'] + 's' for item in order['Order Items']])})
        return orders

    def get_items(self):
        items = []
        for item in self.warehouse.get_items():
            if item['isActive'] == True:
                items.append({'Item Name': item['Name'], 'Stock': len(item['Items'])})
        return items

    def get_users(self):
        return self.warehouse.get_users()

    #Validates input for admin window
    def validate_new_username(self, username ):
        if username is not None:
            if self.warehouse.find_user(username) is not None:
                return "Username is already in use"
            else:
                return "OK"
        else:
            return "Username required"

    def validate_new_pw(self, password):
        if password is None:
            return "Password required"
        else:
            return "OK"


    #MVC wrappers, could flesh out for error handling
    def create_new_user(self, username, password, role):
        self.warehouse.create_user(username,password,role, self.get_current_username())



    def edit_user(self, username, password=None, role=None, newUsername=None, active=None, locked=None):
        if password == "":
            self.warehouse.edit_user(username, self.get_current_username(), role=role,newUsername=newUsername, active=active, locked=locked)
        else:
            self.warehouse.edit_user(username, self.get_current_username(), password=password,role=role,newUsername=newUsername, active=active,locked=locked)

    def create_new_item(self, item_name, item_desc, item_model, item_brand, isActive, item_weight=None, item_length=None, item_width=None, item_depth=None):
        self.warehouse.create_main_item(self.get_current_username(), item_name, item_desc, item_model, item_brand,isActive=isActive,length=item_length,width=item_width,depth=item_depth,weight=item_weight)

    def edit_item( self, item_name, item_desc=None,item_model=None,item_brand=None,isActive=None,item_weight=None, item_length=None, item_width=None, item_depth=None, new_name=None):
        self.warehouse.edit_main_item(self.get_current_username(),item_name, description=item_desc,modelNumber=item_model,brand=item_brand,isActive=isActive,length=item_length,width=item_width,depth=item_depth,weight=item_weight,newName=new_name)

    def create_sub_item(self, item_name):
        self.warehouse.create_sub_item(self.get_current_username(), item_name)

    def delete_sub_item(self, item_name, barcode):
        self.warehouse.delete_sub_item(item_name,barcode)
    
