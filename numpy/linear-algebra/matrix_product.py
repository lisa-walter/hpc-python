import numpy as np


def main():

	A = np.array([[1, 2], [3, 4]])
	A_sym = A + A.T
	print("A_sym:\n", A_sym)

	B = np.array([[5, 6], [7, 8]])
	B_sym = B + B.T
	print("B_sym:\n", B_sym)

	C = np.dot(A_sym, B_sym)
	print("matrix product:\n", C)

	values = np.linalg.eigvals(C)
	print("eigenvalues of product matrix:\n", values)

main()
