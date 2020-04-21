def subfunc1(Mat,P1,P2,P12,l1,l2):
	for s in P12:
		for i in range(0, l1):
			if s.issubset(P1[i]):
				break
		for j in range(0, l2):
			if s.issubset(P2[j]):
				break
		Mat=Matrix(Mat)
		Mat[i,j] = 1
	return Mat

def FromSetPartitions2Matrix(P1,P2):
    P12 = P1 * P2
    l1 = len(P1)
    l2 = len(P2)
    row = [0] * l1
    Mat = [row] * l2
    Mat = subfunc1(Mat, P1, P2, P12, l1, l2)
    return Mat

def FromSetPartitons2BipartiteGraph(P1,P2,baseCar,CarOfP12):
	P12 = P1 * P2
	if P12.max_block_size() == baseCar/CarOfP12 and len(P12) == CarOfP12:
		Mat = FromSetPartitions2Matrix(P1,P2)
		G = BipartiteGraph(Mat.T)
		return G
	return []

def CanonicalGraphList(P1,Partitions,CarofP12):
	baseCar = P1.base_set_cardinality()
	CanonicalGlist = []
	for P2 in Partitions:
		G = FromSetPartitons2BipartiteGraph(P1,P2,baseCar,CarOfP12)
		if G:
			if not CanonicalGlist:
				CanonicalGlist.append(G)
			else:
				verify = 0
				for CanonicalG in CanonicalGlist:
					if CanonicalG.is_isomorphic(G):
						verify = 1
						break
				if verify == 0:
					CanonicalGlist.append(G)
	return CanonicalGlist


