import socket
import datetime
import sys

# Configuration
HOST = '0.0.0.0'
PORT = 1502  # Port 1502 used to avoid 'root' permission issues on macOS
LOG_FILE = "pipeline_attacks.log"

def log_attack(remote_ip, data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hex_payload = data.hex(' ')
    entry = f"[{timestamp}] ALERT: Unauthorized Modbus Access from {remote_ip} | Payload: {hex_payload}\n"
    
    print(entry.strip())
    with open(LOG_FILE, "a") as f:
        f.write(entry)

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"--- Pipeline-Sentinel Active ---")
        print(f"[*] Emulating Oil Rig PLC on Port {PORT}")
        print(f"[*] Listening for unauthorized mapping requests...")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    while True:
        try:
            client_sock, client_addr = server.accept()
            data = client_sock.recv(1024)
            if data:
                log_attack(client_addr[0], data)
                # Fake Modbus Success Response
                client_sock.send(b"\x00\x01\x00\x00\x00\x06\x01\x03\x02\x00\x00")
            client_sock.close()
        except KeyboardInterrupt:
            print("\n[!] Shutting down...")
            break

if __name__ == "__main__":
    start_honeypot()
