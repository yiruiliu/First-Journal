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

    