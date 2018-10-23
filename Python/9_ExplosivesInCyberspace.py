# --- Day 9: Explosives in Cyberspace ---
# Wandering around a secure area, you come across a datalink port to a new part of the network. After briefly scanning it for interesting files, you find one file in particular that catches your attention. It's compressed with an experimental format, but fortunately, the documentation for the format is nearby.

# The format compresses a sequence of characters. Whitespace is ignored. To indicate that some sequence should be repeated, a marker is added to the file, like (10x2). To decompress this marker, take the subsequent 10 characters and repeat them 2 times. Then, continue reading the file after the repeated data. The marker itself is not included in the decompressed output.

# If parentheses or other characters appear within the data referenced by a marker, that's okay - treat it like normal data, not a marker, and then resume looking for markers after the decompressed section.

# For example:

# ADVENT contains no markers and decompresses to itself with no changes, resulting in a decompressed length of 6.
# A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a decompressed length of 7.
# (3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.
# A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a decompressed length of 11.
# (6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but because it's within a data section of another marker, it is not treated any differently from the A that comes after it. It has a decompressed length of 6.
# X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18), because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped and not processed further.
# What is the decompressed length of the file (your puzzle input)? Don't count whitespace.

# Your puzzle answer was 152851.

import re

with open("9_ExplosivesInCyberspace.txt", 'r') as file:
	data = file.read()

def decompressedLength(line):
	"""Returns decompressed length"""
	itr = re.finditer(r"\((.*?)\)", line)	# iterator of match objects inside brackets
	length = len(line)						# original length of string
	toAdd  = decompress(itr)				# decompress string
	return length + toAdd					# return decompressed length	

def decompress(itr):
	"""Return number of characters to add to original length"""
	currentIndex  = 0
	currentLength = -1
	toAdd = 0	
	for i in itr:									# iterating through match objects
		lngth, rep, x, y = properties(i)
		# print(lngth, rep, x, y, total)
		if not x < (currentIndex + currentLength):	# if not inside previous brackets
			toAdd  += ((rep - 1) * lngth - (y - x))	# num of chars changed
			currentIndex  = y						# current index is close bracket
			currentLength = lngth					# current length updated
	return toAdd
		
def properties(mtch):
	"""Get properties of match object"""
	st = mtch.group()		# matched string
	st = st.split('x')		# splits matched string by 'x'
	lngth = int(st[0][1:])	# length of pattern to decompress
	rep   = int(st[1][:-1])	# number of repeats
	sp = mtch.span()			
	x = sp[0]				# start index of match
	y = sp[1]				# end index of match
	return lngth, rep, x, y
	
# def decompressedLength2(line):
	# """Returns decompressed length"""
	# st = line
	# while re.search(r"\(", st):				# while bracket is found
		# st = replaceBracket(st)				# replace bracket after decompression
		# # print(st)
		# # print(len(st))
	# return len(st)							# return decompressed length
	
# def decompressedLength2B(line):
	# """Returns decompressed length"""
	# itr = re.finditer(r"\((.*?)\)", line)	# iterator of match objects inside brackets
	# length = len(line)						# original length of string
	# toAdd  = decompress2(itr)				# decompress string
	# return length + toAdd					# return decompressed length	

# def decompress2(itr):
	# """Return number of characters to add to original length"""
	# currentIndex  = 0
	# currentLength = -1
	# toAdd = 0
	# active = []
	# for i in itr:									# iterating through match objects
		# lngth, rep, x, y = properties(i)			# matching i-th bracket
		# # print(lngth, rep, x, y, total)
		# for j in active:
			# lngth2, rep2, x2, y2 = properties(j)
			# if not x < y2 + lngth2:					# if not inside previous brackets
			# else:
				# toAdd  += ((rep - 1) * lngth - (y - x))	# num of chars changed
				# currentIndex  = y						# current index is close bracket
				# currentLength = lngth					# current length updated
			# active.append(i)
	# return toAdd
	
# def replaceBracket(line):
	# """Returns next brackets"""
	# next = re.search(r"\((.*?)\)", line)	# next brackets
	# start = next.start()					# starting index
	# end   = next.end()						# end index
	# st    = next.group()					# matched string
	# st    = st.split('x')					# splits matched string by 'x'
	# lngth = int(st[0][1:])					# length of pattern to decompress
	# rep   = int(st[1][:-1])					# number of repeats
	# decompressed = line[end:end+lngth] * (rep-1)
	# newSt = line[:start] + decompressed + line[end:]
	# return newSt							# return decompressed length
	
print(decompressedLength(data))

# --- Part Two ---
# Apparently, the file actually uses version two of the format.

# In version two, the only difference is that markers within decompressed data are decompressed. This, the documentation explains, provides much more substantial compression capabilities, allowing many-gigabyte files to be stored in only a few kilobytes.

# For example:

# (3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no markers.
# X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker is then further decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
# (27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 241920 times.
# (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long.
# Unfortunately, the computer you brought probably doesn't have enough memory to actually decompress the file; you'll have to come up with another way to get its decompressed length.

# What is the decompressed length of the file using this improved format?


# print(decompressedLength2B(data))
	
