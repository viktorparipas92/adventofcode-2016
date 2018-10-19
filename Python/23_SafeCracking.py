# --- Day 23: Safe Cracking ---
# This is one of the top floors of the nicest tower in EBHQ. The Easter Bunny's private office is here, complete with a safe hidden behind a painting, and who wouldn't hide a star in a safe behind a painting?

# The safe has a digital screen and keypad for code entry. A sticky note attached to the safe has a password hint on it: "eggs". The painting is of a large rabbit coloring some eggs. You see 7.

# When you go to type the code, though, nothing appears on the display; instead, the keypad comes apart in your hands, apparently having been smashed. Behind it is some kind of socket - one that matches a connector in your prototype computer! You pull apart the smashed keypad and extract the logic circuit, plug it into your computer, and plug your computer into the safe.

# Now, you just need to figure out what output the keypad would have sent to the safe. You extract the assembunny code from the logic chip (your puzzle input).
# The code looks like it uses almost the same architecture and instruction set that the monorail computer used! You should be able to use the same assembunny interpreter for this as you did there, but with one new instruction:

# tgl x toggles the instruction x away (pointing at instructions like jnz does: positive means forward; negative means backward):

# For one-argument instructions, inc becomes dec, and all other one-argument instructions become inc.
# For two-argument instructions, jnz becomes cpy, and all other two-instructions become jnz.
# The arguments of a toggled instruction are not affected.
# If an attempt is made to toggle an instruction outside the program, nothing happens.
# If toggling produces an invalid instruction (like cpy 1 2) and an attempt is later made to execute that instruction, skip it instead.
# If tgl toggles itself (for example, if a is 0, tgl a would target itself and become inc a), the resulting instruction is not executed until the next time it is reached.
# For example, given this program:

# cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a
# cpy 2 a initializes register a to 2.
# The first tgl a toggles an instruction a (2) away from it, which changes the third tgl a into inc a.
# The second tgl a also modifies an instruction 2 away from it, which changes the cpy 1 a into jnz 1 a.
# The fourth line, which is now inc a, increments a to 3.
# Finally, the fifth line, which is now jnz 1 a, jumps a (3) instructions ahead, skipping the dec a instructions.
# In this example, the final value in register a is 3.

# The rest of the electronics seem to place the keypad entry (the number of eggs, 7) in register a, run the code, and then send the value left in register a to the safe.

# What value should be sent to the safe?

class Monorail(object):
	def __init__(self, idx=0, tgl=-1):
		self.idx = idx
		self.tglbuf = []
		self.registers = {}
	def copy(self, x, y):
		self.registers[y] = self.val(x)
		self.idx += 1
	def inc(self, x):
		self.registers[x] = self.val(x) + 1
		self.idx += 1
	def dec(self, x):
		self.registers[x] = self.val(x) - 1
		self.idx += 1
	def tgl(self, x):								# TOGGLE
		self.tglbuf.append(self.idx + self.val(x))	# Add given index to buffer
		self.idx += 1								# Increment current index
		# print(self.tglbuf)
	def jnz(self, x, y):
		if self.val(x) != 0:
			self.idx += self.val(y)
		else:
			self.idx += 1
	def val(self, x):
		if x.isalpha():
			return self.registers.get(x, 0)	
		else:
			return int(x)
	def parse(self, line):
		"""Parses line of instruction"""
		lst   = line.split()				# line is split into list
		cmd   = lst[0]
		if self.idx in set(self.tglbuf):	# If command is toggled
			cmd = self.toggle(cmd)			# toggle command
		param = lst[1:]
		if cmd == "cpy":
			self.copy(*param)
		elif cmd == "inc":
			self.inc(*param)
		elif cmd == "dec":
			self.dec(*param)
		elif cmd == "jnz":
			self.jnz(*param)
		elif cmd == "tgl":
			self.tgl(*param)
		# print(self.idx, cmd, self.tglbuf, self.registers)
	def executeData(self, data):
		"""Executes all instructions"""
		while self.idx < len(data):	
			line = data[self.idx]
			self.parse(line)
	def toggle(self, cmd):
		"""Toggle commands"""
		if cmd == "inc":
			return "dec"
		elif cmd == "tgl" or cmd == "dec":
			return "inc"
		elif cmd == "jnz":
			return "cpy"
		elif cmd == "cpy":
			return "jnz"
			
with open("23_SafeCracking.txt", 'r') as file:
	data = [row.strip() for row in file.readlines()]
	
safe = Monorail()
safe.registers["a"] = 7
safe.executeData(data)
print(safe.registers["a"])

safe2 = Monorail()
safe2.registers["a"] = 12
safe2.executeData(data)
print(safe2.registers["a"])