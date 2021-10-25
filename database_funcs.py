from pymongo import MongoClient # MongoDB Library to connect to database.
from datetime import datetime # Used to get timestamps for database information
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
        self.items_collection.update_one(
            {"Name" : Name},
            {"$push":
                {"Items":
                    {
                    "Barcode":generate_barcode(Name, self.get_item_increment(Name)+1),
                    "Container":container,
                    "Status":"Available",
                    "Date modified":get_time(),
                    "Last modified by":"get_user()"
                    }
                }
            }
        )
        self.increment_barcode_increment(Name)

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

#warehouse = Warehouse()
#print(warehouse.items_collection.find_one({}))

# create_main_item("Banana", "This is a fruit derived from the angels.", "BANANA0", "Banana Incorporated")
# create_sub_item("Banana", "BAN0001", "PALLET0001")
# edit_main_item("Banana", description="New Description", brand="New Brand") ~ This is how we would use optional parameters to only have to input what we want to change
# edit_sub_item("Banana", "BAN3", container="PALLET0001", status="PooPooPeePee")
# warehouse.create_user("admin", "admin", "Admin")
# edit_user("TonyN123", password="newPassword123")
