public class SumArraySeri {
    public static void main(String[] args) {
		int m = 200000000;
		long a[] = new long[m];
		for (int i=0;i<m;i++) {
			a[i] = i*2;
		}
		long start_time = System.nanoTime();
        long sum = 0;
        for (int i = 0; i < m; i++) {
            sum += a[i];
        }
        System.out.println("Tuan Tu=================");
        System.out.println("Tổng của mảng là: " + sum);
        long end_time = System.nanoTime();
		long excute_time = end_time - start_time;
		System.out.println("\n Sum = " + sum + "\n Time excute: " + excute_time/1000000 + " mili_second");
    }
}
