from MongoDBManager import MongoDBManager

# Create a MongoDBManager instance
mongo_manager = MongoDBManager(
    collection_name="<COLLECTION_NAME>",
    database_name="<DATABASE_NAME>"
)


initial_json_data = {}
response = mongo_manager.write(initial_json_data)
print(response) 
