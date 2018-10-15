# --- Day 7: Internet Protocol Version 7 ---
# While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

# For example:

# abba[mnop]qrst supports TLS (abba outside square brackets).
# abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
# aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
# ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
# How many IPs in your puzzle input support TLS?

# Your puzzle answer was 118.
import re

with open("7_IPv7.txt",'r') as file:
	data = [row.rstrip() for row in file]

class IPAddress(object):
	def __init__(self, address):
		self.address = address
		self.inside  = self.splitAddress()[0]
		self.outside = self.splitAddress()[1]
		
	def supportTLS(self):
		"""Returns whether address supports TLS or not"""
		return self.isABBAOutside() and self.noABBAInside()
		
	def isABBAOutside(self):
		"""Returns true if ABBA pattern occurs outside brackets"""
		for i in self.outside:
			if self.isABBA(i):
				return True
				break
		return False
		
	def noABBAInside(self):
		"""Returns true if ABBA pattern does not occur inside"""
		for i in self.inside:
			if self.isABBA(i):
				return False
				break
		return True
		
	def splitAddress(self):
		"""Splits the address based on the brackets"""
		inside  = [m[1:-1] for m in re.findall('\[.*?\]', self.address)]	# find characters inside brackets
		outside = [s.split(']')[-1] for s in self.address.split('[')]		# find characters outside brackets
		return [inside, outside]
	
	def isABBA(self, st):
		"""Returns true if ABBA pattern is matched in st"""
		p = re.compile(r'(.)(?!\1)(.)\2\1')									# find ABBA patern
		return bool(p.search(st))											# return True if pattern found		

print(sum([IPAddress(row).supportTLS() for row in data]))					# how many IPs support TLS?