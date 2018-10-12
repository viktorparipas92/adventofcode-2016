# --- Part Two ---
# You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    # 1
  # 2 3 4
# 5 6 7 8 9
  # A B C
    # D
# You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

# You start at "5" and don't move at all (up and left are both edges), ending at 5.
# Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
# Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
# Finally, after five more moves, you end at 3.
# So, given the actual keypad layout, the code would be 5DB3.

# Using the same instructions in your puzzle input, what is the correct bathroom code?

class button(object):
	def __init__(self, x=-2, y=0):
		self.X = x
		self.Y = y
	def right(self):
		if (self.X + abs(self.Y)) < 2:
			self.X += 1
	def left(self):
		if (-self.X + abs(self.Y)) < 2:
			self.X -= 1
	def down(self):
		if (self.Y + abs(self.X)) < 2:
			self.Y += 1
	def up(self):
		if (-self.Y + abs(self.X)) < 2:
			self.Y -= 1
	def move(self, instr):
		# switcher = {
		# "R": self.right(),
		# "L": self.left(),
		# "U": self.up(),
		# "D": self.down() }
		# func = switcher.get(instr, lambda: 0)
		if instr == 'R':
			self.right()
		elif instr == 'L':
			self.left()
		elif instr == 'U':
			self.up()
		elif instr == 'D':
			self.down()
	def number(self):
		if abs(self.Y) == 1:
			num = 7 + self.Y * 4 + self.X
		else:
			num = 7 + self.Y * 3 + self.X	
		return str(format(num,'x'))

with open("2_BathroomSecurity.txt",'r') as file:
	instructions = file.readlines()

Button = button()
solution = ""
	
for stage in instructions:
	for instruction in stage:
		Button.move(instruction)
	solution += Button.number()
print(solution)
		


