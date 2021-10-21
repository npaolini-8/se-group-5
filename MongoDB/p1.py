from pymongo import MongoClient # MongoDB Library to connect to database.
from datetime import datetime # Used to get timestamps for database information
import ssl # Used to specify certificate connection for MongoDB

# This line allows us to connect to the MongoDB. Parameter 1 is the connection link grabbed from MongoDB.com. Paramter 2 is a ssl parameter which essentially says we don't want to check for a certificate when connecting.
cluster = MongoClient("mongodb+srv://softgod1:banana123@group5warehouse.kvdys.mongodb.net/test", ssl_cert_reqs=ssl.CERT_NONE)

# This line just sets variable "warehouse_database" to connect to the cluster which indexes to our database "warehouse".
warehouse_database = cluster["warehouse"]

# This line indexes our "warehouse" database into the items collection.
items_collection = warehouse_database["items"]

# This line indexes our "warehouse" database into the users collection.
users_collection = warehouse_database["users"]

def get_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def generate_barcode(id, increment):
    string = id[0:3].upper()
    return f'{string}{increment}'

def get_item_increment(id):
    main_item = items_collection.find({"_id":id})[0]
    return main_item["Barcode Increment"]

def increment_barcode_increment(id):
    items_collection.update_one(
        {"_id": id},
        {"$set": {"Barcode Increment": get_item_increment(id)+1}}
    )

def create_main_item(id, description, modelNumber, brand):
    try:
        items_collection.insert_one(
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
    except:
        print(f"Error: {id} already exist!")

def create_sub_item(id, container):
    items_collection.update_one(
        {"_id" : id},
        {"$push": 
            {"Items":
                {
                "Barcode":generate_barcode(id, get_item_increment(id)+1),
                "Container":container,
                "Status":"Available",
                "Date modified":get_time(),
                "Last modified by":"get_user()"
                }
            }
        }
    )
    increment_barcode_increment(id)

def edit_main_item(id, description=None, modelNumber=None, brand=None, isActive=None):
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

    items_collection.update_one(
        {"_id" : id},
        {"$set": edit_dict}
    )

def delete_main_item(id):
    items_collection.delete_one({"_id":id})

def edit_sub_item(id, barcode, container=None, status=None):
    edit_dict = {}
    if container is not None:
        edit_dict.update({"Items.$[subitem].Container": container})
    if status is not None:
        edit_dict.update({"Items.$[subitem].Status": status})
    edit_dict.update([("Items.$[subitem].Date modified",get_time()),("Items.$[subitem].Last modified by","getUser()")])

    items_collection.update_one(
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

def delete_sub_item(id, barcode):
    items_collection.update_one(
        {
            "_id": id
        },
        {  
            '$pull': {"Items": {"Barcode":barcode}}
        }
    )

def create_user(id, password, role):
    users_collection.insert_one(
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

def edit_user(id, password=None, role=None):
    edit_dict = {}
    if password is not None:
        edit_dict.update({"Password": password})
    if role is not None:
        edit_dict.update({"Role":role})
    edit_dict.update([("Date modified",get_time()),("Last modified by","getUser()")])

    users_collection.update_one(
        {"_id" : id},
        {"$set": edit_dict}
    )

def delete_user(id):
    users_collection.delete_one({"_id": id})

# create_main_item("Logitech G502 Mouse", "This is a lightweight 5kg mouse.", "LG5M", "Logitech")
# create_sub_item("Banana", "PALLET0001")
# edit_main_item("Banana", description="New Description", brand="New Brand") ~ This is how we would use optional parameters to only have to input what we want to change
# edit_sub_item("Banana", "BAN3", container="PALLET0001", status="PooPooPeePee")
# create_user("admin", "admin", "Admin")
# edit_user("TonyN123", password="newPassword123")
# delete_main_item("Banana")
# delete_user("TonyN22")
# delete_sub_item("Oranges", "ORA1")