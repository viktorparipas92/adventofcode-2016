# --- Day 21: Scrambled Letters and Hash ---
# The computer system you're breaking into uses a weird scrambling function to store its passwords. It shouldn't be much trouble to create your own scrambled password so you can add it to the system; you just have to implement the scrambler.

# The scrambling function is a series of operations (the exact list is provided in your puzzle input). Starting with the password to be scrambled, apply each operation in succession to the string. The individual operations behave as follows:

# swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
# swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
# rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
# rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
# reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
# move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.
# For example, suppose you start with abcde and perform the following operations:

# swap position 4 with position 0 swaps the first and last letters, producing the input for the next step, ebcda.
# swap letter d with letter b swaps the positions of d and b: edcba.
# reverse positions 0 through 4 causes the entire string to be reversed, producing abcde.
# rotate left 1 step shifts all letters left one position, causing the first letter to wrap to the end of the string: bcdea.
# move position 1 to position 4 removes the letter at position 1 (c), then inserts it at position 4 (the end of the string): bdeac.
# move position 3 to position 0 removes the letter at position 3 (a), then inserts it at position 0 (the front of the string): abdec.
# rotate based on position of letter b finds the index of letter b (1), then rotates the string right once plus a number of times equal to that index (2): ecabd.
# rotate based on position of letter d finds the index of letter d (4), then rotates the string right once, plus a number of times equal to that index, plus an additional time because the index was at least 4, for a total of 6 right rotations: decab.
# After these steps, the resulting scrambled password is decab.

# Now, you just need to generate a new scrambled password and you can access the system. Given the list of scrambling operations in your puzzle input, what is the result of scrambling abcdefgh?

class Scramble(object):
	def __init__(self, input):
		self.strng = list(input)
	def __str__(self):
		return "".join(self.strng)
	def parseAndArbitrate(self, line):
		"""Parses line"""
		lst = line.split()
		if lst[0] == "swap":
			X = lst[2]
			Y = lst[5]
			self.swap(X, Y)
		elif lst[0] == "reverse":
			X = int(lst[2])
			Y = int(lst[4])
			self.reverse(X, Y)
		elif lst[0] == "move":
			X = int(lst[2])
			Y = int(lst[5])
			self.move(X, Y)
		elif lst[0] == "rotate":
			drctn = lst[1]
			if lst[1] != "based":					# rotate given num. of times
				X = int(lst[2]) % len(self.strng)
			else:									# rotate based on position
				A = lst[6]
				X = self.strng.index(A)
				if X >= 4:
					X = X + 2
				else:
					X = X + 1
			self.rotate(drctn, X)
	def unscramble(self, line):
		"""Parses line"""
		lst = line.split()
		if lst[0] == "swap":						# easily reversible
			X = lst[2]
			Y = lst[5]
			self.swap(X, Y)
		elif lst[0] == "reverse":					# easily reversible
			X = int(lst[2])
			Y = int(lst[4])
			self.reverse(X, Y)
		elif lst[0] == "move":						# easily reversible
			X = int(lst[2])
			Y = int(lst[5])
			self.move(Y, X)							# swap indices
		elif lst[0] == "rotate":
			drctn = lst[1]
			if lst[1] != "based":					# rotate given num. of times
				X = int(lst[2]) % len(self.strng)
			else:									# rotate based on position
				A = lst[6]
				X = self.strng.index(A)
				if X >= 4:
					X = X + 2
				else:
					X = X + 1
			self.unRotate(drctn, X)
	def swap(self, X, Y):
		"""Swaps letters X and Y | letters at position X and Y"""
		if not X.isalpha():	# swap position
			X, Y = int(X), int(Y)
			self.strng[X], self.strng[Y] = self.strng[Y], self.strng[X]
		else:				# swap letters
			a = self.strng.index(X)
			b = self.strng.index(Y)
			self.strng[a], self.strng[b] = Y, X
	def reverse(self, X, Y):
		"""Reverse string from indexes X to Y inclusive"""
		self.strng[X:Y+1] = reversed(self.strng[X:Y+1])
	def move(self, X, Y):
		"""Moves letter at position X to position Y"""
		self.strng.insert(Y, self.strng.pop(X))
	def rotate(self, drctn, X):
		"""Rotates string left or right by X"""
		if drctn == "left":
			self.strng = self.strng[X:] + self.strng[:X]
		else:
			Y = len(self.strng) - X							# "right" or "based"
			self.strng = self.strng[Y:] + self.strng[:Y]
	def unRotate(self, drctn, X):
		if drctn == "right":
			self.strng = self.strng[X:] + self.strng[:X]
		else:
			Y = len(self.strng) - X							# "left" or "based"
			self.strng = self.strng[Y:] + self.strng[:Y]

start = "abcdefgh"
filename = "21_ScrambledLettersHash.txt"
with open(filename, 'r') as file:
	data = [line.strip() for line in file.readlines()]

scrmble = Scramble(start)

for i in data:
	scrmble.parseAndArbitrate(i)
print(scrmble)

# --- Part Two ---
# You scrambled the password correctly, but you discover that you can't actually modify the password file on the system. You'll need to un-scramble one of the existing passwords by reversing the scrambling process.

# What is the un-scrambled version of the scrambled password fbgdceah?