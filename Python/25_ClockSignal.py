# --- Day 25: Clock Signal ---
# You open the door and find yourself on the roof. The city sprawls away from you for miles and miles.

# There's not much time now - it's already Christmas, but you're nowhere near the North Pole, much too far to deliver these stars to the sleigh in time.

# However, maybe the huge antenna up here can offer a solution. After all, the sleigh doesn't need the stars, exactly; it needs the timing data they provide, and you happen to have a massive signal generator right here.

# You connect the stars you have to your prototype computer, connect that to the antenna, and begin the transmission.

# Nothing happens.

# You call the service number printed on the side of the antenna and quickly explain the situation. "I'm not sure what kind of equipment you have connected over there," he says, "but you need a clock signal." You try to explain that this is a signal for a clock.

# "No, no, a clock signal - timing information so the antenna computer knows how to read the data you're sending it. An endless, alternating pattern of 0, 1, 0, 1, 0, 1, 0, 1, 0, 1...." He trails off.

# You ask if the antenna can handle a clock signal at the frequency you would need to use for the data from the stars. "There's no way it can! The only antenna we've installed capable of that is on top of a top-secret Easter Bunny installation, and you're definitely not-" You hang up the phone.

# You've extracted the antenna's clock signal generation assembunny code (your puzzle input); it looks mostly compatible with code you worked on just recently.

# This antenna code, being a signal generator, uses one extra instruction:

# out x transmits x (either an integer or the value of a register) as the next value for the clock signal.
# The code takes a value (via register a) that describes the signal to generate, but you're not sure how it's used. You'll have to find the input to produce the right signal through experimentation.

# What is the lowest positive integer that can be used to initialize register a and cause the code to output a clock signal of 0, 1, 0, 1... repeating forever?

class Clock(object):
	def __init__(self, idx=0, tgl=-1):
		self.idx = idx
		self.registers = {}
		self.output = []
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
	def out(self, x):
		"""Outputs value x"""
		"""Returns True if not a clock signal"""
		self.output.append(self.val(x))
		# print(self.idx, self.output[-1])
		self.idx += 1
		if len(self.output) == 1 and self.output[-1] == 0:
			pass
		elif len(self.output) == 1:
			return True
		elif self.output[-1] != self.output[-2]:
			pass
		else:
			return True
		l = len(self.output)
		if l > 100:
			return False
	def parse(self, line):
		"""Parses line of instruction"""
		"""Returns true if clock signal violated"""
		lst   = line.split()				# line is split into list
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
		elif cmd == "out":
			s = self.out(*param)
			# print(self.idx, cmd, self.output)
			return s
	def executeData(self, data):
		"""Executes all instructions"""
		while self.idx < len(data):	
			line = data[self.idx]
			p = self.parse(line)	
			if p:	# clock signal violated
				# print(self.output)
				self.reset()
				return True
			if p == False:
				return False
		return False
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
	def findSolution(self):
		"""Finds lowest number to generate clock signal"""
		i = 0
		b = True
		while b == True:
			self.registers["a"] = i
			b = self.executeData(data)
			print(i, b)
			i += 1
	def reset(self):
		self.idx = 0
		self.registers = {}
		self.output = []
			
			
with open("25_ClockSignal.txt", 'r') as file:
	data = [row.strip() for row in file.readlines()]
	
clock = Clock()
clock.findSolution()
