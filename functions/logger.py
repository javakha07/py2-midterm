import os
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(__file__), '..', 'logs', 'app.log')

def log_action(action, result):
    try:
        with open(LOG_FILE, 'a') as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] {action}: {result}\n"
            log_file.write(log_entry)
    except Exception as e:
        print(f"An error occurred while logging: {e}")
