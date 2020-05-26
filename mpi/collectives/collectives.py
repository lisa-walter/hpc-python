import numpy as np
from mpi4py import MPI


def main():


	# simple broadcast ----------------------------------------------

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

#	if (rank == 0):
#		data = np.arange(8)
#	else:
#		data = np.zeros(8, dtype=int)

#	comm.Bcast(data, root=0)

#	print("My rank is ", rank, " and 'data' contains: ", data)


	# initial data vectors ------------------------------------------

	data = np.arange(8) + 8*rank
#	print("My rank is ", rank, " and 'data' contains: ", data)

	# receive buffer
	buffer = np.ones(8, int) * -1


	# case 1 --------------------------------------------------------

	# idea: one to many, scatter

#	comm.Scatter(data, buffer, root=0)


	# case 2 --------------------------------------------------------

	# idea: many to one, gather

#	comm.Gather(data[:2], buffer, root=1)


	# case 3 --------------------------------------------------------

	# idea: buffer0 = data0 + data1, buffer2 = data2 + data3
	# many to one, reduce

	# create 2 communicators

	if (rank < 2):
		color = 0
	else:
		color = 1

	comm_local = comm.Split(color)
	rank_local = comm_local.Get_rank()

	# found out: global ranks 0 1 2 3 correspond to local ranks 0 1 0 1

	comm_local.Reduce(data, buffer, op=MPI.SUM, root=0)

	# print resulting vectors

	print("My rank is ", rank, " and 'buffer' contains: ", buffer)



main()
