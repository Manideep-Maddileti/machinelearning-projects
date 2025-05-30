import logging
import os
from datetime import datetime

# Create a log file name based on the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m-%d_%Y_%H_%M_%S')}.log"

# Define the path for the logs directory
logs_dir = os.path.join(os.getcwd(), "logs")

# Ensure the logs directory exists
os.makedirs(logs_dir, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Set up logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

