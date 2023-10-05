function teste1(num) {
    if(num>7)
        console.log(num)
        console.log('Final')
        // Vai imprimir Final sempre, pois está fora do bloco
}

teste1(6)
teste1(8)

function teste2(num) {
    if(num>7); {
        console.log(num)
    }
    // Vai imprimir qualquer coisa que for enviada, pois o if está com ;
    // encerrando a senstença. Esse bloco de chaves não tem condição.
}

teste2(6)
teste2(8)