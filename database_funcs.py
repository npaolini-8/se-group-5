from pymongo import MongoClient # MongoDB Library to connect to database.
from datetime import datetime # Used to get timestamps for database information
import ssl # Used to specify certificate connection for MongoDB


def get_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def generate_barcode(id, increment):
    string = id[0:3].upper()
    return f'{string}{increment}'

class Warehouse():
    def __init__(self):
        self.cluster = MongoClient("mongodb+srv://softgod1:banana123@group5warehouse.kvdys.mongodb.net/test", ssl_cert_reqs=ssl.CERT_NONE)
        self.warehouse_database = self.cluster["warehouse"]
        self.items_collection = self.warehouse_database["items"]
        self.users_collection = self.warehouse_database["users"]

    def get_item_increment(self, id):
        main_item = self.items_collection.find({"_id":id})[0]
        return main_item["Barcode Increment"]

    def find_item(self, id):
        return self.items_collection.find_one({"_id": id})

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


    def increment_barcode_increment(self, id):
        self.items_collection.update_one(
            {"_id": id},
            {"$set": {"Barcode Increment": self.get_item_increment(id)+1}}
        )

    def create_main_item(self, id, description, modelNumber, brand):
        self.items_collection.insert_one(
            {
                "_id": id,
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

    def create_sub_item(self, id, container):
        self.items_collection.update_one(
            {"_id" : id},
            {"$push":
                {"Items":
                    {
                    "Barcode":generate_barcode(id, self.get_item_increment(id)+1),
                    "Container":container,
                    "Status":"Available",
                    "Date modified":get_time(),
                    "Last modified by":"get_user()"
                    }
                }
            }
        )
        self.increment_barcode_increment(id)

    def edit_main_item(self, id, description=None, modelNumber=None, brand=None, isActive=None):
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
            {"_id" : id},
            {"$set": edit_dict}
        )

    def edit_sub_item(self, id, barcode, container=None, status=None):
        edit_dict = {}
        if container is not None:
            edit_dict.update({"Items.$[subitem].Container": container})
        if status is not None:
            edit_dict.update({"Items.$[subitem].Status": status})
        edit_dict.update([("Items.$[subitem].Date modified",get_time()),("Items.$[subitem].Last modified by","getUser()")])

        self.items_collection.update_one(
            {
                "_id": id
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

    def create_user(self, id, password, role):
        self.users_collection.insert_one(
            {
                "_id": id,
                "Password": password,
                "Role": role,
                "isActive": True,
                "isLocked": False,
                "Date modified": get_time(),
                "Last modified by": "getUser()",
            }
        )

    def edit_user(self, id, password=None, role=None):
        edit_dict = {}
        if password is not None:
            edit_dict.update({"Password": password})
        if role is not None:
            edit_dict.update({"Role":role})
        edit_dict.update([("Date modified",get_time()),("Last modified by","getUser()")])

        self.users_collection.update_one(
            {"_id" : id},
            {"$set": edit_dict}
        )


# create_main_item("Banana", "This is a fruit derived from the angels.", "BANANA0", "Banana Incorporated")
# create_sub_item("Banana", "BAN0001", "PALLET0001")
# edit_main_item("Banana", description="New Description", brand="New Brand") ~ This is how we would use optional parameters to only have to input what we want to change
# edit_sub_item("Banana", "BAN3", container="PALLET0001", status="PooPooPeePee")
# create_user("TonyN123", "banana123", "Admin")
# edit_user("TonyN123", password="newPassword123")
