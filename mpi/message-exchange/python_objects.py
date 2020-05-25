from mpi4py import MPI


def main():

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	dict = {'rank': rank}

	if (rank == 0):

		comm.send(dict, dest=1)
		dict_received = comm.recv(source=1)

	elif (rank == 1):

		comm.send(dict, dest=0)
		dict_received = comm.recv(source=0)

	print("My rank is ", rank, "and I received: ", dict_received['rank'])



main()
