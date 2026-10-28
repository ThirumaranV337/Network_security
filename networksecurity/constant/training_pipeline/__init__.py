"""Shared names and default settings used by the pipeline stages."""

import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for training pipeline
"""
# Name of the label column the model is expected to predict.
TARGET_COLUMN = "Result"
# General project label and folder for outputs from pipeline runs.
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
# Source dataset name and the two split-file names.
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

# Locations/names reserved for schema and model files in later stages.
SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

SAVED_MODEL_DIR =os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"




"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
# MongoDB location and folder names used by the ingestion stage.
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "MARANAI"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
# The fraction of rows held aside for testing; the rest are used for training.
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

"""Data  Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME:str ="data_validation"
DATA_VALIDATION_VALID_DIR:str ="validated"
DATA_VALIDATION_INVALID_DIR:str ="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report.yaml"

