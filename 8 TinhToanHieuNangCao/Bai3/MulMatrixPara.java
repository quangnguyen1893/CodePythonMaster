import java.util.Scanner;

public class MulMatrixPara extends Thread {
	private int n;
	private int st;
	private int en;
	private int[][] result;
	private int[][] matrix1;
	private int[][] matrix2;

	public MulMatrixPara(int n, int st, int en, int[][] result, int[][] matrix1, int[][] matrix2) {
		this.result = result;
		this.matrix1 = matrix1;
		this.matrix2 = matrix2;
		this.st = st;
		this.en = en;
		this.n = n;
	}

	public static int[][] createMatrix(int n) {
		int[][] matrix = new int[n][n];
		for (int r = 0; r < n; r++) {
			for (int c = 0; c < n; c++) {
				matrix[r][c] = c;
			}
		}
		return matrix;
	}

	public void run() {
		for (int row = st; row < en; row++) {
			for (int col = 0; col < n; col++) {
				result[row][col] = 0;
				for (int j = 0; j < n; j++) {
					result[row][col] += matrix1[row][j] * matrix2[j][col];
				}
			}
		}
	}

	private static void print2dArray(int[][] matrix) {
		for (int r = 0; r < matrix.length; r++) {
			for (int c = 0; c < matrix[0].length; c++) {
				System.out.print(matrix[r][c] + "\t");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) throws InterruptedException {
		int cpu = Runtime.getRuntime().availableProcessors();
		// System.out.println("Nhap so luong hang x cot cua Matrix: ");
		// Scanner sc = new Scanner(System.in);
		// int n = sc.nextInt();
		int n = 2000;

		int[][] first = createMatrix(n);
		int[][] second = createMatrix(n);
		int[][] result = new int[n][n];
		MulMatrixPara t[] = new MulMatrixPara[cpu];

		int size = n / cpu;
		int startIndex = 0;
		int endIndex;

		long start_time = System.nanoTime();

		for (int i = 0; i < cpu; i++) {
			if (i == cpu - 1) {
				endIndex = n;
			} else {
				endIndex = startIndex + size;
			}
			t[i] = new MulMatrixPara(n, startIndex, endIndex, result, first, second);
			startIndex = endIndex;
		}

		for (int i = 0; i < cpu; i++) {
			t[i].start();
		}
		for (int i = 0; i < cpu; i++) {
			t[i].join();
		}
		print2dArray(result);
		long end_time = System.nanoTime();
		long excute_time = end_time - start_time;
		System.out.println("Time excute: " + excute_time / 1000000 + " mili_second");
	}

}