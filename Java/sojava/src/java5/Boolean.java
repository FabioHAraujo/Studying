package java5;

public class Boolean {
	public static void main(String[] args) {
		int idade = 20;
		int qtdPessoas = 2;
		boolean acompanhado = qtdPessoas > 1;
		
		if (idade>=18 && acompanhado) {
			System.out.println("To com ela");
		}
		else {
			System.out.println("Infelizmente nao rolou");
		}
	}
}
