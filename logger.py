from datetime import datetime
import csv
import os

REPORT_FOLDER = "reports"
REPORT_FILE = os.path.join(REPORT_FOLDER, "events.csv")

os.makedirs(REPORT_FOLDER, exist_ok=True)

if not os.path.exists(REPORT_FILE):

    with open(REPORT_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Timestamp",
            "Event",
            "Target",
            "Risk",
            "MITRE ID",
            "Technique"
        ])


def log_event(
    event_type,
    target_name,
    risk,
    technique="N/A",
    description="N/A"
):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("=" * 65)
    print(f"Time       : {current_time}")
    print(f"Event      : {event_type}")
    print(f"Target     : {target_name}")
    print(f"Risk       : {risk}")
    print(f"MITRE ID   : {technique}")
    print(f"Technique  : {description}")
    print("=" * 65)

    with open(REPORT_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            current_time,
            event_type,
            target_name,
            risk,
            technique,
            description
        ])