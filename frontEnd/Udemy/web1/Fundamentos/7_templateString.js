const nome = 'Rebeca'
const concatenacao = 'Olá ' + nome + '!'
const template =  `
    Olá
    ${nome}!
` // Só mostrando que suporta quebra de linha

console.log(concatenacao)
console.log(template)

// expressoes...
console.log(`1 + 1 = ${1 + 1}`)
console.log(`1 + 1 = ${1 + 4}`)

const up = texto => texto.toUpperCase()
console.log(`Ei... ${up('cuidado')}!`)