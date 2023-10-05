// Funcao sem retorno

function imprimirSoma(a, b) {
    console.log(a + b);
}

imprimirSoma(2, 3);
imprimirSoma(2);
imprimirSoma(2, 3, 4, 5, 6, 7, 8); // Se a função só aceita 2 parâmetros, o restante é ignorado
imprimirSoma(2, 10, 4, 5, 6, 7, 8); // Se a função só aceita 2 parâmetros, o restante é ignorado

// Funcao com retorno

function soma(a, b = 0) {
    return a + b;
}

soma(2, 3);
console.log(soma(2, 3));
console.log(soma(2));
console.log(soma());
