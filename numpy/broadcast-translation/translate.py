import numpy as np


def main():

	data = np.loadtxt('points_circle.dat')
	print("data:\n", data)

	vector = np.array([[2.1, 1.1]])
	print("vector:\n", vector)

	print("shape of data: ", data.shape, "\n", "shape of vector: ", vector.shape)
	data_translated = data + vector
	print("translated data:\n", data_translated)



main()
