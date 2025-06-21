#logging  is crucial for debugging and monitoring events when the application runs

import logging
import os
from datetime import datetime

# Create logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Create timestamped log file path
log_filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, log_filename)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Logging started with timestamped file.")