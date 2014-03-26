def genH ():
	elem = 0
	H = set([])
	while elem not in H:
		H.add(elem)
		elem = (elem + 69) % 84

	return H

print sorted(genH())

