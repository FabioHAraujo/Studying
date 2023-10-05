let valor; // não inicializada
console.log(valor);

valor = null; //ausêcia de valor

console.log(valor);
// console.log(valor.toString()) // Erro!!!

const produto = {};
console.log(produto.preco);
console.log(produto);

produto.preco = 3.5;
console.log(produto);

produto.preco = undefined; // evitar atribuir undefined, melhor zerar se for
// valor ou apontar para nulo
console.log(!!produto.preco);
console.log(produto);

produto.preco = null; // sem preço
console.log(!!produto.preco); // verifica se está setado
console.log(produto);
