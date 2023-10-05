// par nome/valor ou chave/valor
const saudacao = "Opa"; // contexto léxico 1

function exec() {
    const saudacao = "Faaaaaala"; // contexto léxico 2
    return saudacao;
}

// Objetos são grupso aninhados de pares nomes/valor
const cliente = {
    nome: "Pedro",
    idade: 30,
    peso: 90,
    endereco: {
        logradouro: "Rua Muito Legal",
        numero: 123,
    },
};

console.log(saudacao);
console.loog(exec());
console.loog(cliente);
