# --- Day 20: Firewall Rules ---
# You'd like to set up a small hidden computer here so you can use it to get back into the network later. However, the corporate firewall only allows communication with certain external IP addresses.

# You've retrieved the list of blocked IPs from the firewall, but the list seems to be messy and poorly maintained, and it's not clear which IPs are allowed. Also, rather than being written in dot-decimal notation, they are written as plain 32-bit integers, which can have any value from 0 through 4294967295, inclusive.

# For example, suppose only the values 0 through 9 were valid, and that you retrieved the following blacklist:

# 5-8
# 0-2
# 4-7
# The blacklist specifies ranges of IPs (inclusive of both the start and end value) that are not allowed. Then, the only IPs that this firewall allows are 3 and 9, since those are the only numbers not in any range.

# Given the list of blocked IPs you retrieved from the firewall (your puzzle input), what is the lowest-valued IP that is not blocked?
from itertools import chain
concatenated = chain(range(30), range(2000, 5002))

with open("20_FirewallRules.txt",'r') as file:
	data = [row.strip() for row in file.readlines()]
	
def parseLine(line):
	lst = line.split('-')
	low = int(lst[0])
	hi  = int(lst[1])
	return (low, hi)

def isNumberOk(num, low, hi):
	if num < low or num > hi:
		return True
	else:
		return False
		
lowestIP	= 0
i			= 0

while i < len(data):
	line      = data[i]
	(low, hi) = parseLine(line)
	ok        = isNumberOk(lowestIP, low, hi)
	if ok:
		i    += 1
	else:
		i     = 0
		lowestIP = hi + 1
print(lowestIP)
	
# --- Part Two ---
# How many IPs are allowed by the blacklist?

x = range(4294967295 + 1)
y = range(0,0)
for i in data:
	(lo, hi) = parseLine(i)
	y = chain(y, range(lo, hi+1))