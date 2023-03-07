package java5;

import java.util.Scanner;

public class PlusMinus {
	public static void main(String[] args) {
		Scanner sc = new Scanner (System.in);
		int positives=0;
		int negatives=0;
		int zeros=0;
		int[] array;
		int qtd=0;
		array = new int[qtd];
		for(int i=0; i<qtd; i++) {
			array[i] = sc.nextInt();
			if(array[i]<0) {
				negatives++;
			}
			else if(array[i]>0) {
				positives++;
			}
			else {
				zeros++;
			}
		}
		System.out.println("Teste"+String.format("%.6f",qtd/negatives));
	}
}
