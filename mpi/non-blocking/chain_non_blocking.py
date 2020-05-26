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

	req = []
	req.append(comm.Isend(send_arr, dest=tgt))
	req.append(comm.Irecv(recv_arr, source=src))

	MPI.Request.waitall(req)

	# print not true for cases 0 and ntasks-1
	print("My ID is ", myid, " I sent ", send_arr[0], "s, I received ", recv_arr[0], "s")

main()
