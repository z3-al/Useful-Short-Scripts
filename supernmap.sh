#!/bin/bash

IPRANGE=$1

if [[ $# -eq 0 ]] ; then
	echo "Please provide an IP range."
	exit 0
fi

IPCOM="echo "$IPRANGE" | awk -F'/' '{print \$1}'"
IP="$(eval $IPCOM)"
# echo $IP
mkdir $IP
cd $IP

# check which hosts are up
ALIVE='nmap -sn -n $1 -oN temp'
eval $ALIVE

# grep out the alive IPs
IPS="cat temp | grep 'Nmap scan report' | awk '{ print \$5 }' > IPs.txt"
eval $IPS
rm -rf temp
