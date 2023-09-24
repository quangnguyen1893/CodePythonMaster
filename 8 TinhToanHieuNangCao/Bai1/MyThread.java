
public class MyThread  extends Thread{
	private String name;
	
	public MyThread(String n) {
		name = new String(n);
		System.out.println(name + "  is started  ... " );
	}
	
	
	public void run() {
		for (int i=0; i < 50; i++) {
			System.out.println(name + " is running at step " + i);
			try {
				Thread.sleep(300);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		MyThread huy  = new MyThread("Huy");
		huy.start();
		
		MyThread luan  = new MyThread("Luan");
		luan.start();
		
		MyThread thu  = new MyThread("Thu");
		thu.start();

		
		

	}

}
