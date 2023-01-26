package java5;

public class SwitchCase {
	public static void main(String[] args) {
		char letra = 'c';
		
		switch (letra) {
	    case 'a':
	            System.out.println("Eh A");
	            break;
	    case 'b':
	            System.out.println("Eh B");
	            break;
	    case 'c':
	            System.out.println("Eh C");
	            break;
	    default:
	            System.out.println("Infelizmente, nao sei essa letra");
		}
	}
}
