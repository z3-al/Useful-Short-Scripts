#!/usr/bin/python

import re
import sys
import os


filename = 'data.html'

with open(filename) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

firewall = dict()

try:
    os.remove('test')
except OSError:
    pass
f = open('test','a+')


stopcount = 0
for line in content: 

	# there will be 7 <td> tags per line
	newline = line.replace('<td>','')
	line_list = newline.split("</td>")

	# lets cook up these dictionaries...
	rule = line_list[0]
	active = line_list[1]

	#source requires some parsing... unsure if this will work for multi-sources
	temp = line_list[3].split("/>")
	src_list = []
	for s in temp:
		if "</a>" in s: 
			src_list.append(s.split("</a>")[0])

	# gotta start writing the file now so that we can write out src as we go....
	f.write(rule + ';' + active + ';')
	for src in src_list: 
		if src == src_list[-1]:
			f.write(src)
		else:
			f.write(src)
			f.write(',')
	f.write(';')

	# FINAL DESTINATION TIME
	temp = line_list[4].split("/>")
	# print temp
	dst_list = []
	for s in temp:
		if "</a>" in s:
			dst_list.append(s.split("</a>")[0])

	# let's write out dest now
	for dst in dst_list:
		if dst == dst_list[-1]:
			f.write(dst)
		else:
			f.write(dst)
			f.write(',')
	f.write(';')


	#SERVICE TIME, THE FINAL STRETCH
	temp = line_list[5].split("/>")
	svc_list = []
	for s in temp:
		if "</a>" in s:
			svc_list.append(s.split("</a>")[0])

	for svc in svc_list:
		if svc == svc_list[-1]:
			f.write(svc)
		else:
			f.write(svc)
			f.write(',')



	f.write('\n')
	stopcount += 1 

	#if stopcount == 5: 
	#	f.close()
	#	sys.exit()

f.close()
