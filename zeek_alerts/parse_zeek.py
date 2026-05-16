def parse_conn_log(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    headers = None
    records = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('#fields\t'):
            headers = line[len('#fields\t'):].split('\t')
        elif not line.startswith('#') and headers:
            values = line.split('\t')
            record = {}
            for i, header in enumerate(headers):
                record[header] = values[i] if i < len(values) else ''
            records.append(record)

    return records
