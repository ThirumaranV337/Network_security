"""Creates the paths and settings used by one pipeline run."""

from datetime import datetime
import os 
from networksecurity.constant import training_pipeline

# Print the configured project and artifact-folder names when this module is imported.
print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

# Groups settings for one complete run of the training pipeline.
class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        # Use the current time to give this run its own artifact folder.
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        # Keep the general project name, base folder, run folder, and run time.
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.timestamp: str=timestamp

# Holds the data-ingestion-specific paths and MongoDB settings for that run.
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        # Put ingestion outputs inside this run's unique artifact folder.
        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME
                    ) 
        # Keep a copy of the full dataset under the feature-store folder.
        self.feature_store_file_path:str=os.path.join(
                    self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME   
                            )   
        # Define where the training portion of the dataset will be written.
        self.training_file_path: str=os.path.join(
                    self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME

        )  
        # Define where the held-out test portion will be written.
        self.testing_file_path: str=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME
        )
        # Read the split ratio and MongoDB destination from shared project constants.
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name: str =training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str =training_pipeline.DATA_INGESTION_DATABASE_NAME

class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str=os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_VALIDATION_DIR_NAME)##name of the folder
        self.valid_data_dir: str=os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir: str=os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path: str=os.path.join(self.valid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.invalid_train_file_path:str =os.path.join(self.invalid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path:str =os.path.join(self.invalid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path:str =os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
        )
        


















DATA_VALIDATION_DIR_NAME:str ="data_validation"
DATA_VALIDATION_VALID_DIR:str ="validated"
DATA_VALIDATION_INVALID_DIR:str ="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report.yaml"










