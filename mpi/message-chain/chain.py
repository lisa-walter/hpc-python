import numpy as np
from mpi4py import MPI


def main():

	comm = MPI.COMM_WORLD
	myid = comm.Get_rank()
	ntasks = comm.Get_size()

	send_arr = np.full(100000, myid, dtype=int)
	recv_arr = np.empty_like(send_arr)

	if (myid < ntasks-1):

		comm.Send(send_arr, dest=myid+1)
		print("I sent ", send_arr.size, " elements")

	if (myid > 0):

		comm.Recv(recv_arr, source=myid-1)
		print("My ID is ", myid, " and I received ", recv_arr[0], "s")

main()
