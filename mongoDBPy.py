from pymongo import MongoClient

uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client['naeen']
collection = db['table1']

result = collection.insert_one({'Name':'Naveen','Age':'25','# Number':'3133254772' ,'From':'PECHS Karachi'} )
print(result.inserted_id)


#for i in collection.find({'Age':'25'}):
 #  print(i)

#for b in collection.delete_one({'Name':'Naveen', '# Number':'3133254772'}):
#   print(b)
 
#for a in collection.find({'Name': 'Naveen', 'Age': '25', '# Number': '3133254772', 'From': 'PECHS Karachi'}):
 #  print(a)  
