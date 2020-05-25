from mpi4py import MPI


def main():

	comm = MPI.COMM_WORLD
	size = comm.Get_size()
	rank = comm.Get_rank()

	print("I am rank ", rank, " in a group of ", size, " processes")


main()
