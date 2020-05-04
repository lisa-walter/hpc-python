import numpy as np

def main():

	# create numpy array from list containing int and float
	list = [1, 3.4, 5, 2, 4.5]
	a = np.array(list)
	print(a)
	print(a.size, a.shape)

	# create 1D numpy array with numbers from -2 to 2, step size 0.2
	b = np.arange(-2, 2.01, 0.2)
	print(b)

	# create 1D numpy array with 11 equally spaced values between 0.5 and 1.5
	c = np.linspace(0.5, 1.5, 11)
	print(c)

	# create numpy array of characters from python string
	str = "Hello World"
	d = np.array(str, dtype='c')
	print(d)
	#numpy.fromiter('string', dtype='U1') would also be possible (from comment section)


main()
