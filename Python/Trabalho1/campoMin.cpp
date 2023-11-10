#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

int largura = 0;
int altura = 0;

using namespace std;

string criaCampo(int linha, int coluna, int dificuldade);
void atualizarCamposAoRedor(char campo[][20], int linha, int coluna);


int main () {
    srand(static_cast<unsigned>(time(nullptr)));
    cout << "Por favor, digite a altura e largura do campo minado (em quadrados) separados por espaço: \n";
    cin >> altura >> largura;
    int dificuldade = 100;
    string campo = criaCampo(altura,largura,100);
    cout << campo;
}

string criaCampo(int linha, int coluna, int dificuldade){
    char campo[20][20] = {};
    string resultado = {};
    
    for (int i=0; i<linha; i++){
        for (int j=0; j<coluna; j++) {
            int random = rand() % dificuldade;
            if (random > 90) {
                campo[i][j] = '*';
            }
            else {
                campo[i][j] = '-';
            }
        }
    }

    for (int i = 0; i < linha; i++) {
        for (int j = 0; j < coluna; j++) {
            if (campo[i][j] == '*') {
                atualizarCamposAoRedor(campo, i, j);
            }
        }
    }

    for (int i = 0; i < linha; i++) {
        for (int j = 0; j < coluna; j++) {
            resultado += campo[i][j];
        }
        resultado += '\n';
    }

    return resultado;
}

void atualizarCamposAoRedor(char campo[][20], int linha, int coluna) {
    int dx[] = { -1, -1, -1, 0, 0, 1, 1, 1 };
    int dy[] = { -1, 0, 1, -1, 1, -1, 0, 1 };

    for (int i = 0; i < 8; i++) {
        int novaLinha = linha + dx[i];
        int novaColuna = coluna + dy[i];

        if (novaLinha >= 0 && novaLinha < 20 && novaColuna >= 0 && novaColuna < 20) {
            if (campo[novaLinha][novaColuna] == '-') {
                campo[novaLinha][novaColuna] = '1';
            } else if (campo[novaLinha][novaColuna] >= '1' && campo[novaLinha][novaColuna] < '8') {
                campo[novaLinha][novaColuna]++;
            }
        }
    }
}