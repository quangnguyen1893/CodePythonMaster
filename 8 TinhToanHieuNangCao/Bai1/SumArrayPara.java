public class SumArrayPara extends Thread {
	public long resultThread = 0;
	private long ar[];
	private int st;
	private int en;
	
	public SumArrayPara(int start, int end, long arr[]) {
		st = start;
		en = end;
		ar = arr;
	}
	
	public void run() {
		for(int i = st; i < en; i++) {
			resultThread += ar[i];
		}
	}

	public static void main(String[] args) throws InterruptedException{
		int cpu = Runtime.getRuntime().availableProcessors();
		int m = 200000000;
		long ar[] = new long[m];
		for (int i=0;i<m;i++) {
			ar[i] = i*2;
		}

		long start_time = System.nanoTime();
		SumArrayPara t[] = new SumArrayPara[cpu];
		int size = m / cpu;
        int startIndex = 0;
		int endIndex;

		for (int i = 0; i < cpu; i++) {
			if (i == cpu - 1) {
				endIndex = m;
			} else {
				endIndex = startIndex + size;
			}
			t[i] = new SumArrayPara(startIndex, endIndex, ar);
			startIndex = endIndex;
		}

		for(int i=0; i<cpu; i++) {
			t[i].start();
		}
		for(int i=0; i<cpu; i++) {
			t[i].join();
		}
		
		long all_sum = 0;
		for(int i=0; i<cpu; i++) {
			all_sum += t[i].resultThread;
		}
		System.out.println("Song Song=================");
		long end_time = System.nanoTime();
		long excute_time = end_time - start_time;
		System.out.println("\n Sum = " + all_sum + "\n Time excute: " + excute_time/1000000 + " mili_second");

	}

}