import json

def load_suricata_alerts(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    if isinstance(data, dict):
        return [data]
    return data
