#logging is crucial for tracking events when application runs

import logging
import os
from  datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%s')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s-%(messages)s",
    lavel=logging.INFO
)