#!/usr/bin/python3
# coding: utf-8

# +========================================================+
# A portscan that can check for open TCP ports in a host.
# You can specify the ports:
# 	Like a single port, 22
#	A range of ports, 80-1000
#	Each single port, 22,8080,3306
# +========================================================+


import sys, socket

args = sys.argv
if len(args) < 2:
	print(f'USAGE: {args[0]} <target_ip> [port1,port2,... port1-port2]')
	sys.exit(1)

target = args[1]

try:
	if(args[2].isdigit()):
		ports = range(int(args[2]), int(args[2]) + 1)

	elif ',' in args[2]:
		ports = args[2].split(',')
		for i in range(len(ports)):
			ports[i] = int(ports[i])
	
	elif '-' in args[2]:
		try:
			ports = range(int(args[2].split('-')[0]), int(args[2].split('-')[1]))
		except:
			ports = range(1, 10000)
	else:
		ports = range(1, 10000)
except:
	ports = range(1, 10000)

print(f'[+] Portscan started on host {target}...')

for port in ports:
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if(sock.connect_ex((target, port)) == 0):
			print(f'Port {port} is open!')

		sock.close()
	except:
		pass

print('--- END OF PORTSCAN ---')
