#include <mpi.h>
#include <stdio.h>
int main(int argc, char ** argv)
{
	int i, rank, size;
	/* -- Initialize MPI environment -- */
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	/* -- Create multiplication table -- */
	printf ("[Rank # %d]\n", rank);
	for (i = 1; i <= 10; i++){
	printf ("%d x %d = %d\n",rank+1,i,i*(rank+1));
	}
	MPI_Finalize();
	return 0;
}
