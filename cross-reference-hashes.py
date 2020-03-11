#!/usr/bin/python

import sys

file1 = sys.argv[1]   # full NTLM file with users
file2 = sys.argv[2]	  # just the NTLM hashes w/ cracked passwords

# full NTLM file with users
with open (sys.argv[1]) as f: 
	full_ntlm = f.readlines()

# just the NTLM hashes
with open (sys.argv[2]) as f2:
	cracked_hashes = f2.readlines()

# print full_ntlm

for item in cracked_hashes:
	cracked = item.split(':')[0]
	for line in full_ntlm: 
		if cracked in line: 
			print line.strip() + item.strip()
