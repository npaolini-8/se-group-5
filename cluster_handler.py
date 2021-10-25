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

def generate_barcode(name, increment):
    string = name[0:3].upper()
    return f'{string}{increment}'

def get_item_increment(name):
    main_item = items_collection.find({"Name":name})[0]
    return main_item["Barcode Increment"]

def increment_barcode_increment(name):
    items_collection.update_one(
        {"Name": name},
        {"$set": {"Barcode Increment": get_item_increment(name)+1}}
    )

def create_main_item(name, description, modelNumber, brand):
    try:
        items_collection.insert_one(
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
    except:
        print(f"Error: {name} already exist!")

def create_sub_item(name, container):
    items_collection.update_one(
        {"Name" : name},
        {"$push": 
            {"Items":
                {
                "Barcode":generate_barcode(name, get_item_increment(name)+1),
                "Container":container,
                "Status":"Available",
                "Date modified":get_time(),
                "Last modified by":"get_user()"
                }
            }
        }
    )
    increment_barcode_increment(name)

def edit_main_item(name, description=None, modelNumber=None, brand=None, isActive=None):
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
        {"Name" : name},
        {"$set": edit_dict}
    )

def delete_main_item(name):
    items_collection.delete_one({"Name":name})

def edit_sub_item(name, barcode, container=None, status=None):
    edit_dict = {}
    if container is not None:
        edit_dict.update({"Items.$[subitem].Container": container})
    if status is not None:
        edit_dict.update({"Items.$[subitem].Status": status})
    edit_dict.update([("Items.$[subitem].Date modified",get_time()),("Items.$[subitem].Last modified by","getUser()")])

    items_collection.update_one(
        {
            "Name": name
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

def delete_sub_item(name, barcode):
    items_collection.update_one(
        {
            "Name": name
        },
        {  
            '$pull': {"Items": {"Barcode":barcode}}
        }
    )

def create_user(name, password, role):
    users_collection.insert_one(
        {
            "Name": name,
            "Password": password,
            "Role": role,
            "isActive": True,
            "isLocked": False,
            "Date modified": get_time(),
            "Last modified by": "getUser()",
        }
    )

def edit_user(name, password=None, role=None):
    edit_dict = {}
    if password is not None:
        edit_dict.update({"Password": password})
    if role is not None:
        edit_dict.update({"Role":role})
    edit_dict.update([("Date modified",get_time()),("Last modified by","getUser()")])

    users_collection.update_one(
        {"Name" : name},
        {"$set": edit_dict}
    )

def delete_user(name):
    users_collection.delete_one({"Name": name})

# create_main_item("Logitech G502 Lightspeed", "This is a lightweight 5kg mouse.", "LG5M", "Logitech")
# create_sub_item("Logitech G502 Lightspeed", "PALLET0001")
# edit_main_item("Logitech G502 Lightspeed", description="This is a lightweight 5kg mouse that preceeds the Logitech G503 Lightspeed.", brand="Logitech")
# edit_sub_item("Logitech G502 Lightspeed", "LOG1", container="LGT Pallet 3", status="Inactive")
# create_user("admin", "admin", "Admin")
# edit_user("TonyN123", password="newPassword123")
# delete_main_item("Logitech G502 Lightspeed")
# delete_user("TonyN22")
# delete_sub_item("Logitech G502 Lightspeed", "LOG1")