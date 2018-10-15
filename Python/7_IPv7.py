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
		
	# # FOR PART 2 #
	# def supportSSL(self):
		
	
	def isABA(self, st):
		"""Returns matched ABA patterns as list of tuples"""
		p = re.compile(r'(.)(?!\1)(.)\1')	
		try:
			chrs = p.findall(st)
			return chrs[:]													# [(ext1,int1),(ext2,int2),...]
		except:
			return None
			
	def isABARow(self, row):
		"""Returns matched ABA patterns for whole address as a list of tuples"""
		chrs = []
		for st in row:
			if self.isABA(st) == None:
				continue
			else:
				chrs.extend(self.isABA(st))
		return chrs
			
	def isBAB(self, a, b, st):
		"""Returns true if given BAB pattern is matched in st"""
		pattern = r"" + b + a + b
		p = re.compile(pattern)
		return bool(p.search(st))
		
	def isBABRow(self, a, b, row):
		"""Returns true if given BAB pattern is matched in row"""
		for st in row:
			if self.isBAB(a, b, st):
				return True
		return False

print(sum([IPAddress(row).supportTLS() for row in data]))					# how many IPs support TLS?

cnt = 0
for row in data:							# iterating through rows
	ip = IPAddress(row)						# IP address
	[ins, outs] = ip.splitAddress()			# splitting with brackets
	matchedABA = ip.isABARow(ins)			# list of matched ABA patterns
	for tuples in matchedABA:				# trying each corresp. BAB pattern
		if ip.isBABRow(*tuples, outs):
			cnt += 1
			break
	# print(cnt, row, matchedABA)
print(cnt)

# --- Part Two ---
# You would also like to know which IPs support SSL (super-secret listening).

# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

# For example:

# aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
# xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
# aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
# zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
# How many IPs in your puzzle input support SSL?

# Your puzzle answer was 260.