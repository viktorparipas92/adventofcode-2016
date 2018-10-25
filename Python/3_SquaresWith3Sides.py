# --- Day 3: Squares With Three Sides ---
# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

# Or are they?

# The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

# In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

# In your puzzle input, how many of the listed triangles are possible?

# Your puzzle answer was 862.

class triangle(object):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	def isTriangle(self):
		if (self.a + self.b) > self.c and (self.a + self.c) > self.b and (self.b + self.c) > self.a:
			return True
		else:
			return False
	def __str__(self):
		return "Triangle with sides %s %s and %s"%(self.a, self.b, self.c)
	@classmethod
	def fromString(cls, str):
		sides = cls.parseTriangle(str)
		return cls(*sides)
	@staticmethod
	def parseTriangle(str):
		str   = str.rstrip()
		sides = str.split()
		a = int(sides[0])
		b = int(sides[1])
		c = int(sides[2])
		return (a, b, c)
		

with open("3_SquaresWith3Sides.txt",'r') as file:
	triangles = file.read().splitlines()

numOfTriangles = sum([triangle.fromString(row).isTriangle() for row in triangles])
print(numOfTriangles)

# --- Part Two ---
# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

# Your puzzle answer was 1577.

numOfTriangles = 0
for i in range(len(triangles)):
	if i % 3 == 2:							# after every 3 rows
		twoBefore = triangles[i-2].split()
		oneBefore = triangles[i-1].split()
		current   = triangles[i].split()
		numOfTriangles += triangle(int(twoBefore[0]), int(oneBefore[0]), int(current[0])).isTriangle()
		numOfTriangles += triangle(int(twoBefore[1]), int(oneBefore[1]), int(current[1])).isTriangle()
		numOfTriangles += triangle(int(twoBefore[2]), int(oneBefore[2]), int(current[2])).isTriangle()
print(numOfTriangles)

		


