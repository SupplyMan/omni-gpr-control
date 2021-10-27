class Vec2D():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return str(self.x) + ',' + str(self.y)

	def __hash__(self):
		return hash(str(self))

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __add__(self, other):
		return Vec2D(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vec2D(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		return Vec2D(self.x * other.x, self.y * other.y)

	def get(self):
		return (self.x, self.y)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def isInBounds(self, pmin, pmax):
		if pmin.x > self.x or pmax.x < self.x:
			return False

		if pmin.y > self.y or pmax.y < self.y:
			return False

		return True