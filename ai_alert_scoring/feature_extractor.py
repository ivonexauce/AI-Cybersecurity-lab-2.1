import ipaddress

def _is_private_ip(ip_str):
    try:
        return int(ipaddress.ip_address(ip_str).is_private)
    except ValueError:
        return 0

def extract_features(alert):
    src_ip = alert.get('src_ip', '')
    dest_ip = alert.get('dest_ip', '')

    return [
        alert.get('severity', 0),
        len(src_ip),
        len(dest_ip),
        _is_private_ip(src_ip),
        _is_private_ip(dest_ip),
        alert.get('alert_count', 1),
    ]
