package java5;

public class TesteSoma {
	public static void main(String[] args) {
		int count=0;
		int total = 0;
		while(count<=10) {
			total+=count;
			System.out.println(total);
			count++;
		}
		System.out.println("Resultado final foi: "+total);
	}
}
