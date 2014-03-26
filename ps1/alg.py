class Formula(object):
	def __init__ (self, s):

		self.tokens = self.tokenize (s)
		if len (self.tokens) > 0 and self.tokens[0] != "(":
			self.tokens.insert(0, "(")
			self.tokens.append (")")

		i = 0

		# add extra tokens when needed
		# simplify when needed
		while i < len(self.tokens) - 1:
			t = self.tokens[i]
			t2 = self.tokens[i + 1]
			if not self.is_operator(t) and not self.is_operator(self.tokens[i + 1]):
				self.tokens.insert(i + 1, "*")

			i += 1

	def is_operator (self, s):
		return s in ["*", "+", "-", "/", ")", "("]

	def tokenize (self, s):
		# all the tokens in a formula
		return filter(lambda k: k != " ", list(s))

	def __str__ (self):
		return " ".join(self.tokens)

	def __neg__ (self):
		return Formula ("-" + str(self))

	def _op (self, other, op):

		t1 = str(self)
		t2 = str(other)
		return Formula (t1 + op + t2)

	def __mul__ (self, other):
		"""Multiply this by another formula."""

		return self._op(other, "*")

	def __add__ (self, other):
		"""Multiply this by another formula."""

		return self._op(other, "+")

class Matrix (object):
	"""2x2 matrix"""

	def __init__ (self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def inverse (self):
		return Matrix (self.d, -self.b, -self.c, self.a)

	def __str__(self):
		s = "|\t%s\t%s\t|\n" % (self.a, self.b)
		s += "|\t%s\t%s\t|" % (self.c, self.d)
		return s

def load_values():
	# values for A:
	d = {
		"a": "a + b",
		"b": "-2b",
		"c": "b",
		"d": "a - b"
	}

	A = Matrix (Formula(d["a"]), Formula(d["b"]), Formula(d["c"]), Formula(d["d"]))
	#print str(A)
	print str(A.inverse())

def get_matrix(name):
    print "Define a matrix %s" % name
    a = raw_input("a ")
    b = raw_input("b ")
    c = raw_input("c ")
    d = raw_input("d ")
    print "%s:" % name
    print "|\t%s\t%s\t|" % (a, b)
    print "|\t%s\t%s\t|" % (c, d)
    return { "a" : a, "b" : b, "c" : c, "d" : d}

def matrix_2_by_2_inverse (matrix):
    print "Front factor: (%s) * (%s) - (%s) * (%s)"

def mul():
	f1 = Formula("ab")
	f2 = Formula("bc")
	print f1
	print f2
	print f1 * f2
	print f1 + f2 
	print -f1

if __name__ == "__main__":
	#A = get_matrix("A")
	#B = get_matrix("B")
	#B_inverse = matrix_2_by_2_inverse (B)
	mul()
