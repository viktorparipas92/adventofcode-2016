# --- Day 10: Balance Bots ---
# You come upon a factory in which many robots are zooming around handing small microchips to each other.

# Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

# Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

# Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

# For example, consider the following instructions:

# value 5 goes to bot 2
# bot 2 gives low to bot 1 and high to bot 0
# value 3 goes to bot 1
# bot 1 gives low to output 1 and high to bot 0
# bot 0 gives low to output 2 and high to output 0
# value 2 goes to bot 2
# Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
# Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
# Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
# Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.
# In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

# Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?

class BalanceBots(object):
	def __init__(self):
		self.dict = {}
	def valueFromInput(self, ID, value):
		"""Updates value of bot with given ID"""
		try:							# if bot already exists, just update it
			self.dict[ID]
			self.dict[ID].receiveValue(value)
		except:							# if bot does not exist, create it
			self.createBot(ID, value)
	def fullTransfer(self, ID1, type2, which2, ID2, type3, which3, ID3):
		"""Bot ID1 transfers both values"""
		try:
			if self.dict[ID1].count() == 2:
				if type2   == "bot":
					self.transferBetweenBots(ID1, which2, ID2)
				elif type2 == "output":
					self.transferToOutput(ID1, which2, ID2)
				
				if type3   == "bot":
					self.transferBetweenBots(ID1, which3, ID3)
				elif type3 == "output":
					self.transferToOutput(ID1, which3, ID3)
				return True
			else:
				return False
				
		except:
			return False
			
	def transferBetweenBots(self, ID1, which, ID2):
		"""Bot ID1 gives which value, bot ID2 receives it"""
		try:														
			self.dict[ID2]
			if which   == "high":
				self.dict[ID2].receiveValue(self.dict[ID1].high)
			elif which == "low":
				self.dict[ID2].receiveValue(self.dict[ID1].low)
		except:
			if which   == "high":
				self.createBot(ID2, self.dict[ID1].high)
			elif which == "low":
				self.createBot(ID2, self.dict[ID1].low)			
	def transferToOutput(self, ID1, which, ID2):
		"""Bot ID1 gives which value to output ID2"""
		if which   == "high":
			self.dict[ID2].receiveValueAsOutput(self.dict[ID1].high)
		elif which == "low":
			self.dict[ID2].receiveValueAsOutput(self.dict[ID1].low)
	def createBot(self, ID, value):
		"""Creates new bot with ID and value"""
		self.dict[ID] = Bot(ID, value)
	
	def executeInstructionList(self, data):
		"""Parses and executes list of instructions"""
		i = 0
		while len(data) > 0:					# run until all instructions are executed
			line = data[i]
			instr = self.parseInstruction(line)	# parse and execute instruction
			if instr:							# if instruction executed,
				data.remove(line)				# remove line, do not increment index
			else:
				i += 1							# if instrucion not executed, keep line, increment index
			if i > len(data)-1:
				i = 0							# if instuctions are left, start over
	def parseInstruction(self, line):
		"""Parses and executes instruction"""
		if line[0] == "v":						# value
			inp = self.parseValue(line)			# parse
			self.valueFromInput(*inp)			# execute
			return True
		else:									# transfer
			inp = self.parseTransfer(line)		# parse
			trn = self.fullTransfer(*inp)		# execute; 1 if command was executed, 0 else
			return trn
	def parseTransfer(self, line):
		"""Parsing transfer instruction"""
		lst    = line.split()
		ID1    = lst[1]
		which2 = lst[3]
		type2  = lst[5]
		ID2    = lst[6]
		which3 = lst[8]
		type3  = lst[10]
		ID3    = lst[11]
		return (ID1, type2, which2, ID2, type3, which3, ID3)
	def parseValue(self, line):
		"""Parsing value instruction"""
		lst   = line.split()
		ID    = lst[5]
		value = int(lst[1]) 
		return (ID, value)
		
	def findValuePair(self, A, B):
		"""Gives solution to Part 1"""
		for k in self.dict.keys():
			if self.dict[k].high == A and self.dict[k].low == B:
				return k
				break
		return None
		
	def multiplyThreeOutputs(self, A, B, C):
		"""Gives solution to Part 2"""
		a = self.dict[A].output
		b = self.dict[B].output
		c = self.dict[C].output
		return a*b*c
		
class Bot(object):
	def __init__(self, ID, high=None, low=None, output=None):
		self.ID     = ID
		self.high   = high
		self.low    = low
		self.output = output
	def count(self):
		"""Returns how many values the bot has"""
		count  = isinstance(self.high, int) + isinstance(self.low, int)
		return count
	def receiveValueAsOutput(self, value):
		"""Bot receives value to its output"""
		self.output = value
	def receiveValue(self, value):
		"""Bot receives given value"""
		if self.count() == 0:			# first value
			self.high = value		# high by default
		else:						# second value
			self.secondValue(value)
	def secondValue(self, value):
		"""Bot receives given value as second value"""
		if value > self.high:		# higher than high
			self.low  = self.high
			self.high = value		# new high
		else:
			self.low  = value		# else new low
	
with open("10_BalanceBots.txt",'r') as file:
	data = [row.strip() for row in file.readlines()]

bots = BalanceBots()	
bots.executeInstructionList(data)
print(bots.findValuePair(61, 17))

# --- Part Two ---
# What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?

print(bots.multiplyThreeOutputs("0", "1", "2"))
	
