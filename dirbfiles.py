#!/usr/share/python3
# coding: utf-8

# +================================================+
#	This script allows you to discover directories
#	and files in a webserver. Just provide the
#	wordlist containing the possible names of files
#	or directories.
# +================================================+

import urllib.request
import sys
from http import HTTPStatus

args = sys.argv

if len(args) < 3:
	print(f'USAGE: {args[0]} <http://www.site.com> <wordlist.txt>')
	sys.exit(1)

site = sys.argv[1]

try:
	wordlist = open(args[2], 'r')
	wl_lines = wordlist.read().splitlines()
except Exception as e:
	print(e)
	sys.exit(1)

try:
	status = urllib.request.urlopen(site).getcode()
	print(f'[~] Connection status to {site}: HTTP Code {status}\n')
	if status == HTTPStatus.NOT_FOUND:
		sys.exit(1)
except Exception as e:
	print(e)
	sys.exit(1)

for line in wl_lines:
	try:
		status = urllib.request.urlopen(site + '/' + line).getcode()
		if status == HTTPStatus.OK:
			print(f'[+] {site + "/" + line} has been found!')
	except:
		pass
	
