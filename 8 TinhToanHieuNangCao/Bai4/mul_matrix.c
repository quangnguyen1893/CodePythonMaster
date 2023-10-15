#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

#define N 4
#define size 2

void printMatrix(int matrix[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

void matrixMultiply(int a[N][N], int b[N][N], int result[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            result[i][j] = 0;
            for (int k = 0; k < N; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

void splitMatrix(int original[N][N], int start_row, int end_row, int result[end_row - start_row][N]) {
    for (int i = start_row; i < end_row; i++) {
        for (int j = 0; j < N; j++) {
            result[i - start_row][j] = original[i][j];
        }
    }
}

int main(int argc, char** argv) {
    int rank, num_procs;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

    int local_N = N / size;
    int local_a[local_N][N], local_b[N][N], local_result[local_N][N];

    // Ma trận A và B chỉ được khởi tạo ở quá trình có rank là 0
    if (rank == 0) {
        int matrixA[N][N] = {{1, 2, 3, 4},
                             {5, 6, 7, 8},
                             {9, 10, 11, 12},
                             {13, 14, 15, 16}};

        int matrixB[N][N] = {{17, 18, 19, 20},
                             {21, 22, 23, 24},
                             {25, 26, 27, 28},
                             {29, 30, 31, 32}};

        // Phân phối dữ liệu cho các quá trình
        for (int i = 1; i < size; i++) {
            // Gửi ma trận B đến tất cả các quá trình
            MPI_Send(matrixB, N * N, MPI_INT, i, 1, MPI_COMM_WORLD);
        }

        // Chia dữ liệu cho quá trình 0
        splitMatrix(matrixA, 0, local_N, local_a);
    } else {
        // Nhận ma trận B từ quá trình có rank là 0
        MPI_Recv(local_b, N * N, MPI_INT, 0, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    }

    // Phân phối ma trận A cho tất cả các quá trình
    MPI_Bcast(local_a, local_N * N, MPI_INT, 0, MPI_COMM_WORLD);

    // Thực hiện phép nhân ma trận local
    matrixMultiply(local_a, local_b, local_result);

    // Gom kết quả từ tất cả các quá trình
    MPI_Gather(local_result, local_N * N, MPI_INT, local_a, local_N * N, MPI_INT, 0, MPI_COMM_WORLD);

    // In kết quả
    if (rank == 0) {
        printf("Ma trận A sau khi nhân:\n");
        printMatrix(local_a);
    }

    MPI_Finalize();

    return 0;
}
