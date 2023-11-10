function soma () {
    let soma = 0
    for (i in arguments) {
        soma += arguments[i]
    }
    return soma
}

console.log(soma(1,2,3,4,5,6,7,8,9))
console.log(soma(1,9))
console.log(soma(1.1, 2.2, 3.3))
console.log(soma(1,2,3,4,5,6,7,8,'Teste'))
console.log(soma(1,2,3,'Pastel',5,6,7,8,'Teste')) // Depois de colocar uma string na soma, tudo será tratado como string e fará apenas concatenação
console.log(soma('Pastel','Docinho','Teste')) // Como let soma é iniciado com 0, concatenará 0 que é soma inicial.

