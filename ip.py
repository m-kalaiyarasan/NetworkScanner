import re

def extract_ip_addresses(file_path):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'  # Regular expression pattern for matching IP addresses
    ip_addresses = []

    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(ip_pattern, line)
            ip_addresses.extend(matches)

    return ip_addresses

# Example usage:
file_path = 'exampleip.txt'  # Replace with the path to your file
ips = extract_ip_addresses(file_path)
print("IP Addresses found:", ips[0])
