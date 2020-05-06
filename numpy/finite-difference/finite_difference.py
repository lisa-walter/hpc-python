import numpy as np


def main():

	# construct 1D numpy array with values in [0, pi/2], step size 0.1
	n = int((np.pi/2)/0.1)
	step = 0.1
	xi_s = np.linspace(0, n*step, n+1)
	#print(xi_s)

	# derivative of sin() on interval [0, pi/2] (excluding end points)
	sin_arr = np.sin(xi_s) # calculate that before deriv_sin, otherwise have to do it twice
	deriv_sin = (sin_arr[2:] - sin_arr[:-2]) / (2*step)
	print(deriv_sin)

	cos_arr = np.cos(xi_s)
	deriv_cos = (cos_arr[2:] - cos_arr[:-2]) / (2*step)
	print(deriv_cos)


main()
