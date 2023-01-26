public class java4 {
    public static void main(String[] args) {
        System.out.println("Testando Condicionais");

        int idade = 17;
        int qtdPessoas = 2;
        if (idade >=  18){
            System.out.println("Voce tem mais de 18 anos");
            System.out.println("Seja bem-vindo");
        }
        else {
            if(qtdPessoas>0){
                System.out.println("Voce pode entrar, pois esta acompanhado");
            }
            else {
                System.out.println("Infelizmente voce nao pode entrar");
            }
        }
    }
}
