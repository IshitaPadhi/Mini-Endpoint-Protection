# config.py

# Processes commonly abused by attackers
SUSPICIOUS_PROCESSES = [
    "powershell.exe",
    "cmd.exe",
    "wmic.exe",
    "reg.exe",
    "net.exe",
    "rundll32.exe",
    "certutil.exe",
    "mshta.exe",
    "cscript.exe",
    "wscript.exe"
]

# Process monitoring interval (seconds)
SCAN_INTERVAL = 2


# MITRE ATT&CK Mapping

MITRE_MAPPING = {

    "powershell.exe": {
        "technique": "T1059",
        "description": "Command and Scripting Interpreter"
    },

    "cmd.exe": {
        "technique": "T1059",
        "description": "Windows Command Shell"
    },

    "reg.exe": {
        "technique": "T1112",
        "description": "Modify Registry"
    },

    "wmic.exe": {
        "technique": "T1047",
        "description": "Windows Management Instrumentation"
    },

    "certutil.exe": {
        "technique": "T1105",
        "description": "Ingress Tool Transfer"
    },

    "mshta.exe": {
        "technique": "T1218.005",
        "description": "Mshta Proxy Execution"
    },

    "rundll32.exe": {
        "technique": "T1218.011",
        "description": "Signed Binary Proxy Execution"
    }

}