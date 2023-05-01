
import java.util.*;


public class Author {
	
	private String name; 
	private Date birthday; 
	private Set<Publication> pubs;
	
	public Author() {
	}
	
    public Author(String name) {
		
		this.name = name;
		
		this.pubs = new  HashSet<Publication>();
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Date getBirthday() {
		return birthday;
	}
	public void setBirthday(Date birthday) {
		this.birthday = birthday;
	}
	public Set<Publication> getPubs() {
		return pubs;
	}
	public void setPubs(Set<Publication> pubs) {
		this.pubs = pubs;
	}
	public void printAut(){
		 
		System.out.print("Author: "); 
		 System.out.print(this.getName()); 
		 if (this.getBirthday()!=null) System.out.println(" - Birthday: "+ this.getBirthday().toString());
		 System.out.println ("Pubs: "); 
		 for (Publication p : this.getPubs())
	 			System.out.println("            -  "+ p.getTitle());
	
}
	
	//// Viết phương thức addPub(Publication author) để thêm các Publication cho một Author  
	
	public boolean addPub(Publication pub) {
		// Viết code 
	}
}
