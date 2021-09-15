#importing the module

import re

#opening and reading the file
with open('/home/IP.txt') as fh;
	fstring = fh.readlines()

#declaring the regex pattern for IP address
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3})')

#initializing the list object 
lst=[]

#extracting the IP address 
for line in fstring:
	lst.append(append.search(line)[0])

#displaying the extracted IP addresses
print(lst)
