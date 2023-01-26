public class Main {
    public static void main(String[] args) {
        int idade = 10;
        int qtdPessoas = 2;

        if (idade>=18 || qtdPessoas>=0){
            System.out.println("Voce pode entrar, aproveite a noite!");
        }
        else {
            System.out.println("Infelizmente voce nao tem idade para entrar, volte acompanhado de pessoas maiores de 18 anos");
        }
    }
}