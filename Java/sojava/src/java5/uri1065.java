package java5;

import java.util.Scanner;

public class uri1065 {
	public static void main(String[] args) {
		Scanner sc = new Scanner (System.in);
		int pares = 0;
		int qtd = 5;
		int[] vetor;
		vetor = new int[qtd];
		for(int i=0; i<qtd; i++) {
			vetor[i] = sc.nextInt();
		}
		for(int i=0; i<qtd; i++) {
			if(vetor[i]%2==0) {
				pares++;
			}
		}
		System.out.println(pares+" valores pares");
	}
}
