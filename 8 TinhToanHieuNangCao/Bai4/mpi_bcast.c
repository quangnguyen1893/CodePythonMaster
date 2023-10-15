#include <mpi.h>
#include <stdio.h>
#define NELEMENTS 5
int main(int argc, char ** argv)
{
	int i, rank, size;
	int buf[NELEMENTS];

	MPI_Init(&argc, &argv); // Initialize the MPI execution environment
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	if (rank == 0){ // Process #0 broadcast to all processes with MPI_Send() and MPI_Recv()
		int dest;
		for (i = 0; i < NELEMENTS; i++) buf[i] = 1 + i*i; // Fill buffer
		
		for (dest = 1; dest < size; dest++){
			MPI_Send(buf, NELEMENTS, MPI_INT, dest, 0, MPI_COMM_WORLD);
		}
	}else{ // Receive from rank #0
		MPI_Recv(buf, NELEMENTS, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		printf("Rank: %d - da nhan tu rank 0: \n", rank);
		for(int i=0;i<NELEMENTS;i++) printf("%d ", buf[i]);
		printf("\n");
	}
	

	return MPI_Finalize();

}
