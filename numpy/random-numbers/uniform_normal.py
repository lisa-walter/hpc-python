import numpy as np


def main():

	uniform_rands = np.random.random(size=1000)

	me = np.mean(uniform_rands)
	deviation = np.std(uniform_rands)
	print("uniform distribution\nmean: ", me, "standard deviation: ", deviation)

	normal_rands = np.random.normal(size = 1000)
	me = np.mean(normal_rands)
	deviation = np.std(normal_rands)
	print("normal distribution\nmean: ", me, "standard deviation: ", deviation)

main()
