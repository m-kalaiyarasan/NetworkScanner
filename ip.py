import re


def extract_ip_addresses(text):
    # Regular expression pattern for matching IP addresses
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

    # Find all IP addresses in the text using the pattern
    ip_addresses = re.findall(ip_pattern, text)

    return ip_addresses


# Example usage
text = "The server's IP address is 192.168.1.1 and the client's IP address is 10.0.0.1  192.178.7.1"
ip_addresses = extract_ip_addresses(text)
print("IP addresses found in the text:", ip_addresses)
