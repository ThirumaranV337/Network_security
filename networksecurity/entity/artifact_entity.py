"""Defines the information passed from one pipeline stage to another."""

from dataclasses import dataclass

# A small container for the two files produced by data ingestion.
@dataclass
class DataIngestionArtifact:
    # Path to the portion used for model training.
    trained_file_path:str
    # Path to the portion held aside for testing.
    test_file_path:str