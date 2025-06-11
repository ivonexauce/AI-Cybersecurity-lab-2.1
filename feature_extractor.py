# feature_extractor.py
        import json

        def extract_features(alert):
            return [
                alert.get('severity', 0),
                len(alert.get('src_ip', '')),
                len(alert.get('dest_ip', ''))