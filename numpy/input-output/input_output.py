import numpy as np


def main():

	coord = np.loadtxt('xy-coordinates.dat')
	print("coordinates:\n", coord)

	coord[:,1] = coord[:,1] + 2.5
	print("new coordinates:\n", coord)

	args = {
		'fmt': '%1.6f'
	}
	np.savetxt('new-xy-coordinated.dat', coord, **args)

main()
