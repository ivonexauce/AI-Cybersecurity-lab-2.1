# parse_zeek.py
        def parse_conn_log(file_path):
            with open(file_path, 'r') as f:
                lines = f.readlines()
            return [line.strip().split('\t') for line in lines if not line.startswith('#')]