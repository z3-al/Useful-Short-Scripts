#!/bin/bash

# Don't run several of these at the same time... if you're unlucky you'll get a race condition 

PORT=$1

if [[ $# -eq 0 ]] ; then
	echo "Please provide a port."
	exit 0
fi

# echo $1

SCAN='nmap -n -iL all-ips.txt -p $1 -oN temp'
eval $SCAN

SM="cat temp | grep -B4 open | grep report | awk '{print \$5}' > $1.txt"
eval $SM

rm -rf temp
