
public final class Book extends Publication {
	float price;
	public Book(String title) {
		super(title);
		// TODO Auto-generated constructor stub
	}

	public Book(String title, int year) {
		super(title, year);
		// TODO Auto-generated constructor stub
	}
	public Book(String title, int year,float price) {
		super(title, year);
		this.price=price;
		// TODO Auto-generated constructor stub
	}

	public float getPrice() {
		return price;
	}

	public void setPrice(float price) {
		this.price = price;
	}
	 public String toString() {
	        return "[ Tua: " + this.getTitle() + "; Nam xuat ban: "+ this.getYear() + "; Gia: "+ this.price+ "]";
	    }
	

}
