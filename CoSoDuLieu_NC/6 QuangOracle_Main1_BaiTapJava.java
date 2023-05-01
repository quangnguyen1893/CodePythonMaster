import java.io.File;
import java.io.ObjectInputStream.GetField;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;
import com.db4o.query.Constraint;
import com.db4o.query.Predicate;
import com.db4o.query.Query;

// đổi font: Edit -> set encoding "UTF8"
public class Main {

	public static void main(String[] args) {
		
		// 1. Xoá CSDL nếu CSDL đã có
		new File("D:/db4o/db4oExample.db4o").delete();
		
		//2. Mở CSDL nếu đã có, ngược lại tạo mới và mở
		ObjectContainer db = Db4oEmbedded.openFile("D:/db4o/db4oExample.db4o");
		//3. Thêm vào CSDL 7 đối tượng (Diem,20) (An,30) (Diem,18) (Phuc,30) (Tam,40) (Phuc,25) (Thu,40)
		
		db.store(new Person("Diem", 20));
		db.store(new Person("An", 30));
		db.store(new Person("Diem", 18));
		db.store(new Person("Phuc", 30));
		db.store(new Person("Tam", 40));
		db.store(new Person("Phuc", 25));
		db.store(new Person("Thu", 40));
		// Truy vấn QBE
		
		// 4. Tìm những người tên Diễm 
		System.out.println("-Tim nhung nguoi co ten Diem");
		Person p = new Person();
		p.setName("Diem");
		ObjectSet<Person> t = db.queryByExample(p);
		for (Person a: t){
			System.out.println(a.toString());
		}
		System.out.println("---------------------");
		// 5. Tìm những người có tuổi 30  	
		System.out.println("-Tim nhung nguoi co tuoi 30 ");
		Person per_age = new Person();
		per_age.setAge(30);
		ObjectSet<Person> age = db.queryByExample(per_age);
		for (Person c: age){
			System.out.println(c.toString());
		}
		System.out.println("---------------------");
		// 6. Tìm tất cả mọi người sử dụng thuộc tính class 
		System.out.println("-Tim tat ca su dung class");
		ObjectSet<Person> pubs = db.queryByExample(Person.class);
		for (Person publication: pubs) {
			 System.out.println(publication.toString());
		 }
					
		System.out.println("---------------------");
		
		// 7. Tìm tất cả mọi người sử dụng hàm tạo rỗng
		System.out.println("-Tim tat ca su dung hàm tạo rỗng");
		Person rong = new Person();
		ObjectSet<Person> p_rong = db.queryByExample(rong);
		for (Person pup: p_rong) {
			 System.out.println(pup.toString());
		 }
		System.out.println("---------------------");
		//Native Query
		System.out.println("----------NATIVE-----------");		
		System.out.println("8. Tìm tất cả người tuổi từ 20 đến 30");
		ObjectSet<Person> person_s = db.query(new Predicate<Person>() {
			public boolean match(Person naperson) {
				return naperson.getAge() >= 20 && naperson.getAge() <= 30;
			}
		});
		for (Person naP: person_s) {
			System.out.println(naP.toString());
		}
		System.out.println("---------------------");
			 
		System.out.println("9.Tìm tất cả người tên Diễm và có tuổi 20");
		ObjectSet<Person> person_n = db.query(new Predicate<Person>() {
			public boolean match(Person nnaperson) {
				return nnaperson.getName().equals("Diem") && nnaperson.getAge() == 20;
			}
		});
		for (Person naN: person_n) {
			System.out.println(naN.toString());
		}
		//SODA
		System.out.println("----------SODA-----------");
		System.out.println("----------10. SODA: tat ca moi nguoi");
		Query query = db.query();
		query.constrain(Person.class); 
		ObjectSet<Person> soda_all = query.execute();
		for (Person soda_p_all : soda_all) {
			System.out.println(soda_p_all.toString()); 
		}
		System.out.println("----------11. SODA: tat ca moi nguoi: sap xep theo ten-----------");
		Query query_ten = db.query();
		query_ten.constrain(Person.class);
		query_ten.descend("name").orderAscending();
		ObjectSet<Person> soda_sxten = query_ten.execute();
		for (Person soda_p_ten : soda_sxten) {
			System.out.println(soda_p_ten.toString()); 
		}
				 
		System.out.println("----------12. SODA: Nhung nguoi ten Diem-----------");
		Query query_tenDiem = db.query();
		query_tenDiem.constrain(Person.class);
		query_tenDiem.descend("name").constrain("Diem").equal();
		ObjectSet<Person> soda_tenDiem = query_tenDiem.execute();
		for (Person soda_p_tenDiem : soda_tenDiem) {
			System.out.println(soda_p_tenDiem.toString()); 
		}
		System.out.println("----------13. SODA: Nhung nguoi khac 30 tuoi -----------");
		Query query_khac30 = db.query();
		query_khac30.constrain(Person.class);
		query_khac30.descend("age").constrain(Integer.valueOf(30)).not();
		ObjectSet<Person> soda_khac30 = query_khac30.execute();
		for (Person soda_p_khac30 : soda_khac30) {
			System.out.println(soda_p_khac30.toString()); 
		}
		System.out.println("----------14. SODA: Nhung nguoi tuoi tu 20 den 30 tuoi -----------");
		Query query_2030 = db.query();
		query_2030.constrain(Person.class);
		Constraint constr = query_2030.descend("age").constrain(Integer.valueOf(31)).smaller();
		query_2030.descend("age").constrain(Integer.valueOf(19)).greater().contains().and(constr);
		ObjectSet<Person> soda_2030 = query_2030.execute();
		for (Person soda_p_2030 : soda_2030) {
			System.out.println(soda_p_2030.toString()); 
		}
				 
		System.out.println("----------15. SODA: Nhung nguoi ten bat dau bang T -----------");
		Query query_tenT = db.query();
		query_tenT.constrain(Person.class);
		query_tenT.descend("name").constrain("T").startsWith(false); // true: phân biệt hoa thường
		ObjectSet<Person> soda_tenT = query_tenT.execute();
		for (Person soda_p_tenT : soda_tenT) {
			System.out.println(soda_p_tenT.toString()); 
		}
		db.close();
	}

}
