import csv
import random
import time
from datetime import datetime

file_name = "auth_logs.csv"

# Columns for UIDAI-like logs
headers = [
    "user_id",
    "timestamp",
    "service_type",
    "auth_status",
    "region",
    "device",
    "response_time",
    "error_code"
]

regions = ["MH", "DL", "KA"]
services = ["OTP", "Biometric"]
devices = ["Mobile", "POS"]

# Create file with headers if not exists
try:
    with open(file_name, 'x', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
except FileExistsError:
    pass

print("🔄 Real-time data generation started... Press Ctrl+C to stop")

while True:
    row = [
        random.randint(100000, 999999),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        random.choice(services),
        random.choices(["Success", "Fail"], weights=[85, 15])[0],
        random.choice(regions),
        random.choice(devices),
        random.randint(100, 1500),
        random.choice(["None", "BIO_FAIL", "OTP_TIMEOUT", "NETWORK"])
    ]

    # Append row to CSV
    with open(file_name, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)

    print("New log added:", row)
    time.sleep(2)  # add new log every 2 seconds
