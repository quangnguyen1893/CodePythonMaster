
import java.io.File;
import java.util.*;

import com.db4o.*;
import com.db4o.config.Configuration;
import com.db4o.config.EmbeddedConfiguration;
import com.db4o.config.ObjectClass;
import com.db4o.config.ObjectField;
import com.db4o.query.*;


public class Main1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// 1. Xoá CSDL nếu đã có
		
		// 2. Tạo mới và mở CSDL
		
		
		
        /** 3. Tạo  publication  ("Fundamentals of Database Systems", 2015) với các tác giả : 
		
		("Ramez Elmasri"); 
		("Shamkant B. Navathe"); **/
		
		
		//4. Lưu vào CSDL publication vừa tạo
			
		//5. Truy vấn QBE : tìm tác giả Ramez Elmasri  và cho nhận xét
			System.out.println("------- QBE : Author -----------");
			
			
			//6. Hiển thị tất cả Publication 
			System.out.println("----------- QBE : All Publications ---------------");
			
			
			// Native
			System.out.println("---------native & simple  & comparision ------------");
			//7. Thêm vào CSDL 2 publication bất kỳ có năm sau 1990
			// 8.Tìm Tất cả Publication từ năm 1990 trở về sau và sắp xếp theo thứ tự theo tên bài báo 
			
			//9. Tìm Tất cả Publication từ năm 1990 đến năm 2000 hoặc có tựa là "Java Programming"
			System.out.println("---------native & complex  ------------");
				
				
			
			/***** SODA****/
			
			System.out.println("---------SODA------------");
			// 10.  Tìm Tất cả Publication từ năm 1990 và có tựa là "Java Programming"
			
			
			/**** UPDATE SIMPLE************/
			//11. Cập nhật lại ngày sinh cho tác giả  Ramez Elmasri là 20/10/1956
			
			//12. HIển thị kết quả cập nhật
			
			/********  UPDATE COMPLEX**************/
			//13. Cap nhat lai ngay sinh cho tác giả Ramez Elmasri 20/10/1945 và năm xuất bản cho tất cả các publication là 2008
			System.out.println("---------UPDATE COMPLEX ------------");
			
			//14. In kết quả gồm tên năm sinh  tựa và năm xuất bản các pub của tác giả vừa cập nhật để kiểm tra 
			//15. Đóng CSDL sau đó mở lại
			// 16. Làm lại câu 14 và nhận xét
			
			 //17. Đặt lại cấu hình cho phép cập nhật cascade. 
			 // 18. Chạy lại chương trình để kiểm tra cập nhật cascade
			 //19. Thêm hai class java định nghĩa cho Article(tự thêm) và Book(có sẵn) kế thừa Publication như hình trong phần giới thiệu db4O 
			// 20.Thêm Quyển sách "Gone with the wind", tác giả  Margaret Mitchell, năm xuất bản 2011, Giá 12.98 
			//21. Kiểm tra rằng tác giả và publication cũng được lưu
			

	
				
		} finally {
            db.close();
        }	

	}
	
	
	
}
