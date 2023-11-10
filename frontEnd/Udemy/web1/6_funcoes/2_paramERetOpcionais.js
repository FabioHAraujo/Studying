/* 
ABREVIEI O NOME DO ARQUIVO POIS ERA UMA SACANAGEM.
MAS BASICAMENTE, PARAMETROS E RETORNO SÃO OPCIONAIS.
*/
function area(largura, altura) {
    const area = largura * altura
    if (area > 20) {
        console.log(`Valor acima do permitido: ${area}m²`)
    }
    else {
        return area
    }
}

console.log(area(5,5))
console.log(area(2,5))
console.log(area(2))
console.log(area(2, 3, 4, 5))