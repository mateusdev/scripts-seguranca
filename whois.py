#!/usr/bin/python3
# coding: utf-8

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Sends a WHOIS query to a whois server and outputs the response
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import socket, sys

args = sys.argv

if len(args) < 2:
	print(f'USAGE: {args[0]} <domain>')
	sys.exit(1)

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('64.124.14.21', 43))
	sock.send(f'{args[1]}\r\n'.encode())

	msg = sock.recv(2048)
	print(msg.decode())
	sock.close()
except Exception as e:
	print(e)

