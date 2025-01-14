from pymongo import MongoClient

uri = "mongodb://localhost:27017"
client = MongoClient(uri)
DD = client ['School']
collection = DD ['Table1']

result = collection.insert_one( {"Name":'Mehtab', "Age":'26',"Number":'319766666',"Address":'Mithi Tharparkar'} )
print(result.inserted_id)


