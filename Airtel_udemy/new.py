import os
from datetime import datetime

LOG_FILE = "system_logs.txt"
OUTPUT_FILE = "collected_logs.txt"

def collect_logs():
    if not os.path.exists(LOG_FILE):
        print("Log file not found!")
        return

    with open(LOG_FILE, "r") as src, open(OUTPUT_FILE, "a") as dst:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dst.write(f"\n--- Logs collected at {timestamp} ---\n")
        for line in src:
            dst.write(line)

    print("Logs collected successfully!")

if __name__ == "__main__":
    collect_logs()
