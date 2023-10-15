#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

#define N 4
#define size 4

void printMatrix(int matrix[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

void matrixMultiply(int a[N][N], int b[N][N], int result[N][N], int start_row, int end_row) {
    for (int i = start_row; i < end_row; i++) {
        for (int j = 0; j < N; j++) {
            result[i][j] = 0;
            for (int k = 0; k < N; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

void sendMatrix(int matrix[N][N], int rows, int dest, int tag) {
    for (int i = 0; i < rows; i++) {
        MPI_Send(matrix[i], N, MPI_INT, dest, tag, MPI_COMM_WORLD);
    }
}

void receiveMatrix(int matrix[N][N], int rows, int source, int tag) {
    for (int i = 0; i < rows; i++) {
        MPI_Recv(matrix[i], N, MPI_INT, source, tag, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    }
}

int main(int argc, char** argv) {
    int rank, num_procs;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

    int local_N = N / size;
    int local_a[local_N][N], local_b[N][N], local_result[local_N][N];

    if (rank == 0) {
        int matrixA[N][N] = {{1, 2, 3, 4},
                             {5, 6, 7, 8},
                             {9, 10, 11, 12},
                             {13, 14, 15, 16}};

        int matrixB[N][N] = {{17, 18, 19, 20},
                             {21, 22, 23, 24},
                             {25, 26, 27, 28},
                             {29, 30, 31, 32}};

        // Distribute matrix B to all processes
        for (int i = 1; i < size; i++) {
            sendMatrix(matrixB, N, i, 1);
        }

        // Distribute matrix A rows to all processes
        for (int i = 1; i < size; i++) {
            sendMatrix(&matrixA[i * local_N], local_N, i, 2);
        }

        // Split data for process 0
        for (int i = 0; i < local_N; i++) {
            for (int j = 0; j < N; j++) {
                local_a[i][j] = matrixA[i][j];
            }
        }
    } else {
        // Receive matrix B
        receiveMatrix(local_b, N, 0, 1);

        // Receive matrix A rows
        receiveMatrix(local_a, local_N, 0, 2);
    }

    // Perform local matrix multiplication
    matrixMultiply(local_a, local_b, local_result, 0, local_N);

    // Gather results in process 0
    if (rank == 0) {
        for (int i = 1; i < size; i++) {
            receiveMatrix(&local_result[i * local_N], local_N, i, 3);
        }
    } else {
        sendMatrix(local_result, local_N, 0, 3);
    }

    // Print the final result in process 0
    if (rank == 0) {
        printf("Ma trận A sau khi nhân:\n");
        printMatrix(local_result);
    }

    MPI_Finalize();

    return 0;
}
