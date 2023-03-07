
public class CriaConta {
	public static void main(String[] args) {
		conta primeiraConta = new conta();
		primeiraConta.saldo = 200;
		primeiraConta.agencia = 01;
		primeiraConta.numero = 1;
		primeiraConta.titular = "Francisco Paulo";
		System.out.println(primeiraConta.saldo);
		System.out.println(primeiraConta.agencia);
		System.out.println(primeiraConta.numero);
		System.out.println(primeiraConta.titular);
		
		conta segundaConta = new conta();
		segundaConta.saldo = 50;
		segundaConta.agencia = 01;
		segundaConta.numero = 2;
		segundaConta.titular = "Maria Antonieta";
		System.out.println(segundaConta.saldo);
		System.out.println(segundaConta.agencia);
		System.out.println(segundaConta.numero);
		System.out.println(segundaConta.titular);
		
		conta terceiraConta = segundaConta;
		System.out.println("Saldo da Terceira conta "+terceiraConta.saldo);
		terceiraConta.saldo+=100;
		System.out.println("Saldo da Terceira conta "+terceiraConta.saldo);
		System.out.println(segundaConta.saldo);
	}
}
