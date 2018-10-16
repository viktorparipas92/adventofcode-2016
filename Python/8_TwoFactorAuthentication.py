# --- Day 8: Two-Factor Authentication ---
# You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

# To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

# Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

# The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

# rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
# rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
# rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
# For example, here is a simple sequence on a smaller screen:

# rect 3x2 creates a small rectangle in the top-left corner:

# ###....
# ###....
# .......
# rotate column x=1 by 1 rotates the second column down by one pixel:

# #.#....
# ###....
# .#.....
# rotate row y=0 by 4 rotates the top row right by four pixels:

# ....#.#
# ###....
# .#.....
# rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

# .#..#.#
# #.#....
# .#.....
# As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

# There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

class Pixel(object):
	def __init__(self, coord, On=False):
		self.x = coord[0]
		self.y = coord[1]
		self.on = On
	def turnOn(self):
		self.on = True

class Screen(object):
	def __init__(self, sizeX=50, sizeY=6):
		self.width  = sizeX										
		self.height = sizeY
		self.matrix = self.createMatrix()
	def arrayPrint(self):
		"""Prints screen in a readable way"""
		# mx = [[self.matrix[i][j].on for j in range(self.height)] for i in range(self.width)]
		mx = [["." for i in range(self.width)] for j in range(self.height)]
		for j in range(self.height):
			for i in range(self.width):
				if self.matrix[i][j].on:
					mx[j][i] = "#"
		for j in range(self.height):
			print("".join(mx[j]))
			
	def createMatrix(self):
		"""Creates array of pixels"""
		return [[Pixel((i,j)) for j in range(self.height)] for i in range(self.width)]
	def rectangleOn(self, A, B):
		"""Turns on all pixels in a rectangle"""
		for i in range(A):
			for j in range(B):
				self.matrix[i][j].turnOn()								# updates pixels in rectangle
	def rotateRow(self, A, B):
		"""Rotates row y=A by B"""
		oldList = [self.matrix[i][A].on for i in range(self.width)]		# creates list of booleans for each pixel
		newList = oldList[-B:] + oldList[:-B]							# rotates list of booleans to the right
		for i in range(self.width):										# updates pixels
			self.matrix[i][A].on = newList[i]
	def rotateColumn(self, A, B):
		"""Rotates column x=A by B"""
		oldList = [self.matrix[A][j].on for j in range(self.height)]	# creates list of booleans for each pixel
		newList = oldList[-B:] + oldList[:-B]							# rotates list of booleans down
		for j in range(self.height):									# updates pixels
			self.matrix[A][j].on = newList[j]
	def executeInstruction(self, line):
		"""Parses the instruction contained in line"""
		words = line.split()											# split string into list
		if words[0] == "rect":
			size = [int(i) for i in words[1].split('x')]				# size of rectangle to be lit	
			A = size[0]
			B = size[1]
			self.rectangleOn(A, B)
		else:
			A = int(words[2].split('=')[1])								# index of row/column
			B = int(words[4])											# shift by B
			if words[1] == "row":
				self.rotateRow(A, B)
			else:
				self.rotateColumn(A, B)
	def numberOfPixelsLit(self):
		"""Counts how many pixels are on in the screen"""
		Lit = [[int(self.matrix[i][j].on) for j in range(self.height)] for i in range(self.width)]
		return sum(sum(x) for x in Lit)
				
with open("8_TwoFactorAuthentication.txt",'r') as file:
	data = [row.strip() for row in file.readlines()]	# formatting raw data

screen = Screen()										# creating screen
for row in data:										# going through instructions				
	screen.executeInstruction(row)						# execute each instruction
	
print(screen.numberOfPixelsLit())

# --- Part Two ---
# You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

# After you swipe your card, what code is the screen trying to display?
	
screen.arrayPrint()
