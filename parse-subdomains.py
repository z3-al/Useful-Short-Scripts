#!/usr/bin/python

import re



with open('subdomains.txt') as f: 
	lines = f.read().splitlines()

cleanlist = []

for line in lines: 
	templist = line.split('<BR>')
	print templist
	for item in templist:
		cleanlist.append(item)


r = re.compile("([a-z0-9]+[.])*adorebeauty.com.au")

newlist = list(filter(r.match, cleanlist))
final_list = sorted(set(newlist))

with open('output.txt', 'w') as o:
	for i in final_list:
		o.write("%s\n" % i)

