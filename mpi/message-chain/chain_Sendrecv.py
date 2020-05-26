import numpy as np
from mpi4py import MPI


def main():

	comm = MPI.COMM_WORLD
	myid = comm.Get_rank()
	ntasks = comm.Get_size()

	send_arr = np.full(100000, myid, dtype=int)
	recv_arr = np.empty_like(send_arr)

	tgt = myid + 1
	src = myid - 1

	if (myid == 0):
		src = MPI.PROC_NULL

	elif (myid == ntasks-1):
		tgt = MPI.PROC_NULL

	comm.Sendrecv(send_arr, dest=tgt, recvbuf=recv_arr, source=src)
	print("My ID is ", myid)
	if (myid != ntasks-1):
		print("I sent ", send_arr.size, " elements")
	if (myid != 0):
		print("I received ", recv_arr[0], "s")

main()
