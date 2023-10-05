const resultado = (nota) => (nota >= 7 ? "Aprovado" : "Reprovado");

console.log(typeof resultado);
console.log(resultado(7.1));
console.log(resultado(7));
console.log(resultado(6));
console.log(resultado(6.8));
