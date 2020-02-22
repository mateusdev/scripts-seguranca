#!/usr/bin/env python3

import socket
import sys

if len(sys.argv) < 3:
    print("USAGE: {} <ip> <port>".format(sys.argv[0]))
    sys.exit(1)

try:
    ip, port = sys.argv[1], int(sys.argv[2])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.recv(1024)

    qt_bytes = 1

    while True:
        payload = "A" * qt_bytes
        print("[+] Trying with {} bytes...".format(qt_bytes))
        sock.send(payload.encode())
        sock.recv(1024)
        qt_bytes += 1


except Exception as e:
    print("Error: {}".format(e))

finally:
    print("Finishing...")
    sock.close()
