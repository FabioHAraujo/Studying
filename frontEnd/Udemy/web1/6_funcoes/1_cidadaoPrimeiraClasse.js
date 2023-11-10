// Função em JS é First Class Object ou First Class Citizen
// Higher-order function

// Funcoes em javascript sempre retornam algo.
// Mesmo que você não perceba, quando faz uma função sem retorno,
// esta retorna Undefined.

// Criando de forma Literal
function fun1() {}

// Armazneando em uma Variável
const fun2 = function () {};

// Armazenando em um Array
const array = [function (a, b ) { return a+b }, fun1, fun2]
console.log(array[0](2,3))

// Armazenando em um objeto
const obj = { }
obj.falar = function () { return "Opa"}
console.log(obj.falar())

// Passar a função como paramêtro
function run(fun) {
    fun()
}

run(function () {console.log('Executando...')})

// Uma função pode retornar/conter uma função
function soma(a,b) {
    return function (c) {
        console.log(a+b+c)
    }
}

soma(2, 3)(4) // O 4 está dentro do segundo parênteses, 
//pois este é o retorno da função soma, que retorna uma func.

const cincoMais = soma(2,3)
cincoMais(4)