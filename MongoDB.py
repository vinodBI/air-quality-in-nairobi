from pymongo import MongoClient

# Connect to server
client = MongoClient(host="localhost", port=27017)

# Connect to database
db = client["air-quality"]

# Get collection
nairobi = db["nairobi"]
