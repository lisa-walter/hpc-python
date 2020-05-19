from cyt_module import subtract
import numpy as np


def main():

	print(subtract(4.5, 2))
	x = np.array((1,2,3,4,5,6,7,8,9,10))
	y = np.array((4.2, 5.2, 5.7, 4, 5.3, 5, 6.32, 5, 6.6, 10))
	print(subtract(x, y))


main()
