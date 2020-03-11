# Useful-Short-Scripts
Useful short scripts. 

supernmap.sh: nmap ping sweep a CIDR, create a dir, then parse the results into a simple list of IP addresses to be stored in the dir

supercat.sh: Combine several supernmap outputs

superport.sh: nmap a single port for supercat output and parse output into another simple list of IPs

cross-reference-hashes.py: When you pull NTDS.DIT, then extract the NTLM hashes and crack them, this script cross references the cracked hashes back with the original NTDS.DIT output and creates a new output in the format: domain\username:password

list-regions.sh: list ec2 instances per region for an AWS deployment. Useful if you're working with an unfamiliar AWS environment and want to know what is where

change-ip.sh: change your mac, then get a new IP from DHCP

sophos-to-firewall-audit.py: not useful at all, very niche scenario and absolutely disgusting script. Why did I not use a python HTTP parsing library you ask? Some things in life just cannot be explained. But here it is. In case you ever need to grab a HTML table from a Sophos firewall audit report and parse it into an open source format for review. 
