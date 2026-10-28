"""Reads the MongoDB dataset and creates the first pipeline artifacts."""

# Shared project error and logging helpers, plus the settings and result containers.
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

##configuration of the Data Ingestion Config

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import os 
import sys
import numpy as np
import pymongo
from typing import List
from sklearn.model_selection import train_test_split
import pandas as pd

# Load the database connection address from the project environment file.
from dotenv import load_dotenv
load_dotenv(override=True)

# This must be the same MongoDB connection setting used by the upload script.
MONGO_DB_URL=os.getenv("MONGO_URI")

# Implements the data-ingestion box in the project diagram.
class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):

        try:
            # Keep the paths and MongoDB names chosen for this pipeline run.
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    # Read all documents from MongoDB and represent them as a table (DataFrame).
    def export_collection_as_dataframe(self):
        try:
            # Get the database and collection names from the ingestion settings.
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            collection=self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collection.find()))
            # MongoDB adds an internal ID to each document; it is not a data feature.
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"])

            # Treat the text marker "na" as a missing value in the table.
            df.replace({"na":np.nan},inplace=True)
            return df
            

        except Exception as e:
            raise NetworkSecurityException(e,sys)

    # Coordinate ingestion: read MongoDB, save a feature-store copy, then split files.
    def initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            # Return the two output paths so later pipeline stages can find the files.
            dataingestionartifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,test_file_path=self.data_ingestion_config.testing_file_path)
            return dataingestionartifact
        except Exception as e:
                    raise NetworkSecurityException(e,sys)

    # Save the complete table as the feature-store copy for this run.
    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
         try:
              # Create the output folder if it does not exist yet.
              feature_store_file_path=self.data_ingestion_config.feature_store_file_path
              dir_path=os.path.dirname(feature_store_file_path)
              os.makedirs(dir_path,exist_ok=True)
              # Write the table as CSV; index=False avoids an extra row-number column.
              dataframe.to_csv(feature_store_file_path,index=False,header=True)
              return dataframe
         except Exception as e:
              raise NetworkSecurityException(e,sys)

    # Divide the table into training and test data and save both CSV files.
    def split_data_as_train_test(self,dataframe:pd.DataFrame):
         try:
              # Keep the configured proportion for testing; the remaining rows are training.
              train_set,test_set=train_test_split(
                   dataframe,test_size=self.data_ingestion_config.train_test_split_ratio
                   
              )
              logging.info("Performed train test split on the Dataframe")

              logging.info(
                   "Excited split_data_as_train_test method of  Data_Ingestion class"
              )

              # Both output files live in the same ingested-data folder.
              dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)

              os.makedirs(dir_path,exist_ok=True)

              logging.info(f"Exporting train and test file path.")

              # Save each portion separately for later pipeline stages.
              train_set.to_csv(
                   self.data_ingestion_config.training_file_path,index=False,header=True
              )
              test_set.to_csv(
                   self.data_ingestion_config.testing_file_path,index=False,header=True
              )
              logging.info(f"Exported train and Test file path.")

         except Exception as e:
              raise NetworkSecurityException(e,sys)
