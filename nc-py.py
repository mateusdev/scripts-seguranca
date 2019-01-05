#!/usr/bin/python3
# coding: utf-8

# -----------------------------------------------------------------------
# This program can connect to a service, both TCP and UDP are supported.
# Allows you to manually do your requests to a server.
# -----------------------------------------------------------------------

import sys, socket

args = sys.argv

if len(args) < 3:
	print(f'USAGE: {args[0]} [-u] <ip> <port>')
	sys.exit(1)

if not args[-1].isdigit():
	print('ERROR: port must be an integer!')
	sys.exit(1)

if int(args[-1]) < 1 or int(args[-1]) > 65535:
	print('ERROR: port number must be between 1 and 65535')
	sys.exit(1)

if args[1] == '-u':
	ip = args[2]
	port = int(args[3])
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		while True:
			req = input() + '\r\n'
			if req == '\r\n':
				break
			req = req.encode()
			sock.sendto(req, (ip, port))
			resp, addr = sock.recvfrom(2048)
			print(f'Got message from {addr[0]}:{addr[1]}...')
			print(f'{resp.decode()}', end='')
	except Exception as e:
		print(e)
		sys.exit()
else:
	ip = args[1]
	port = int(args[2])
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((ip, port))
		while True:
			req = input() + '\r\n'
			if req == '\r\n':
				break
			req = req.encode()
			sock.send(req)
			print(sock.recv(2048).decode())
	except Exception as e:
		print(e)
		sys.exit()
