# parse_suricata.py
        import json

        def load_suricata_alerts(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
