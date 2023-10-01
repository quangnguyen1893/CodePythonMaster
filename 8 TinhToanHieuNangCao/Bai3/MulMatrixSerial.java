import java.util.Scanner;

public class MulMatrixSerial {

	public static int[][] createMatrix(int n) {
		int[][] matrix = new int[n][n];

		for (int r = 0; r < n; r++) {
			for (int c = 0; c < n; c++) {
				matrix[r][c] = c;
			}
		}
		return matrix;
	}

	private static void multiply(int[][] first, int[][] second,int n) {
		int row = n;
		int column = n;
		int[][] sum = new int[n][n];
	
		for (int r = 0; r < row; r++) {
			for (int c = 0; c < column; c++) {
				sum[r][c]=0;
				for (int k = 0; k < column; k++) {
					sum[r][c] = sum[r][c] + first[r][k] * second[k][c];	
				}
			}
		}
		// print2dArray(sum);
	}

	private static void print2dArray(int[][] matrix) {
		for (int r = 0; r < matrix.length; r++) {
			for (int c = 0; c < matrix[0].length; c++) {
				System.out.print(matrix[r][c] + "\t");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		// System.out.println("Nhap so luong hang x cot cua Matrix: ");
		// Scanner sc = new Scanner(System.in);
		// int n = sc.nextInt();
		int n = 2000;
		long start_time = System.nanoTime();

		int[][] first = createMatrix(n);
		int[][] second = createMatrix(n);

		// System.out.println("First Matrix:\n");
		// print2dArray(first);

		// System.out.println("Second Matrix:\n");
		// print2dArray(second);

		// System.out.println("Result Matrix:\n");
		multiply(first,second,n);

		long end_time = System.nanoTime();
		long excute_time = end_time - start_time;
		// System.out.println("Time excute: " + excute_time/1000000 + " mili_second");
		System.out.println(excute_time/1000000);
	}

	
}