# --- Day 12: Leonardo's Monorail ---
# You finally reach the top floor of this building: a garden with a slanted glass ceiling. Looks like there are no more stars to be had.

# While sitting on a nearby bench amidst some tiger lilies, you manage to decrypt some of the files you extracted from the servers downstairs.

# According to these documents, Easter Bunny HQ isn't just this building - it's a collection of buildings in the nearby area. They're all connected by a local monorail, and there's another building not far from here! Unfortunately, being night, the monorail is currently not operating.

# You remotely connect to the monorail control systems and discover that the boot sequence expects a password. The password-checking logic (your puzzle input) is easy to extract, but the code it uses is strange: it's assembunny code designed for the new computer you just assembled. You'll have to execute the code and get the password.

# The assembunny code you've extracted operates on four registers (a, b, c, and d) that start at 0 and can hold any integer. However, it seems to make use of only a few instructions:

# cpy x y copies x (either an integer or the value of a register) into register y.
# inc x increases the value of register x by one.
# dec x decreases the value of register x by one.
# jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
# The jnz instruction moves relative to itself: an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

# For example:

# cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a
# The above code would set register a to 41, increase its value by 2, decrease its value by 1, and then skip the last dec a (because a is not zero, so the jnz a 2 skips it), leaving register a at 42. When you move past the last instruction, the program halts.

# After executing the assembunny code in your puzzle input, what value is left in register a?

class Monorail(object):
	def __init__(self, idx=0):
		self.idx = idx
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
		lst   = line.split()
		cmd   = lst[0]
		param = lst[1:]
		if cmd == "cpy":
			self.copy(*param)
		elif cmd == "inc":
			self.inc(*param)
		elif cmd == "dec":
			self.dec(*param)
		elif cmd == "jnz":
			self.jnz(*param)
	def executeData(self, data):
		while self.idx < len(data):	
			line = data[self.idx]
			self.parse(line)
			
with open("12_LeonardosMonorail.txt", 'r') as file:
	data = [row.strip() for row in file.readlines()]
	
monorail = Monorail()
monorail.executeData(data)
print(monorail.registers["a"])

# --- Part Two ---
# As you head down the fire escape to the monorail, you notice it didn't start; register c needs to be initialized to the position of the ignition key.

# If you instead initialize register c to be 1, what value is now left in register a?

# Your puzzle answer was 9227737.

monorail2 = Monorail()
monorail2.registers["c"] = 1
monorail2.executeData(data)
print(monorail2.registers["a"])

	