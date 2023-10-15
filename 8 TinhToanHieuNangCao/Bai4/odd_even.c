#include <mpi.h>
#include <stdio.h>
#define NELEMENTS 5
int main(int argc, char ** argv)
{
int i, rank;
int send_buf[NELEMENTS], recv_buf[NELEMENTS];
MPI_Request req;
MPI_Init(&argc, &argv); // Initialize the MPI execution environment
MPI_Comm_rank(MPI_COMM_WORLD, &rank);
/* -- Create buffers of odd or even number -- */
for (i = 0; i < NELEMENTS; i++) send_buf[i] = 2*i + rank;
if (rank == 0){
MPI_Send(send_buf, NELEMENTS, MPI_INT, 1, 0, MPI_COMM_WORLD);
printf("Da gui\n");
MPI_Recv (recv_buf, NELEMENTS, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
printf("Da nhan\n");
}
if (rank == 1){
MPI_Send(send_buf, NELEMENTS, MPI_INT, 0, 0, MPI_COMM_WORLD);
MPI_Recv (recv_buf, NELEMENTS, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
}
for(int i=0; i< NELEMENTS; i++) printf("%d ", recv_buf[i]);
//printf("\n");
return MPI_Finalize();
}
