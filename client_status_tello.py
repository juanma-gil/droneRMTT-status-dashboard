import socket
import time
import json

# IP and port to listen on
SERVER_IP = "0.0.0.0"
SERVER_PORT = 8890

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP and port
sock.bind((SERVER_IP, SERVER_PORT))

print(f"UDP server listening on {SERVER_IP}:{SERVER_PORT}")

def get_json_data():
    # Receive data from the UDP client
    data = sock.recvfrom(1024)[0]

    # Convert the received data to a string and split it by semicolon
    data_str = data.decode()
    data_parts = data_str.split(";")

    # Ignore the first 5 elements
    data_parts = data_parts[5:]

    # Initialize an empty dictionary
    data_dict = {}

    # Process each part and add to the dictionary if it contains a colon
    for part in data_parts:
        if ":" in part:
            key, value = part.split(":", 1)  # Split only at the first colon encountered
            data_dict[key] = value

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data_dict, indent=4)

    # print(f"Received data from {addr}:")
    # print(json_data)
    
    return json_data

# while True:
#     time.sleep(1e-3)
#     get_json_data()
