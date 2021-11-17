from pymongo import MongoClient # MongoDB Library to connect to database.
from datetime import datetime # Used to get timestamps for database information
from bson.objectid import ObjectId
import ssl # Used to specify certificate connection for MongoDB


def get_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def generate_barcode(Name, increment):
    string = Name[0:3].upper()
    return f'{string}{increment}'

class Warehouse():
    def __init__(self):
        self.cluster = MongoClient("mongodb+srv://softgod1:banana123@group5warehouse.kvdys.mongodb.net/test", ssl_cert_reqs=ssl.CERT_NONE)
        self.warehouse_database = self.cluster["warehouse"]
        self.items_collection = self.warehouse_database["items"]
        self.users_collection = self.warehouse_database["users"]
        self.orders_collection = self.warehouse_database["orders"]
        self.orders_history_collection = self.warehouse_database["orders_history"]
        self.containers_collection = self.warehouse_database["containers"]

    def get_item_increment(self, Name):
        main_item = self.items_collection.find({"Name":Name})[0]
        return main_item["Barcode Increment"]

    def find_item(self, Name):
        return self.items_collection.find_one({"Name": Name})

    def item_column_titles(self):
        value = self.items_collection.find_one({})
        if value == None:
            return None
        return value

    def num_items(self):
        return self.items_collection.count()

    def get_items(self, max = 100):
        items = []
        count = 0
        for item in self.items_collection.find({}):
            items.append(item)
            count += 1
            if count == max:
                break
        return items


    def increment_barcode_increment(self, Name):
        self.items_collection.update_one(
            {"Name": Name},
            {"$set": {"Barcode Increment": self.get_item_increment(Name)+1}}
        )

    def create_main_item(self, name, description, modelNumber, brand):
        self.items_collection.insert_one(
            {
                "Name": name,
                "Description": description,
                "Model Number": modelNumber,
                "Brand": brand,
                "isActive": True,
                "Date modified": get_time(),
                "Last modified by": "getUser()",
                "Barcode Increment": 0,
                "Items": []
            }
        )

    def create_sub_item(self, Name, container):
        barcode = generate_barcode(Name, self.get_item_increment(Name)+1)
        self.items_collection.update_one(
            {"Name" : Name},
            {"$push":
                {"Items":
                    {
                    "Barcode":barcode,
                    "Container":container,
                    "Status":"Available",
                    "Date modified":get_time(),
                    "Last modified by":"get_user()"
                    }
                }
            }
        )
        self.increment_barcode_increment(Name)
        return barcode

    def edit_main_item(self, Name, description=None, modelNumber=None, brand=None, isActive=None):
        edit_dict = {}
        if description is not None:
            edit_dict.update({"Description": description})
        if modelNumber is not None:
            edit_dict.update({"Model Number": modelNumber})
        if brand is not None:
            edit_dict.update({"Brand": brand})
        if isActive is not None:
            edit_dict.update({"isActive": isActive})
        edit_dict.update([("Date modified",get_time()),("Last modified by","getUser()")])

        self.items_collection.update_one(
            {"Name" : Name},
            {"$set": edit_dict}
        )

    def delete_main_item(self, name):
        self.items_collection.delete_one({"Name":name})

    def edit_sub_item(self, Name, barcode, container=None, status=None):
        edit_dict = {}
        if container is not None:
            edit_dict.update({"Items.$[subitem].Container": container})
        if status is not None:
            edit_dict.update({"Items.$[subitem].Status": status})
        edit_dict.update([("Items.$[subitem].Date modified",get_time()),("Items.$[subitem].Last modified by","getUser()")])

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

    def create_user(self, username, password, role):
        self.users_collection.insert_one(
            {
                "Username": username,
                "Password": password,
                "Role": role,
                "isActive": True,
                "isLocked": False,
                "Date modified": get_time(),
                "Last modified by": "getUser()",
            }
        )

    def edit_user(self, username, password=None, role=None):
        edit_dict = {}
        if password is not None:
            edit_dict.update({"Password": password})
        if role is not None:
            edit_dict.update({"Role":role})
        edit_dict.update([("Date modified",get_time()),("Last modified by","getUser()")])

        self.users_collection.update_one(
            {"Username" : username},
            {"$set": edit_dict}
        )

    def delete_user(self, username):
        self.users_collection.delete_one({"Username": username})

    def create_order(self, order_type, client, status):
        inserted_result = self.orders_collection.insert_one(
            {
                "Order Type": order_type,
                "Client": client,
                "Status": status,
                "Date modified": get_time(),
                "Last modified by": "getUser()",
                "Order Items": []
            }
        )
        return str(inserted_result.inserted_id)
    
    def add_to_order(self, order_id, item_name, count):
        item = self.find_item(item_name)
        obj = ObjectId(order_id)
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

    def add_container_type( self, name, length, width, depth, max_weight ):
        self.containers_collection.insert_one(
            {
                "name" : name,
                "legnth" : length,
                "width" : width,
                "depth" : depth,
                "max_weight" : max_weight,
                "last_modified" : get_time(),
                "last_modified_by" : "getUser()",
                "containers" : [],
                "id_increment" : 0
            }
        )
    
    def find_container_type(self, name):
        return self.containers_collection.find_one({"name": name})

    def add_container( self, name, x_loc, y_loc):

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
                        "last_modified" : get_time(),
                        "last_modified_by" : "getUser()",
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




#warehouse = Warehouse()
#print(warehouse.items_collection.find_one({}))

# create_main_item("Banana", "This is a fruit derived from the angels.", "BANANA0", "Banana Incorporated")
# create_sub_item("Banana", "BAN0001", "PALLET0001")
# edit_main_item("Banana", description="New Description", brand="New Brand") ~ This is how we would use optional parameters to only have to input what we want to change
# edit_sub_item("Banana", "BAN3", container="PALLET0001", status="PooPooPeePee")
# warehouse.create_user("admin", "admin", "Admin")
# edit_user("TonyN123", password="newPassword123")
# warehouse.create_order("Random Type", "Jerry", "IN PROGRESS")
# warehouse.add_to_order("617f52a84464fbb2790d1ca2", "Logitech G502 Lightspeed", 3)

#atomic container tests, all passed
#print(warehouse.find_container_type("testContainer"))
#print(warehouse.find_container("testContainer","1"))
#warehouse.add_container_type("test2", 14, 15, 16, 1000)
#warehouse.add_container("test2", 50, 100)
#warehouse.add_item_to_container("test2", "1", "acorn", "AC01")

#warehouse.create_order("Random Type", "Jerry", "IN PROGRESS")
# warehouse.add_to_order("617f52a84464fbb2790d1ca2", "Logitech G502 Lightspeed", 3)
