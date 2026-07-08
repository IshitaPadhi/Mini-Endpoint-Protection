import time
import psutil

from config import SCAN_INTERVAL
from risk_engine import analyze_process
from logger import log_event


def monitor_processes():

    print("\nLearning existing processes...\n")

    known_processes = set()

    for process in psutil.process_iter(['name']):

        try:

            if process.info['name']:
                known_processes.add(process.info['name'])

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    print(f"Baseline Created ({len(known_processes)} processes)")
    print("\nMonitoring for NEW processes...\n")

    while True:

        current_processes = set()

        for process in psutil.process_iter(['name']):

            try:

                process_name = process.info['name']

                if process_name:

                    current_processes.add(process_name)

                    if process_name not in known_processes:

                        analysis = analyze_process(process_name)

                        log_event(
                            event_type="New Process Detected",
                            target_name=process_name,
                            risk=analysis["risk"],
                            technique=analysis["technique"],
                            description=analysis["description"]
                        )

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess
            ):
                continue

        known_processes = current_processes

        time.sleep(SCAN_INTERVAL)