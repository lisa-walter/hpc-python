import numpy as np

def main():

	# create an 8x8 array with alternating 1/0 pattern, upper left: 1
	a = np.zeros((8,8))
	a[::2, ::2] = 1
	a[1::2, 1::2] = 1
	print("8x8 array:\n", a)

	# split array into two 4x8 arrays
	s = np.split(a, 2, axis = 0)
	s1 = s[0]
	s2 = s[1]
	print("split into two 4x8 arrays:\n", s1, "\n\n", s2)

	# recombine them to reconstruct old array
	old = np.concatenate((s1, s2), axis = 0)
	print("reconstruct old array:\n", old)

	# split a into two 8x4 subarrays:
	s = np.split(a, 2, axis = 1)
	s1 = s[0]
	s2 = s[1]
	print("split into two 8x4 arrays:\n", s1, "\n\n", s2)

	# recombine them to reconstruct old array
	old = np.concatenate((s1, s2), axis = 1)
	print("reconstruct old array:\n", old)


main()
