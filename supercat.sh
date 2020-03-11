#!/bin/bash

mapfile -t myArray < all-ranges.txt

for i in "${myArray[@]}"
do
   cat $i/IPs.txt >> all-ips.txt
done

