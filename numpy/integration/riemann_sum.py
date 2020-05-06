import numpy as np


def main():

	step = 0.1
	step_shrink = 0.001

	for i in range(80):

		# construct 1D numpy array with values in [0, pi/2], step size 0.1
		step = step - step_shrink
		#print("step size: ", step)
		n = int((np.pi/2)/step)
		xi = np.linspace(0, n*step, n+1)
		#print(xi)

		fi = np.sin(xi)
		integral = np.sum( ((fi[1:]+fi[:-1])/2) * step)
		print("Riemann sum: ", integral)

main()
