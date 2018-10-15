# --- Day 4: Security Through Obscurity ---
# Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

# Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

# A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

# aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
# a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
# not-a-real-room-404[oarel] is a real room.
# totally-real-room-200[decoy] is not.
# Of the real rooms from the list above, the sum of their sector IDs is 1514.

# What is the sum of the sector IDs of the real rooms?

# Your puzzle answer was 185371.

import re
from collections import Counter

with open("4_SecurityThroughObscurity.txt",'r') as file:
	rooms = [room.rstrip() for room in file.readlines()]

def transform(ch, num):
	x = ord(ch)
	y = (((x+num) - 97) % 26) + 97
	if x == 45:
		char = " "
	else:
		char = chr(y)
	return char
	
class Room(object):
	def __init__(self, str):
		self.startIndex = re.search("\d", str).start()
		self.endIndex   = re.search("\[", str).start()
		self.name = self.findName(str)
		self.nameDashes = self.findNameDashes(str)
		self.sectorID = self.findID(str)
		self.checksum = self.findChecksum(str)
	def __str__(self):
		return "Name %s ID %d checksum %s mostCommon %s real %r" % (self.name, self.sectorID, self.checksum, self.mostCommonLetters(), self.isReal())		
	def findName(self, str):
		return str[:self.startIndex].replace('-','')
	def findNameDashes(self, str):
		return str[:self.startIndex]
	def findChecksum(self, str):
		return str[self.endIndex+1:-1]
	def findID(self, str):
		return int(str[self.startIndex:self.endIndex])
	def mostCommonLetters(self):
		tuples = Counter(self.name).most_common(5)
		mostCommon = [t[0] for t in tuples]
		return "".join(mostCommon)
	def isReal(self):
		return self.mostCommonLetters() == self.checksum
	def decryptName(self):
		newName = ""
		for ch in self.nameDashes:
			char = transform(ch, self.sectorID)
			newName += char
		return newName

def decryptName(name):
	newName = ""
	for ch in name:
		char = transform(ch, 1)
		newName += char	
	return newName
		
realNames = 0		
for i in rooms:
	room = Room(i)
	if room.isReal():
		realNames += room.sectorID
	newName = room.decryptName()
	if newName == "northpole object storage ":
		print(room.sectorID, newName)
print(realNames)


# --- Part Two ---
# With all the decoy data out of the way, it's time to decrypt this list and get moving.

# The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

# To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

# What is the sector ID of the room where North Pole objects are stored?

# Your puzzle answer was 984.
