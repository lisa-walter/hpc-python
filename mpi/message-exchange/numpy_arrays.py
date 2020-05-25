from mpi4py import MPI
import numpy as np


def main():

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()

	rank_arr = np.full(100000, rank, dtype=float)
	receive_arr = np.empty_like(rank_arr, dtype=float)

	if (rank == 0):

		comm.Recv(receive_arr, source=1)
		comm.Send(rank_arr, dest=1)

	elif (rank == 1):

		comm.Send(rank_arr, dest=0)
		comm.Recv(receive_arr, source=0)

	print("My rank: ", rank)
	print("First value in received array: ", receive_arr[0])

main()
