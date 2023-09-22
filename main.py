import logging
import time
from logging.handlers import TimedRotatingFileHandler
import uuid
import socket
from paho.mqtt.publish import single
import json
# Create a custom log file name based on the current date
current_date = time.strftime("%Y-%m-%d")
log_filename = f"./log/{current_date}.log"

# Configure the logging settings with a custom log file name
log_formatter = logging.Formatter('%(asctime)s - %(message)s')
log_handler = TimedRotatingFileHandler(filename=log_filename, when='midnight', interval=1)
log_handler.setFormatter(log_formatter)

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)
host = socket.gethostname()

def log_message():
    """Function to log a message."""
    log = {"host": host, "message_id": str(uuid.uuid4())}
    single(topic= f"network/{host}", payload= json.dumps(log), hostname= "10.3.5.60")
    logger.info(log)

if __name__ == "__main__":
    try:
        while True:
            log_message()
            time.sleep(5)  # Sleep for 5 seconds
    except KeyboardInterrupt:
        print("Logging stopped due to keyboard interrupt.")
        
        
        