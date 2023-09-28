const escola = "Cod3r"

console.log(escola.charAt(4))
console.log(escola.charAt(5)) // não gera erro, apenas imprime nada
// JavaScript tenta ajudar, evitando erros o tempo todo.
console.log(escola.charAt(3))
console.log(escola.charCodeAt(3)) // imprime o unicode, usado no HTML.
console.log(escola.indexOf('3'))
console.log(escola.indexOf('9')) // retorna -1 se não existir, então é importante tratar isso.

console.log(escola.substring(1)) // imprime a partir do index.
console.log(escola.substring(2)) // imprime a partir do index.
console.log(escola.substring(0,3))

console.log("Escla ".concat(escola).concat("!"))
console.log("Escla " + escola + "!")
console.log("3" + 2) // Não soma, apenas concatena, pois + tem signifcado de concatenação.
console.log(escola.replace('3', 'e'))
console.log(escola.replace(/\w/g, 'e')) // usando regex


 /* também regex, transforma em array.
  Professor não vai explicar
  muito pois vende curso sobre isso, jabah kkkk */
console.log('Ana,Maria,Pedro'.split(/,/))