function tocaSom (idAudio) {
    document.querySelector(idAudio).play()
}

const listaDeTeclas = document.querySelectorAll('.tecla');

for (let i=0; i<9; i++){
    listaDeTeclas[i].onclick = function () {
        tocaSom ('#som_tecla_pom');
    }
}