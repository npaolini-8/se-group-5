from warehouse import Warehouse
from application import Application
from bson.objectid import ObjectId
import re

class WarehouseController():
    def __init__(self):
        self.warehouse = Warehouse()
        self.current_user = None
        self.app = Application(self)
        exit(self.app.exec())


    def switch_to(self, current, win_name):
        current.hide()
        if win_name == 'login':
            self.app.login_window.clear_input()
            self.app.login_window.show()
        elif win_name == 'main':
            self.app.main_window.refresh_tables()
            self.app.main_window.show()
            self.app.main_window.ui.user_lbl.setText('Logged in as ' + self.get_current_username())
        elif win_name == 'items':
            self.app.items_window.refresh_item_table()
            self.app.items_window.show()
        elif win_name == 'create_order':
            self.app.create_order_window.refresh_table()
            self.app.create_order_window.show()
        elif win_name == 'process_order':
            self.app.order_processing_window.show()
        elif win_name == 'backup':
            current.show()
            #self.app.backup_window.show()
            #self.app.main_window.show()
            #current.show()


        elif win_name == 'admin_window':
            self.app.admin_window.show()
            #self.app.main_window.show()
            #pass

    def complete_order(self, order_id):
        id = ObjectId(order_id)
        order = self.warehouse.find_order(id)
        self.warehouse.archive_order(order)
        #if order['Order Type'] == "Incoming":

        self.warehouse.delete_order(id)


    def get_current_username(self):
        return self.current_user["Username"]

    def get_current_role(self):
        return self.current_user["Role"] #could be Admin, User

    #give user, supervisor, admin
    #returns true if role is >= role
    def access_check(self, role):
        if role == "User":
            return True
        elif role == "Supervisor":
            if self.get_current_role() == "User":
                return False
            else:
                return True
        elif role == "Admin":
            if self.get_current_role() == "Admin":
                return True
    #TODO: bred - encrypt given password and then check with DB
    def connect_user(self, username, password):
        self.warehouse.cluster.server_info()  #This will fail if we don't have a connection to the server
        return self.warehouse.users_collection.find_one({"Username": username,"Password": password}) #BretC1, bananafish6

    def set_current_user(self, new_user):
        self.current_user = new_user

    def get_incoming_orders_raw(self):
        return self.warehouse.get_incoming_orders()

    def get_outgoing_orders_raw(self):
        return self.warehouse.get_outgoing_orders()

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

    def get_item(self, item_name):
        return self.warehouse.find_item(item_name)

    def get_items_raw(self):
        return self.warehouse.get_items()

    def get_items(self):
        items = []
        for item in self.warehouse.get_items():
            if item['isActive'] == True:
                items.append({'Item Name': item['Name'], 'Stock': len(item['Items'])})
        return items

    def get_all_items(self):
        # items = []
        # for item in self.warehouse.get_items():
        #         items.append({'Item Name': item['Name'], 'Stock': len(item['Items'])})
        # return items
        return self.warehouse.get_items()

    def get_item(self, name):
        return self.warehouse.find_item(name)

    def get_items_from_order(self, order):
        return order['Order Items']

    def get_items_raw_by_name(self, name):
        items = []
        for item in self.warehouse.get_items():
            if item['isActive'] == True:
                items.append({'Item Name': item['Name'], 'Stock': len(item['Items'])})
        return items


    def get_order(self, id_string):
        return self.warehouse.find_order(ObjectId(id_string))


    def get_barcodes(self, item_type):
        main_item = self.get_item(item_type)
        barcodes = []
        if main_item == None:
            return []
        for item in main_item['Items']:
            barcodes.append(item['Barcode'])
        return barcodes


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

    def validate_new_item_name(self, item_name):
        if item_name is None or item_name == "":
            return "Item Name Required"
        elif self.warehouse.find_item(item_name) is not None:
            return "Item Name is already in use"
        else:
            return "OK"

    def parseable_int_str(self, string):
        if re.match(r"^[1-9][0-9]*$", string):
            return True
        else:
            return False

    #MVC wrappers, could flesh out for error handling
    def create_new_user(self, username, password, role): # setting pw to None for new users for now
        self.warehouse.create_user(username,None,role, self.get_current_username())

    def edit_user(self, username, password=None, role=None, newUsername=None, active=None, locked=None):
        if locked == False:
            self.warehouse.clear_user_lock(username)
        if password == "":
            self.warehouse.edit_user(username, self.get_current_username(), role=role,newUsername=newUsername, active=active, locked=locked)
        else: #setting to empty string for null convert for now
            self.warehouse.edit_user(username, self.get_current_username(), password="",role=role,newUsername=newUsername, active=active,locked=locked)
    #TODO: bret - save encrypted PW
    def set_new_pw(self, username, password):
        self.warehouse.edit_user(username, self.get_current_username(), password=password)

    def create_new_item(self, item_name, item_desc, item_model, item_brand, isActive, item_weight=None, item_length=None, item_width=None, item_depth=None):
        self.warehouse.create_main_item(self.get_current_username(), item_name, item_desc, item_model, item_brand,isActive=isActive,length=item_length,width=item_width,depth=item_depth,weight=item_weight)

    def edit_item( self, item_name, item_desc=None,item_model=None,item_brand=None,isActive=None,item_weight=None, item_length=None, item_width=None, item_depth=None, new_name=None):
        self.warehouse.edit_main_item(self.get_current_username(),item_name, description=item_desc,modelNumber=item_model,brand=item_brand,isActive=isActive,length=item_length,width=item_width,depth=item_depth,weight=item_weight,newName=new_name)

    def create_sub_item(self, item_name):
        self.warehouse.create_sub_item(self.get_current_username(), item_name)

    def delete_sub_item(self, item_name, barcode):
        self.warehouse.delete_sub_item(item_name,barcode)

    def get_user_lock(self, username):
        return self.warehouse.get_user_lock(username)

    def increment_user_lock(self, username):
        self.warehouse.increment_user_lock(username)

    def clear_user_lock(self, username):
        self.warehouse.clear_user_lock(username)
        
    def set_none_password(self, username, user):
        self.warehouse.edit_user(username, user, password=None)

    def check_none_password(self, username):
        if self.warehouse.find_user(username)["Password"] == None:
            # promp new password by swapping windows to new password window etc
            pass

    def create_order(self, order_type, client, status):
        return self.warehouse.create_order(order_type, client, status, self.get_current_username())

    def check_none_password(self,username) -> bool:
        return self.warehouse.check_none_password(username)

    def find_user(self, username):
        return self.warehouse.find_user(username)
