import pymongo


client = pymongo.MongoClient("mongodb+srv://maheshbabu9199:RXsHAm3fjrstQQoy@cluster0.6nqhrwi.mongodb.net/test")

mydb = client["Employee"]

information = mydb.employeesinformation

records = {"Name":"maheshbabu","Age":23, "City":"Kurnool", "State":"Andhra Pradesh"}

information.insert_one(records)