"""Loads the source CSV into MongoDB so the ingestion stage can read it."""

# Standard tools for file paths, error details, and converting records to JSON.
import os 
import sys
import json 

# Read MongoDB connection settings from the project's .env file.
from dotenv import load_dotenv
load_dotenv(override=True)

# Connection address used by the script that uploads the original dataset.
MONGO_DB_URI=os.getenv("MONGO_URI")


# Certificate location used when connecting to a secured MongoDB service.
import certifi
# This path is recorded here, but the current MongoClient call does not use it.
ca=certifi.where()

# Data tools and the project's common logging and error handling.
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# This helper handles the first step in the diagram: putting source CSV rows in MongoDB.
class NetworkDataExtract():

    def __init__(self):
        try:
            # No setup is needed yet; this constructor is kept for the class instance.
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    # Read the CSV and turn each row into a dictionary MongoDB can store.
    def csv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)##removing the index
            records=list(json.loads(data.T.to_json()).values())#converting the data into json
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    # Send the converted rows to the named MongoDB database and collection.
    def insert_data_mongodb(self,records,database,collection):
        try:
            # Keep the requested destination and records on this object.
            self.database=database
            self.collection=collection
            self.records=records

            # Open the MongoDB connection and select its database and collection.
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URI)
            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            # Add the CSV rows as documents and report how many were sent.
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)


# Running this file directly uploads the project's source phishing-data CSV.
if __name__=='__main__':
    # These names must match the database and collection read during ingestion.
    FILE_PATH="Network_Data/phisingData.csv"
    DATABASE="MARANAI"
    Collection="NetworkData"
    # Convert the CSV first, then insert its rows into MongoDB.
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)
