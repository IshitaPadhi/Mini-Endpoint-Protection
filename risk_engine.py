from config import SUSPICIOUS_PROCESSES
from config import MITRE_MAPPING


def analyze_process(process_name):

    process_name = process_name.lower()

    risk = "LOW"
    technique = "N/A"
    description = "No MITRE Mapping"

    if process_name in SUSPICIOUS_PROCESSES:
        risk = "HIGH"

    if process_name in MITRE_MAPPING:
        technique = MITRE_MAPPING[process_name]["technique"]
        description = MITRE_MAPPING[process_name]["description"]

    return {
        "risk": risk,
        "technique": technique,
        "description": description
    }