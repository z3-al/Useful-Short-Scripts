#!/bin/bash

OLDIP=$(ifconfig eth0 | grep 'inet ' | awk '{print $2}')


echo "OLD IP: $OLDIP"

echo "eth0 going down..."
ifconfig eth0 down
echo "changing mac.."
sleep 1
macchanger -r eth0 >/dev/null
echo "restart network service..."
sleep 1
service networking restart
sleep 1
echo "bringing up eth0..."
echo "Run ifconfig to check new IP. Takes a while somtimes."
