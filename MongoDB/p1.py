from pymongo import MongoClient
import ssl

cluster = MongoClient("mongodb+srv://softgod1:banana123@group5warehouse.kvdys.mongodb.net/test", ssl_cert_reqs=ssl.CERT_NONE)
db = cluster["bagel-hut-inc"]
coupon_db = db["coupons"]
balances_db = db["balances"]