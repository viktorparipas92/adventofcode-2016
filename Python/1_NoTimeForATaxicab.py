# --- Day 1: No Time for a Taxicab ---
# Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

# The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

# For example:

# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# How many blocks away is Easter Bunny HQ?

# Your puzzle answer was 353.

class bunny(object):
	def __init__(self, direction, x=0, y=0):
		self.direction = direction
		self.X = x
		self.Y = y
		self.visited = set([(self.X, self.Y)])
	def turnRight(self):
		self.direction += 1
		self.direction %= 4
	def turnLeft(self):
		self.direction -= 1
		self.direction %= 4
	def turn(self, drctn):
		if drctn == 'R':
			self.turnRight()
		elif drctn == 'L':
			self.turnLeft()
	def walk(self, steps):
		if self.direction == 0:
			self.Y += steps
		elif self.direction == 1:
			self.X += steps
		elif self.direction == 2:
			self.Y -= steps
		elif self.direction == 3:
			self.X -= steps
	def distance(self):
		return abs(self.X) + abs(self.Y)
	def coordinates(self):
		return (self.X, self.Y)
	def storePosition(self):
		self.visited.add((self.X, self.Y))
		
Bunny = bunny(0)

with open("1_NoTimeForATaxicab.txt",'r') as file:
	data = file.read()
	instructions = data.split(', ')

foundHQ = False

for instr in instructions:
	drctn = instr[0]		# direction to turn
	steps = int(instr[1:])	# number of steps to walk
	Bunny.turn(drctn)
	Bunny.walk(steps)
	if not foundHQ:
		if Bunny.coordinates() not in Bunny.visited:
			Bunny.storePosition()
		else:
			print(Bunny.distance())
			foundHQ = True
	Bunny.storePosition()
	
print(Bunny.distance())

# --- Part Two ---
# Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

# For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

# How many blocks away is the first location you visit twice?