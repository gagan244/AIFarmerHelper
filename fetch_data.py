from pymongo import MongoClient
connection_string= "mongodb+srv://meenakshinandwana53:GGeNFxZCWyLbpADi@cluster1.06ovr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
client = MongoClient(connection_string)
database = client['Farmer2']
collection = database['FarmerData1']

documents = collection.find()  # select * from table;
for document in documents:
    print(document)
print("thank you!")

# execute this file to fatch your data from database
