import java.io.File;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;


public class Main {

	public static void main(String[] args) {
		
		// 1. Xoá CSDL nếu CSDL đã có
		
		//2. Mở CSDL nếu đã có, ngược lại tạo mới và mở
		
		//3. Thêm vào CSDL 7 đối tượng (Diem,20) (An,30) (Diem,18) (Phuc,30) (Tam,40) (Phuc,25) (Thu,40)
		
		
		// Truy vấn QBE
		
		// 4. Tìm những người tên Diễm 
		System.out.println("-Tim nhung nguoi co ten Diem");
		 //	...		
		System.out.println("---------------------");
		// 5. Tìm những người có tuổi 30  	
		System.out.println("-Tim nhung nguoi co tuoi 30 ");
			//	...	 
		System.out.println("---------------------");
		// 6. Tìm tất cả mọi người sử dụng thuộc tính class 
		System.out.println("-Tim tat ca su dung class");
			// ...		
					
		System.out.println("---------------------");
		
		// 7. Tìm tất cả mọi người sử dụng hàm tạo rỗng
		System.out.println("-Tim tat ca su dung hàm tạo rỗng");
			//...
		System.out.println("---------------------");
		//Native Query
		System.out.println("----------NATIVE-----------");		
		System.out.println("8. Tìm tất cả người tuổi từ 20 đến 30");
		    
		System.out.println("---------------------");
			 
		System.out.println("9.Tìm tất cả người tên Diễm và có tuổi 20");
			    
		//SODA
		System.out.println("----------SODA-----------");
		System.out.println("----------10. SODA: tat ca moi nguoi");
				 
		System.out.println("----------11. SODA: tat ca moi nguoi: sap xep theo ten-----------");
			
				 
		System.out.println("----------12. SODA: Nhung nguoi ten Diem-----------");
				
		 System.out.println("----------13. SODA: Nhung nguoi khac 30 tuoi -----------");
				 
		System.out.println("----------14. SODA: Nhung nguoi tuoi tu 20 den 30 tuoi -----------");
				 
				 
		System.out.println("----------15. SODA: Nhung nguoi ten bat dau bang T -----------");
				 
		db.close();
	}

}
