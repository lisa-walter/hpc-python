import numpy as np

def main():

	a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], dtype=float)
	print(a)

	# extract every element from the 2nd row
	b = a[:,1]
	print(b)

	# extract every element from the 3rd column
	c = a[2,:]
	print(c)

	# assign a value of 0.21 to the upper left 2x2 sub-array
	a[:2,:2] = 0.21
	print(a)

	# create an 8x8 array with alternating 1/0 pattern, upper left: 1
	d = np.zeros((8,8))
	d[::2, ::2] = 1
	d[1::2, 1::2] = 1
	print(d)

main()
