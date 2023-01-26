package java5;

public class EscopoDeVariaveis {
	public static void main(String[] args) {
		int idade = 20;
		int qtdPessoas = 2;
		boolean acompanhado;
		
		//boolean acompanhado = qtdPessoas > 1;
		
		if (qtdPessoas>1) {
			acompanhado = true;
		}
		else {
			acompanhado = false;
		}
		
		if (idade>=18 && acompanhado) {
			System.out.println("To com ela");
		}
		else {
			System.out.println("Infelizmente nao rolou");
		}
	}
}
