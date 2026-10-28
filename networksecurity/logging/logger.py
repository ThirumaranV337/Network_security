"""Sets up the file where the project records progress and errors."""

import os
import logging
from datetime import datetime

# Give each program start a timestamped log-file name.
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a folder for this run's log file.
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

# Combine the folder and file name into the full log-file path.
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Configure Python logging to write informational messages and above to that file.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]%(lineno)d %(name)s -%(levelname)s -%(message)s",
    level=logging.INFO,

)