import sys, dns.resolver

# ----------------------------------------------------------
#	This script will take the 'A' records of a nameserver,
#	for each subdomain provided in a wordlist.
#	You only need to provide the domain and the wordlist
#	file containing the possible subdomains.
# ----------------------------------------------------------

args = sys.argv

if len(args) < 3:
	print(f'USAGE: {args[0]} <domain> <wordlist>')
	sys.exit(1)

domain = args[1]

try:
	wordlist = open(args[2], 'r')
	lines = wordlist.read().splitlines()
except Exception as e:
	print(e)
	sys.exit(1)


for subdomain in lines:
	try:
		complete_domain = subdomain + '.' + domain
		# can be replaced for socket.gethostbyname()
		results = dns.resolver.query(complete_domain, 'a')
		for result in results:
			print(f'[+] {complete_domain} has address {result}')
	except:
		pass
