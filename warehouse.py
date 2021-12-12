from pymongo import MongoClient # MongoDB Library to connect to database.
from datetime import datetime # Used to get timestamps for database information
from bson.objectid import ObjectId
import ssl # Used to specify certificate connection for MongoDB
import json # Used for backups
import os.path # Used for file writing path


class Warehouse():
    def __init__(self):
        self.cluster = MongoClient("mongodb+srv://softgod1:banana123@group5warehouse.kvdys.mongodb.net/test", ssl_cert_reqs=ssl.CERT_NONE)
        self.warehouse_database = self.cluster["warehouse"]
        self.items_collection = self.warehouse_database["items"]
        self.users_collection = self.warehouse_database["users"]
        self.orders_collection = self.warehouse_database["orders"]
        self.orders_history_collection = self.warehouse_database["orders_history"]
        self.containers_collection = self.warehouse_database["containers"]

    def find_order(self, id):
        return self.orders_collection.find_one({"_id": id})

    def get_time(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def generate_barcode(self, Name, increment):
        string = Name[0:3].upper()
        return f'{string}{increment}'

    def get_item_increment(self, Name):
        main_item = self.items_collection.find({"Name":Name})[0]
        return main_item["Barcode Increment"]

    def find_item(self, Name):
        return self.items_collection.find_one({"Name": Name})

    def item_column_titles(self):
        return self.items_collection.find_one({})

    def num_items(self):
        return self.items_collection.count()

    def get_items(self):
        items = []
        for item in self.items_collection.find({}):
            items.append(item)
        return items


    def get_users(self):
        users = []

        for user in self.users_collection.find({}):
            users.append(user)

        return users

    def find_user(self, username):
        return self.users_collection.find_one({'Username': username})

    def check_none_password(self, username) -> bool:
        if self.users_collection.find_one({"Username":username,"Password":None}):
            return True
        else:
            return False

    def increment_barcode_increment(self, Name):
        self.items_collection.update_one(
            {"Name": Name},
            {"$set": {"Barcode Increment": self.get_item_increment(Name)+1}}
        )

    def get_incoming_orders(self):
        incoming = []
        for order in self.orders_collection.find({'Order Type': 'Incoming'}):
            incoming.append(order)
        return incoming

    def get_outgoing_orders(self):
        outgoing = []
        for order in self.orders_collection.find({'Order Type': 'Outgoing'}):
            outgoing.append(order)
        return outgoing

    def create_main_item(self, user, name, description, modelNumber, brand, isActive=True,length=None,width=None,depth=None,weight=None):
        self.items_collection.insert_one(
            {
                "Name": name,
                "Description": description,
                "Model Number": modelNumber,
                "Brand": brand,
                "isActive": isActive,
                "Length" : length,
                "Width" : width,
                "Depth" : depth,
                "Weight" : weight,
                "Date modified": self.get_time(),
                "Last modified by": user,
                "Barcode Increment": 0,
                "Pending Shipment": 0,
                "Items": []
            }
        )

    def create_sub_item(self, user, Name, container=None):
        barcode = self.generate_barcode(Name, self.get_item_increment(Name)+1)
        self.items_collection.update_one(
            {"Name" : Name},
            {"$push":
                {"Items":
                    {
                    "Barcode":barcode,
                    "Container":container,
                    "Status":"Available",
                    "Date modified": self.get_time(),
                    "Last modified by":user
                    }
                }
            }
        )
        self.increment_barcode_increment(Name)
        return barcode

    def edit_main_item(self, user, Name, description=None, modelNumber=None, brand=None, isActive=None,length=None,width=None,depth=None,weight=None,newName=None,pending=None):
        edit_dict = {}
        if description is not None:
            edit_dict.update({"Description": description})
        if modelNumber is not None:
            edit_dict.update({"Model Number": modelNumber})
        if brand is not None:
            edit_dict.update({"Brand": brand})
        if isActive is not None:
            edit_dict.update({"isActive": isActive})
        if length is not None:
            edit_dict.update({"Length": length})
        if width is not None:
            edit_dict.update({"Width": width})
        if depth is not None:
            edit_dict.update({"Depth": depth})
        if weight is not None:
            edit_dict.update({"Weight": weight})
        if newName is not None:
            edit_dict.update({"Name": newName})
        if pending is not None:
            edit_dict.update({"Pending Shipment": pending})
        edit_dict.update([("Date modified", self.get_time()),("Last modified by", user)])

        self.items_collection.update_one(
            {"Name" : Name},
            {"$set": edit_dict}
        )

    def delete_main_item(self, name):
        self.items_collection.delete_one({"Name":name})

    def edit_sub_item(self, Name, barcode, user, container=None, status=None):
        edit_dict = {}
        if container is not None:
            edit_dict.update({"Items.$[subitem].Container": container})
        if status is not None:
            edit_dict.update({"Items.$[subitem].Status": status})
        edit_dict.update([("Items.$[subitem].Date modified", self.get_time()),("Items.$[subitem].Last modified by", user)])

        self.items_collection.update_one(
            {
                "Name": Name
            },
            {
                '$set': edit_dict
            },
            upsert=False,
            array_filters=[
                {
                    "subitem.Barcode": barcode
                }
            ]
        )

    def delete_sub_item(self, name, barcode):
        self.items_collection.update_one(
            {
                "Name": name
            },
            {
                '$pull': {"Items": {"Barcode":barcode}}
            }
        )
    #TODO: bret - generate salt field, add it here - generate salt
    def create_user(self, username, password, role, user):
        self.users_collection.insert_one(
            {
                "Username": username,
                "Password": password,
                "Lock Counter": 0,
                "Role": role,
                "isActive": True,
                "isLocked": False,
                "Date modified": self.get_time(),
                "Last modified by": user,
            }
        )

    def edit_user(self, username, user, password=None, role=None, newUsername=None, active=None, locked=None):
        edit_dict = {}
        if password is not None:
            if password == "":
                edit_dict.update({"Password": None})
            else:
                edit_dict.update({"Password": password})
        if role is not None:
            edit_dict.update({"Role":role})
        if newUsername is not None:
            edit_dict.update({"Username":newUsername})
        if active is not None:
            edit_dict.update({"isActive": active})
        if locked is not None:
            edit_dict.update({"isLocked":locked})
        edit_dict.update([("Date modified",self.get_time()),("Last modified by", user)])

        self.users_collection.update_one(
            {"Username" : username},
            {"$set": edit_dict}
        )

    def delete_user(self, username):
        self.users_collection.delete_one({"Username": username})

    def delete_order(self, id):
        self.orders_collection.delete_one({'_id': id})

    def archive_order(self, order):
        order['Status'] = 'Complete'
        order['Date modified'] = self.get_time()
        self.orders_history_collection.insert_one(order)

    def create_order(self, order_type, client, status, user):
        inserted_result = self.orders_collection.insert_one(
            {
                "Order Type": order_type,
                "Client": client,
                "Status": status,
                "Date modified": self.get_time(),
                "Last modified by": user,
                "Order Items": []
            }
        )
        return str(inserted_result.inserted_id)

    def add_to_order(self, order_id, item_name, count, order_type):
        item = self.find_item(item_name)
        obj = ObjectId(order_id)

        if order_type == "Outgoing":
            self.items_collection.update_one(
                {"_id" : item["_id"]},
                {"$set":
                    {"Pending Shipment":item["Pending Shipment"] + count}
                }
            )

        self.orders_collection.update_one(
            {"_id" : obj},
            {"$push":
                {"Order Items":
                    {
                    "Item ID": item["_id"],
                    "Item Name": item["Name"],
                    "Count": count
                    }
                }
            }
        )

    def add_container_type( self, name, length, width, depth, max_weight, user):
        self.containers_collection.insert_one(
            {
                "name" : name,
                "legnth" : length,
                "width" : width,
                "depth" : depth,
                "max_weight" : max_weight,
                "last_modified" : self.get_time(),
                "last_modified_by" : user,
                "containers" : [],
                "id_increment" : 0
            }
        )

    def find_container_type(self, name):
        return self.containers_collection.find_one({"name": name})

    def add_container( self, name, x_loc, y_loc, user):

        #grab id increment for id generation, save, then increment
        container_type = self.find_container_type(name)
        id_increment = container_type["id_increment"]
        id_increment += 1
        self.containers_collection.update_one(
            {"name" : name},
            {"$set" :
                {
                    "id_increment" : id_increment
                }
            }
        )

        #create new container using id increment
        self.containers_collection.update_one(
            {"name" : name},
            {"$push":
                {"containers":
                    {
                        "id" : str(id_increment),
                        "v_curr" : 0,
                        "w_curr" : 0,
                        "x_loc" : x_loc,
                        "y_loc" : y_loc,
                        "last_modified" : self.get_time(),
                        "last_modified_by" : user,
                        "items" : []

                    }
                }
            }
        )

    #returns single container object from container type
    #TODO: is there a better way to do this? need to search an array of dicts
    def find_container( self, cont_type, cont_id ):

        container_type = self.find_container_type(cont_type)

        for container in container_type["containers"]:
            if container["id"] == cont_id:
                return container

        return None


    #adds item to container
    def add_item_to_container( self, cont_type, cont_id, item_name, item_barcode ):

        #grab container, then the item list, append to the list, set the list in the db to the new list (list of item dicts)
        container = self.find_container( cont_type, cont_id)

        item_list = container["items"]
        item_list.append( {"item_name":item_name, "barcode": item_barcode})

        self.containers_collection.update_one(
            {
                "name": cont_type
            },
            {
                '$set': { "containers.$[containers].items": item_list}
            },
            upsert=False,
            array_filters=[
                {
                    "containers.id": cont_id
                }
            ]
        )

    def create_backup(self):
        for database in [self.items_collection, self.orders_collection, self.orders_history_collection, self.users_collection]:
            while True:
                try:
                    database_list = list(database.find())
                    for kiefernumber1fan, document in enumerate(database_list):
                        document["_id"] = str(document["_id"])
                        if database in [self.orders_collection, self.orders_history_collection]:
                            for item in document["Order Items"]:
                                item["Item ID"] = str(item["Item ID"])

                    with open(f'./Backups/{database.name}_backup.txt', 'w') as backup_file:
                        json.dump(database_list, backup_file)
                        break
                except:
                    pass

    def clear_database(self, database):
        database.delete_many({})

    def import_backup(self, database, file):
        if database == 'Users':
            database = self.users_collection
        elif database == 'Items':
            database = self.items_collection
        elif database == 'Orders':
            database = self.orders_collection
        elif database == 'Orders History':
            database = self.orders_history_collection

        with open(file, 'r') as backup_file:
            backup_json = json.load(backup_file)
            dict_list = []
            for document in backup_json:
                document_dict = {}
                for item in document:
                    if item == '_id':
                        document_dict.update({item: ObjectId(document[item])})
                    elif item == 'Order Items':
                        sub_item_dict_list = []
                        for order_item in document["Order Items"]:
                            sub_item_dict = {}
                            for sub_item in order_item:
                                if sub_item == 'Item ID':
                                    sub_item_dict.update({sub_item: ObjectId(order_item[sub_item])})
                                else:
                                    sub_item_dict.update({sub_item: order_item[sub_item]})
                            sub_item_dict_list.append(sub_item_dict)
                        document_dict.update({item: sub_item_dict_list})
                    else:
                        document_dict.update({item: document[item]})
                dict_list.append(document_dict)
            self.clear_database(database)
            for dict in dict_list:
                database.insert_one(dict)

    def get_user_lock(self, username):
        return self.find_user(username)["Lock Counter"]

    def increment_user_lock(self, username):
        self.users_collection.update_one(
            {"Username": username},
            {"$set": {"Lock Counter": self.get_user_lock(username)+1}}
        )
        return self.get_user_lock(username)

    def clear_user_lock(self, username):
        self.users_collection.update_one(
            {"Username": username},
            {"$set": {"Lock Counter": 0}}
        )
        
#warehouse = Warehouse()