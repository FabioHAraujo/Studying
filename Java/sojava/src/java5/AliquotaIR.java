package java5;

public class AliquotaIR {
	public static void main(String[] args) {

		double salario = 3800.00;
	
		if(salario<1900)
		{
			System.out.println("Voce esta isento do Imposto de Renda");
		}
		else if(salario>=1900 && salario<=2800) {
			System.out.println("Voce pagara imposto de R$" + salario * 0.075);
		}
		else if(salario>2800 && salario<=3751) {
			System.out.println("Voce pagara imposto de R$" + salario * 0.15);
		}
		else if(salario>3751 && salario<=4664) {
			System.out.println("Voce pagara imposto de R$" + salario * 0.225);
		}
	}
}