from pymongo.mongo_client import MongoClient
import json
import pandas as pd

uri = "mongodb+srv://2341037:hile3mOjBWyaQyOH@cluster0.vlmheoy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

#creating_database and collection name
DATABASE_NAME="wafer"
COLLECTION_NAME="wafer_data"


df=pd.read_csv("C:\Users\panka\OneDrive\Desktop\ML_Projects\Sensor-Project\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)
json_records=list(json.loads(df.T.to_json()).values())
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)