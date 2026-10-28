"""Starts the first implemented stage of the Network Security project."""

# Import the data-ingestion stage, its configuration, and shared logging/error helpers.
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig

from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

# This block runs only when this file is started directly with Python.
if __name__=="__main__":
    try:
        # Build the run settings, then pass them into the data-ingestion component.
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        # Run the first project stage: MongoDB data -> saved CSV files.
        logging.info("Initiate the Data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        # Show the paths of the training and test files produced by ingestion.
        print(dataingestionartifact)
    except Exception as e:
        # Add the project-specific file-and-line details to any error that occurs.
        raise NetworkSecurityException(e,sys)