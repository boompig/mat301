def gen (generator, modulus, G=None, a=None):
	G = set([])
	a = generator

	while a not in G:
		G.add (a)
		a = (a * generator) % modulus

	return G

def mod_group_op (a, b, modulus):
	return (a * b) % modulus

def find_order (a, group_op, identity):
	order = 1
	b = a
	while b != identity:
		order += 1
		b = group_op (a, b)
	return order

def do_stuff ():
	orders = {}
	for item in G:
		n = find_order (item, mod_16, 1)
		orders [item] = n
		#print "%d has order %d" % (item, n)
		if n == 4:
			Gn = gen (item, 16)
			if item in [5, 13]:
				print item
				print Gn
			#print Gn.intersection(G3)
	print orders

if __name__ == "__main__":
	G3 = gen (3, 16)
	#print G
	mod_16 = lambda a, b: mod_group_op (a, b, 16)

	G = [1, 3, 5, 7, 9, 11, 13, 15]
	flag = False

	for item in G:
		Gn = gen(item, 16)
		if len(Gn) == G:
			print "yay"
			print item
			flag = True

	if flag == False:
		print "aww :("
