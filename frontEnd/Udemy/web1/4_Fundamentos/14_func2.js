// Armazenando função em uma variável
const imprimeSoma = function (a, b) {
    console.log(a + b);
};

imprimeSoma(2, 3);

// Armazenando função arrow em uma variável
const soma = (a, b) => {
    return a + b;
};

console.log(soma(2, 3));

// Retorno Implícito

const subtracao = (a, b) => a - b;
console.log(subtracao(2, 3));

const imprimir = (a) => console.log(a);
imprimir("Legal!!!");
